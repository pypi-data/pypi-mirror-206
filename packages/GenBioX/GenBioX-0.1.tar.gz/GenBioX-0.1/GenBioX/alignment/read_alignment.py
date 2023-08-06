import subprocess

def read_alignment(reads, reference_genome):
    # Define Bowtie2 command with specified options
    bowtie2_command = f"bowtie2 -x {reference_genome} -U {reads} --quiet --no-hd --no-sq -k 1 --no-unal --score-min L,0,-0.6 -p 4"
    
    # Run Bowtie2 command and capture stdout
    process = subprocess.Popen(bowtie2_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    
    # Parse Bowtie2 output and extract relevant information
    alignment_data = stdout.decode().split('\t')
    chromosome = alignment_data[2]
    position = int(alignment_data[3])
    alignment_quality = int(alignment_data[4])
    
    return (chromosome, position, alignment_quality)
