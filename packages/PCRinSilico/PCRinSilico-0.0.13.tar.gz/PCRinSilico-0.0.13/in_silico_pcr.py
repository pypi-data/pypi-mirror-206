import os
import pandas as pd
from Bio.Seq import Seq
from Bio.SeqUtils import MeltingTemp
from Bio import SeqIO
import argparse
import itertools


def inSilicoPCR():
    # Define the arguments to be parsed
    parser = argparse.ArgumentParser(description='PCR parameter inputs')
    parser.add_argument('--annealing_temp', type=int, help='Annealing temperature (in Celsius)', default = 60.0)
    parser.add_argument('--salt_concentration', type=float, help='Salt concentration (in nM)', default = 50)
    parser.add_argument('--max_amplicon_len', type=float, help='maximum length of PCR products in nucleotides', default = 2000)
    parser.add_argument('--req_five', type=str, help="Require the 5' end of the primer to bind?", default = True)
    parser.add_argument('--primer_seq', type=str, help="Primer sequences, one per line", required = True)
    parser.add_argument('--ref_fasta_file', type=str, help="Reference fasta file", required = True)
    parser.add_argument('--out_file', type=str, help="Output file name", default = "in_silico_PCR")

    # check if blastn is in the system path
    try:
        status = os.system('which blastn > /dev/null 2>&1')
        if status != 0:
            print('Error: BLAST is not installed.')
            exit(1)
    except OSError as e:
        print('Error:', e)
        exit(1)

    # Check if required arguments are missing and print help message
    args = parser.parse_args()
    if not args.primer_seq or not args.ref_fasta_file:
        parser.print_help()
        exit()

    # Define the inputs
    annealing_temp = args.annealing_temp
    salt_conc = args.salt_concentration
    max_amplicon_len = args.max_amplicon_len
    req_five = args.req_five
    primer_seq = args.primer_seq
    ref_fasta_file = args.ref_fasta_file
    out_file = args.out_file


    def find_binding_positions(primer_seq, ref_fasta_file, annealing_temp, req_five, salt_conc):
        # Run BLAST to search for primer sequence against reference FASTA
        blast_cmd = f"blastn -query {primer_seq} -subject {ref_fasta_file} -task blastn-short -outfmt '6 qseqid sseqid qstart qend sstart send qseq sseq mismatch length' > blast_output.txt"
        os.system(blast_cmd)
        
        blast_df = pd.DataFrame(columns=['Query ID', 'Subject ID', 'Query Start', 'Query End', 'Subject Start', 'Subject End', 'Query Sequence Match', 'Direction', 'Binding Position', 'Mismatches', 'Binding Length'])
        
        with open('blast_output.txt', 'r') as f:
            for line in f:
                fields = line.strip().split('\t')
                qseqid, sseqid, qstart, qend, sstart, send, qseq, sseq, mismatch, length = fields
                direction = '+' if int(sstart) < int(send) else '-'
                binding_pos = sstart if direction == '+' else send
                # Check if primer binds at the specified annealing temperature
                if req_five and int(qstart) >= 2:
                    continue
                tm = MeltingTemp.Tm_NN(Seq(sseq), Na=salt_conc, Mg=0, dnac1=250, dnac2=0, saltcorr=7, nn_table=MeltingTemp.DNA_NN4, selfcomp=False, check=True, shift=0.0)
                if annealing_temp <= tm:
                    blast_df.loc[len(blast_df)] = [qseqid, sseqid, qstart, qend, sstart, send, sseq, direction, binding_pos, mismatch, length]
        return blast_df

    def find_compatible_pairs(blast_df, max_len):
        pairs = itertools.combinations(blast_df.index, 2)
        compatible_pairs = []
        for pair in pairs:
            row1 = blast_df.loc[pair[0]]
            row2 = blast_df.loc[pair[1]]
            amp_size = abs(int(row1['Binding Position']) - int(row2['Binding Position']))
            if amp_size <= max_len and row1['Direction'] != row2['Direction'] and row1['Subject ID'] == row2['Subject ID']:
                if row1['Direction'] == '+':
                    compatible_pairs.append({'qseq1': row1['Query Seq'], 'qstart1': row1['Query Start'], 'qend1': row1['Query End'], 'direction1': row1['Direction'], 'mismatch1': row1['Mismatches'],
                                             'qseq2': row2['Query Seq'], 'qstart2': row2['Query Start'], 'qend2': row2['Query End'], 'direction2': row2['Direction'], 'mismatch2': row2['Mismatches'],
                                             'binding_pos_diff': amp_size, 'reference': row1['Subject ID']})
                else:
                    compatible_pairs.append({'qseq1': row2['Query Seq'], 'qstart1': row2['Query Start'], 'qend1': row2['Query End'], 'direction1': row2['Direction'], 'mismatch2': row2['Mismatches'],
                                             'qseq2': row1['Query Seq'], 'qstart2': row1['Query Start'], 'qend2': row1['Query End'], 'direction2': row1['Direction'], 'mismatch1': row1['Mismatches'],
                                             'binding_pos_diff': amp_size, 'reference': row1['Subject ID']})
        return pd.DataFrame(compatible_pairs)

    with open(primer_seq, 'r') as infile, open(primer_seq+'.fasta', 'w') as outfile:
        # Set a counter to generate unique sequence names
        i = 1
        for line in infile:
            # Remove any leading/trailing whitespace from the sequence
            sequence = line.strip()
            # Generate a unique sequence name
            name = f'sequence{i}'
            i += 1
            # Write the sequence to the output file in FASTA format
            outfile.write(f'>{name}\n{sequence}\n')
            
    blast_df = find_binding_positions(primer_seq+'.fasta', ref_fasta_file, annealing_temp, req_five, salt_conc)

    # Read in the FASTA file as a dictionary of SeqRecord objects
    fasta_dict = SeqIO.to_dict(SeqIO.parse(primer_seq+'.fasta', "fasta"))

    # Iterate through the rows of the DataFrame and replace the Query IDs with sequences
    for i, row in blast_df.iterrows():
        query_id = row["Query ID"]
        if query_id in fasta_dict:
            sequence = str(fasta_dict[query_id].seq)
            blast_df.at[i, "Query ID"] = sequence
        else:
            blast_df.at[i, "Query ID"] = ""

    blast_df = blast_df.rename(columns={'Query ID': 'Query Seq'})

    print("Writing output to " + out_file + '.tsv')
    amp_df = find_compatible_pairs(blast_df, max_len=max_amplicon_len)
    amp_df.to_csv(out_file + '.tsv', index=False, sep="\t")


    os.remove(primer_seq+'.fasta')
    os.remove("blast_output.txt")
