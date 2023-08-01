import os
import subprocess

def run_hmmbuild(input_directory, output_directory, threads):
    os.mkdir(os.path.join(output_directory, 'Pfam_hmm'))
    for protein_family in os.listdir(input_directory):
        input_file_path = input_directory + f'/{protein_family}'
        protein_family = protein_family.split('.')[0]
        output_file_path = os.path.join(output_directory, f'Pfam_hmm/{protein_family}.hmm')
        command_line = (f'hmmbuild --cpu {threads} {output_file_path} {input_file_path}')
        subprocess.run(command_line, shell=True)