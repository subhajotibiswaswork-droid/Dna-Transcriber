"""Validation functions for DNA sequences."""

VALID_BASES = {"A", "T", "G", "C"}
"""Set of valid DNA bases."""

def is_valid_dna(sequence: str) -> bool:
    """Checks if a DNA sequence is valid."""
    for base in sequence:
        if base not in VALID_BASES:
            return False
    return True