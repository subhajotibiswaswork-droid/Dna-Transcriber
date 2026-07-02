def transcribe(dna_sequence):
    return dna_sequence.replace('T', 'U').replace('t', 'u')
dna = input("Enter a DNA sequence: ")
rna = transcribe(dna_sequence=dna)
print("RNA sequence:", rna)