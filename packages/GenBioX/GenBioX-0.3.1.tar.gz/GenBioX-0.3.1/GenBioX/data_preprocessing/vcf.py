import allel
import pandas as pd


def read_vcf(vcf_path):
    # Load the VCF file
    callset = allel.read_vcf(vcf_path)

    # Create a DataFrame with the variant data
    df = pd.DataFrame({
        'CHROM': callset['variants/CHROM'],
        'POS': callset['variants/POS'],
        'REF': callset['variants/REF'],
        'ALT': callset['variants/ALT'][:, 0],
        'DP': callset['variants/DP'],
        'QUAL': callset['variants/QUAL'],
    })

    return df
