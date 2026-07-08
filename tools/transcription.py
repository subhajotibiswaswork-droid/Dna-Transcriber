"""Function to transcribe DNA to RNA"""
def transcribe(dna_sequence: str) -> str:
    """Transcribes a DNA sequence into an RNA sequence."""
    return dna_sequence.replace('T', 'U')