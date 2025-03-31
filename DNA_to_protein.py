def dna_translate():
    codon_map = {
        "TTT": "Phe", "TTC": "Phe",
    "TTA": "Leu", "TTG": "Leu",
    "CTT": "Leu", "CTC": "Leu", "CTA": "Leu", "CTG": "Leu",
    "TCT": "Ser", "TCC": "Ser", "TCA": "Ser", "TCG": "Ser",
    "AGT": "Ser", "AGC": "Ser",
    "TAT": "Tyr", "TAC": "Tyr",
    "TGT": "Cys", "TGC": "Cys",
    "TGG": "Trp",
    "CCT": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
    "CAT": "His", "CAC": "His",
    "CAA": "Gln", "CAG": "Gln",
    "CGT": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg", "AGA": "Arg", "AGG": "Arg",
    "ATT": "Ile", "ATC": "Ile", "ATA": "Ile",
    "ATG": "Met",
    "ACT": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
    "AAT": "Asn", "AAC": "Asn",
    "AAA": "Lys", "AAG": "Lys",
    "GTT": "Val", "GTC": "Val", "GTA": "Val", "GTG": "Val",
    "GCT": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
    "GAT": "Asp", "GAC": "Asp",
    "GAA": "Glu", "GAG": "Glu",
    "GGT": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly",
    "TAA": "Stop", "TAG": "Stop", "TGA": "Stop"

    }
    dna_sequence = str(input("What's your DNA sequence?"))
    protein = []
    for i in range(0, len(dna_sequence)-2, 3):
        codon = dna_sequence[i:i+3].upper()
        amino_acid = codon_map.get(codon, '?')

        if amino_acid == 'Stop':
            break
        protein.append(amino_acid)
    print(f"Your proteins are {protein}")


dna_translate()


