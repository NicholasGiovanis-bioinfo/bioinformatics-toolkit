allowed_chars = "ATCG"

sequence1 = input("Enter a valid sequence: ").upper()
sequence2 = input("Enter another valid sequence: ").upper()


def valid_sequence(seq1, seq2):
    try:
        if len(seq1) == 0 or len(seq2) == 0:
            raise ValueError("Sequences cannot be empty")

        if len(seq1) != len(seq2):
            raise ValueError("Sequences must be the same length")

        for char in seq1 + seq2:
            if char not in allowed_chars:
                raise ValueError(f"Invalid character: {char}")

    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        return False

    return True


if valid_sequence(sequence1, sequence2):

    # Mutation detection
    for i in range(len(sequence1)):
        if sequence1[i] != sequence2[i]:
            print(f"Mutation at position {i}: {sequence1[i]} → {sequence2[i]}")

    # Base comparison
    for base in "ATCG":
        count1 = sequence1.count(base)
        count2 = sequence2.count(base)

        print(f"{base} in seq1:", count1)
        print(f"{base} in seq2:", count2)

        if count1 != count2:
            print(f"Number of {base} bases unequal")
        else:
            print(f"Number of {base} bases equal")