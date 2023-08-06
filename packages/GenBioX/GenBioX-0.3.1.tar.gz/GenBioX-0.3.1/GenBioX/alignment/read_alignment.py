import subprocess
import os

def read_alignment(reads, reference_genome):
    # Check that input files exist
    if not os.path.isfile(reads):
        raise ValueError(f"Reads file {reads} does not exist.")
    if not os.path.isfile(reference_genome):
        raise ValueError(f"Reference genome file {reference_genome} does not exist.")

    # Define Bowtie2 command with specified options
    bowtie2_command = f"bowtie2 -x {reference_genome} -U {reads} --quiet --no-hd --no-sq -k 1 --no-unal --score-min L,0,-0.6 -p 4"
    
    # Run Bowtie2 command and capture stdout
    process = subprocess.Popen(bowtie2_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    
    # Parse Bowtie2 output and extract relevant information
    alignment_data = stdout.decode().split('\t')
    if len(alignment_data) < 5:
        raise ValueError("Bowtie2 output does not contain enough fields. Please check that the input files and options are correct.")
    
    chromosome = alignment_data[2]
    position = int(alignment_data[3])
    alignment_quality = int(alignment_data[4])
    
    return (chromosome, position, alignment_quality)
