DNA_sequence = input("Enter DNA sequence:").upper()
allowed_chars = "ATCG"
codon_table = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine", "UUC": "Phenylalanine",
    "UUA": "Leucine", "UUG": "Leucine",
    "UCU": "Serine", "UCC": "Serine",
    "UAU": "Tyrosine", "UAC": "Tyrosine",
    "UGG": "Tryptophan"
}

amino_acids = []
stop_codons = ["UAA", "UAG", "UGA"]

def is_correct(seq):
    try:
        if len(seq) == 0:
            raise ValueError("Sequence must not be empty")
        if len(seq) < 3:
            raise ValueError("Sequence must contain at least 3 bases")
        if  len(seq)%3 != 0:
            raise ValueError("DNA string must have number of bases dividable by 3")
        for character in seq:
            if character not in allowed_chars:
                raise ValueError("Please enter a valid DNA sequence:")
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        return False
    return True

if is_correct(DNA_sequence):

    mRNA_sequence = DNA_sequence.replace("T", "U")
    print("mRNA sequence:", mRNA_sequence)

    amino_acids = []

    for i in range(0, len(mRNA_sequence), 3):
        codon = mRNA_sequence[i:i+3]

        if codon in stop_codons:
            print("Stop codon:", codon, "detected")
            break
        amino_acid = codon_table.get(codon, "Unknown")
        amino_acids.append(amino_acid)

    print("Translated amino acids:")
    print(amino_acids)
