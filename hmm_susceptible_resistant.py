import os

with open('feature_eng_functions.py') as f:
    exec(f.read())

antibiotics = ['AMP', 'AUG', 'AXO', 'CHL', 'FIS', 'FOX', 'GEN', 'KAN', 'STR', 'TET', 'TIO']
profile = ['Susceptible', 'Resistant']

root = '/mnt/e/User/bruna.fistarol/HMM/Salmonella/Antibiotics'
#path_multifasta = '/mnt/e/User/bruna.fistarol/HMM/Salmonella/Pfam_multifasta'

for a in antibiotics:
    #for p in profile:

    #datadir = os.path.join(root, a, p, 'Strains')

    susceptible_directory = os.path.join(root, a, 'Susceptible')

    resistant_directory = os.path.join(root, a, 'Resistant')

    get_multifasta(datadir, output_directory)

    multiple_alignment(input_directory + '/Pfam_multifasta', output_directory)

    run_hmmbuild(input_directory + '/Pfam_ma', output_directory, 28)

    search_hmm(susceptible_directory, resistant_directory, 28)
    search_hmm(resistant_directory, susceptible_directory, 28)