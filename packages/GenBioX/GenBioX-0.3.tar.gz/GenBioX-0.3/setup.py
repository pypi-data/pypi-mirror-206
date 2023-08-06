from setuptools import setup, find_packages

setup(
    name='GenBioX',
    version='0.3',
    packages=find_packages(),
    license='MIT',
    description='A Comprehensive Bioinformatics Package for Genome Analysis',
    long_description='''For documentation, please visit http://genbiox.readthedocs.io/''',
    keywords=['bioinformatics', 'genomics', 'genome analysis', 'quality control', 'preprocessing',  'sequencing', 'annotation','variant analysis', 'gene expression', 'comparative genomics'],
    install_requires=[
        'pandas>=1.3.0',
        'numpy>=1.21.1',
        'Biopython>=1.79',
        'scikit-allel>=1.3.2'
    ],
    url='https://github.com/SayaGarud/GenBioX.git',
    author='Sayali Garud',
    author_email='sayaligrud@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],
)
