import subprocess

import pandas as pd

def variant_effect_prediction(input_vcf, output_vcf, reference_genome):
    # Define SnpEff command with specified options
    snpeff_command = f"java -Xmx4g -jar snpEff.jar {reference_genome} {input_vcf} -o vcf -no-downstream -no-intergenic -no-upstream -no-utr -noStats -forceOverwrite > {output_vcf}"
    
    # Run SnpEff command
    subprocess.run(snpeff_command, shell=True, check=True)
    
    # Load SnpEff output into Python dataframe
    effect_df = pd.read_csv(output_vcf, delimiter='\t', header=0, comment='#', low_memory=False)
    
    return effect_df
