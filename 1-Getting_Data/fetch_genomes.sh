#!/bin/bash

# Read genome_ids.txt line by line
while read -r genome_id; do
  # Skip empty lines
  if [ -z "$genome_id" ]; then
    continue
  fi

  output_directory="/mnt/e/User/bruna.fistarol/HMM/Salmonella/Strains/"

  # Create a TSV file for each genome
  output_file="${output_directory}feature_data_${genome_id}.tsv"

  # Fetch feature data for the specific genome
  p3-echo -t genome_id "$genome_id" | p3-get-genome-features --eq feature_type,CDS --attr patric_id --attr genome_id --attr feature_id --attr refseq_locus_tag  --attr plfam_id --attr na_sequence> "$output_file"

  echo "Saved feature data for genome $genome_id to $output_file"

done < "genome_ids.txt"