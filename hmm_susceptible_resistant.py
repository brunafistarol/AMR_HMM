import os

with open('feature_eng_functions.py') as f:
    exec(f.read())

antibiotics = ['AMP', 'AUG', 'AXO', 'CHL', 'FIS', 'FOX', 'GEN', 'KAN', 'STR', 'TET', 'TIO']
profile = ['Susceptible', 'Resistant']

root = '/mnt/e/User/bruna.fistarol/HMM/Salmonella/Antibiotics'

for a in antibiotics:
    for p in profile:

        datadir = os.path.join(root, a, p, 'Strains')

        output_directory = os.path.join(root, a, p)

        input_directory = os.path.join(root, a, p)

        #get_multifasta(datadir, output_directory)

        multiple_alignment(input_directory + '/Pfam_multifasta', output_directory)

        run_hmmbuild(input_directory + '/Pfam_ma', output_directory, 28)