import pysam
import subprocess

def splice_site_prediction(input_vcf, output_vcf, reference_genome):
    # Define SpliceAI command with specified options
    spliceai_command = f"spliceai -I {input_vcf} -O {output_vcf} -R {reference_genome}"
    
    # Run SpliceAI command
    subprocess.run(spliceai_command, shell=True, check=True)
    
    # Load SpliceAI output into Python dataframe
    vcf = pysam.VariantFile(output_vcf)
    for record in vcf:
        # Parse SpliceAI INFO field to extract splice site predictions
        spliceai_predictions = record.info['SpliceAI']
        spliceai_predictions = [x.split('|') for x in spliceai_predictions.split(',')]
        
        # Add splice site predictions to record INFO field
        record.info['SpliceAI_acceptor_predictions'] = [float(x[1]) for x in spliceai_predictions]
        record.info['SpliceAI_donor_predictions'] = [float(x[2]) for x in spliceai_predictions]
        
        # Update record in VCF file
        vcf.write(record)
    
    # Close VCF file
    vcf.close()
