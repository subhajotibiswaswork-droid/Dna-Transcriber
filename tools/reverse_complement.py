#Function to get the reverse complement of a DNA sequence
def reverse_complement(dna_sequence: str) -> str:
    """Returns the reverse complement of a DNA sequence."""
    complement = {'A': 'T',
                  'T': 'A', 
                  'C': 'G', 
                  'G': 'C'}
    return ''.join(complement[base] for base in reversed(dna_sequence))