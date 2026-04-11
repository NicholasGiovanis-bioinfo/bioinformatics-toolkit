sequence = input("Enter a valid DNA string:").upper()
allowed_chars = "ATCG"

def correct_data(seq):
    try:
        if len(seq) == 0:
            raise ValueError("Sequence cannot be an empty string")

        for char in seq:
            if char not in allowed_chars:
                raise ValueError("Character {} not in allowed characters {}".format(char, allowed_chars))

    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        return False

    return True

if correct_data(sequence):

    A = sequence.count("A")
    T = sequence.count("T")
    G = sequence.count("G")
    C = sequence.count("C")

    GC = G + C
    GC_percentage = (GC / len(sequence)) * 100

    print("Length of sequence:", len(sequence))
    print("GC Content:", round(GC_percentage, 2), "%")
    print("A:", A)
    print("T:", T)
    print("G:", G)
    print("C:", C)

    if "ATG" in sequence:
        print("Start codon (Methionine) detected")