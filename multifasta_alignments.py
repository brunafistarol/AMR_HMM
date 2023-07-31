import os
from Bio import AlignIO
from Bio.Align.Applications import MafftCommandline

def read_fasta_file(file_path):
    sequences = {}
    with open(file_path, 'r') as file:
        sequence = ''
        header = ''
        for line in file:
            if line.startswith('>'):
                if sequence and header:
                    sequences[header] = sequence
                    sequence = ''
                header = line.strip()[1:]
            else:
                sequence += line.strip()
        if sequence and header:
            sequences[header] = sequence
    return sequences

def write_fasta_file(file_path, header, sequence):
    with open(file_path, 'a') as file:
        file.write(f'>{header}\n{sequence}\n')

# Read input fasta files and group sequences by protein family
def get_multifasta(datadir, output_directory):
    
    protein_families = []

    strain = os.listdir(datadir)[0]
    with open(os.path.join(datadir, strain), 'r') as sequences:
        for line in sequences:
            if line[0] == '>':
                protein_families.append(line[1:len(line)-1])

    protein_families = {protein_families[i]: {} for i in range(len(protein_families))}

    os.mkdir(os.path.join(output_directory, 'Pfam_mf'))

    for file_path in os.listdir(datadir):
        sequences = read_fasta_file(os.path.join(datadir, file_path))
        for header, sequence in sequences.items():
            output_file_path = os.path.join(output_directory, f'Pfam_mf/{header}.fasta')
            write_fasta_file(output_file_path, file_path, sequence)

#Multiple alignments with all multifasta files in a folder
def multiple_alignment(input_directory, output_directory):
    os.mkdir(os.path.join(output_directory, 'Pfam_ma'))
    for protein_family in os.listdir(input_directory):
        input_file_path = input_directory + f'{protein_family}'
        output_file_path = os.path.join(output_directory, f'Pfam_ma/{protein_family}')
        mafft_cline = MafftCommandline(input=input_file_path)    # Perform alignment using MAFFT
        stdout, stderr = mafft_cline() 
        with open(output_file_path, 'w') as f:
            f.write(stdout)
