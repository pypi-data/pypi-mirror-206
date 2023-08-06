import subprocess

import pandas as pd

def variant_annotation(input_vcf, output_annovar_prefix, database):
    # Define ANNOVAR command with specified options
    annovar_command = f"table_annovar.pl {input_vcf} {database} -buildver hg19 -out {output_annovar_prefix} -remove -protocol refGene,exac03,avsnp147 -operation g,f,f -nastring . -vcfinput"
    
    # Run ANNOVAR command
    subprocess.run(annovar_command, shell=True, check=True)
    
    # Load ANNOVAR output into Python dataframe
    annovar_output = f"{output_annovar_prefix}.{database}_multianno.txt"
    annotations_df = pd.read_csv(annovar_output, delimiter='\t', header=0)
    
    return annotations_df
