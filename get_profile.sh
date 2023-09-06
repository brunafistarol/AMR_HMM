#!/bin/bash

# Read genome_ids.txt line by line
while read -r genome_id; do
  # Skip empty lines
  if [ -z "$genome_id" ]; then
    continue
  fi

  output_directory="/mnt/e/User/bruna.fistarol/HMM/Salmonella/Profile/"

  # Create a TSV file for each genome
  output_file="${output_directory}resistance_${genome_id}.tsv"

  # get resistance for the specific genome
  p3-echo -t genome_id "$genome_id" | p3-get-genome-drugs --resistant --attr antibiotic > "$output_file"

  echo "Saved resistance for genome $genome_id to $output_file"

done < "genome_ids.txt"

# Read genome_ids.txt line by line
while read -r genome_id; do
  # Skip empty lines
  if [ -z "$genome_id" ]; then
    continue
  fi

 output_directory="/mnt/e/User/bruna.fistarol/HMM/Salmonella/Profile/"

  # Create a TSV file for each genome
  output_file="${output_directory}susceptibility_${genome_id}.tsv"

  # get susceptibility data for the specific genome
  p3-echo -t genome_id "$genome_id" | p3-get-genome-drugs --susceptible --attr antibiotic > "$output_file"

  echo "Saved susceptibility for genome $genome_id to $output_file"

done < "genome_ids.txt"