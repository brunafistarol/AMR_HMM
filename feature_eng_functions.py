import os
from Bio import AlignIO
from Bio.Align.Applications import MafftCommandline
import subprocess

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

    os.mkdir(os.path.join(output_directory, 'Pfam_multifasta'))

    for file_path in os.listdir(datadir):
        sequences = read_fasta_file(os.path.join(datadir, file_path))
        for header, sequence in sequences.items():
            output_file_path = os.path.join(output_directory, f'Pfam_multifasta/{header}.fasta')
            write_fasta_file(output_file_path, file_path, sequence)

#Multiple alignments with all multifasta files in a folder
def multiple_alignment(input_directory, output_directory):
    os.mkdir(os.path.join(output_directory, 'Pfam_ma'))
    for protein_family in os.listdir(input_directory):
        input_file_path = os.path.join(input_directory, protein_family)
        output_file_path = os.path.join(output_directory, f'Pfam_ma/{protein_family}')
        mafft_cline = MafftCommandline(input=input_file_path)    # Perform alignment using MAFFT
        stdout, stderr = mafft_cline() 
        with open(output_file_path, 'w') as f:
            f.write(stdout)

def run_hmmbuild(input_directory, output_directory, threads):
    os.mkdir(os.path.join(output_directory, 'Pfam_hmm'))
    for protein_family in os.listdir(input_directory):
        input_file_path = input_directory + f'/{protein_family}'
        protein_family = protein_family.split('.')[0]
        output_file_path = os.path.join(output_directory, f'Pfam_hmm/{protein_family}.hmm')
        command_line = (f'hmmbuild --cpu {threads} {output_file_path} {input_file_path}')
        subprocess.run(command_line, shell=True)

def align_hmm(path_specie):
    path_multifasta = os.path.join(path_specie, 'Pfam_multifasta')
    path_hmm = os.path.join(path_specie, 'Pfam_hmm')
    output_directory = os.path.join(path_specie, 'Pfam_hmm_alig')
    os.mkdir(output_directory)
    for pfam in os.listdir(path_multifasta):
        input_pfam_path = os.path.join(path_multifasta, pfam)
        pfam = pfam.split('.')[0]
        hmm = pfam + '.hmm'
        input_hmm_path = os.path.join(path_hmm, hmm)
        output_file_path = os.path.join(output_directory, f'{pfam}.sto')
        command_line = (f'hmmalign -o {output_file_path} {input_hmm_path} {input_pfam_path}')
        subprocess.run(command_line, shell=True)

def search_hmm(path_specie, threads):
    path_multifasta = os.path.join(path_specie, 'Pfam_multifasta')
    path_hmm = os.path.join(path_specie, 'Pfam_hmm')
    output_directory = os.path.join(path_specie, 'Pfam_hmm_search')
    os.mkdir(output_directory)
    for pfam in os.listdir(path_multifasta):
        input_pfam_path = os.path.join(path_multifasta, pfam)
        pfam = pfam.split('.')[0]
        hmm = pfam + '.hmm'
        input_hmm_path = os.path.join(path_hmm, hmm)
        output_file_path = os.path.join(output_directory, f'{pfam}.tab')
        command_line = (f'hmmsearch --noali --cpu {threads} --tblout {output_file_path} {input_hmm_path} {input_pfam_path}')
        subprocess.run(command_line, shell=True)


