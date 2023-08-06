#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 17:06:45 2023

@author: li
"""

import os
import sys
sys.path.append("/path/to/Users/li/Desktop/ResistomeX")

from fasta import read_fasta
from fasta_quality_check import fasta_quality_check


# Load the test FASTA file
sequences = read_fasta("test.fasta.txt")

# Apply quality control check
sequences = fasta_quality_check(sequences)

# Print the sequences
for seq_id, seq in sequences.items():
    print(seq_id, seq)
