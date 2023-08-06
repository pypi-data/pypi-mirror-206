import subprocess

def variant_calling(input_bam, reference_genome, output_vcf):
    # Define GATK command with specified options
    gatk_command = f"gatk --java-options '-Xmx4g' HaplotypeCaller -R {reference_genome} -I {input_bam} -O {output_vcf} -ERC GVCF --minimum-mapping-quality 20 --minimum-base-quality 20 --emit-ref-confidence GVCF -ploidy 2"
    
    # Run GATK command
    subprocess.run(gatk_command, shell=True, check=True)
