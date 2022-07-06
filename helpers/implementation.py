def rotations_correct(s):
    """
    This function takes a string and returns a list of all possible rotations of the string.
    """
    rotations = [s[i:] + s[:i]for i in range(len(s))]
    return rotations


def bwm_correct(s):
    """
    This function takes a string and returns a list of all possible rotations
    of the string in the lexicographical order. In other words it returns rows of the Burrows-Wheeler matrix.
    """
    return sorted(rotations_correct(s))


def bwt_with_bwm_correct(s):
    """
    This function applies the Burrows-Wheeler transform to a string by using BW matrix.
    """
    return "".join([r[-1] for r in bwm_correct(s)])


def transformation_to_first_colum_correct(t):
    """
    This function takes the string transformation (t) and returns the first column of the BW matrix as a string.
    """
    return "".join(sorted(t))


def transformation_to_dict_occurrences_correct(t):
    """
    This function takes the string transformation (t) and returns the ranking of the transformation.
    """
    dict_occurrences = {}
    for c in t:
        if c not in dict_occurrences:
            dict_occurrences[c] = 0

        dict_occurrences[c] += 1
    return dict_occurrences


def transformation_b_ranking_correct(t):
    """
        This function takes the string transformation (t) and returns the ranking of the transformation.
        """
    dict_occurrences = {}
    ranks = []
    for c in t:
        if c not in dict_occurrences:
            dict_occurrences[c] = 0
        ranks.append(dict_occurrences[c])
        dict_occurrences[c] += 1
    return ranks


def bwm_first_column_interval_form_from_transform_correct(t):
    """
    This function takes the string transformation (t) and returns
    the first column of the BW matrix in the interval form.
    I.E. the dictionary where the keys are the characters
    and the values are tuples (start, end) of the character occurrences.
    """
    f_colum_cumulative = {}
    c_sum = 0
    dict_occurrences = transformation_to_dict_occurrences_correct(t)
    for c, o in sorted(dict_occurrences.items()):
        f_colum_cumulative[c] = c_sum, c_sum + o
        c_sum += o
    return f_colum_cumulative


def reverse_bwt_correct(t):
    """
    This function takes the BW transformation string (t) and returns the original string.
    """
    occurrences = transformation_to_dict_occurrences_correct(t)
    ranks = transformation_b_ranking_correct(t)
    first_column_intervals = bwm_first_column_interval_form_from_transform_correct(t)
    row_index = 0
    s = "$"
    while t[row_index] != "$":
        s += t[row_index]
        row_index = first_column_intervals[t[row_index]][0] + ranks[row_index]
    return s[::-1]


def main():
    print("\n_________________1______________________")
    string = "abaaba$"
    all_rotations = rotations_correct(string)
    print(all_rotations)

    print("\n_________________2_______________________")
    bwm = bwm_correct(string)
    print(bwm)
    for r in bwm:
        print(r)

    print("\n_________________3_______________________")
    string_long = 'The word squirrel, first attested in 1327, comes from the Anglo-Norman esquirel which is from the Old French escurel, the reflex of a Latin word sciurus, which was taken from the Ancient Greek word σκίουρος (skiouros; from σκία-ουρος) shadow-tailed, referring to the long bushy tail which many of its members have.The native Old English word for the squirrel, ācweorna, survived only into Middle English (as aquerne) before being replaced.[4] The Old English word is of Common Germanic origin, cognates of which are still used in other Germanic languages, including the German Eichhörnchen (diminutive of Eichhorn, which is not as frequently used), the Norwegian ikorn/ekorn, the Dutch eekhoorn, the Swedish ekorre and the Danish egern. A group of squirrels is called a "dray"[5] or a "scurry".[6] '
    string_dna = "cctgaatcaagggccaactcatcaagcgggttaacttagaaacagccatgatcagtgaggtcatttacgccctaacccaacggccgcatttccgttcccaacaggaaccaattgacgggtgtactcctctagtatccgagccacttaccccgagacctcacgcgcacgcacgtgatacgagttgcttctatcgaacccattatgaaacaaggactgccttctcagctgtatagtgttctacttagtgagtactcccccttcggtttttatctctcagagccggcatctatgcccccttttgccgtagtacaaattaggaccagcgtgtagctaaagacgtacctgagcaactttgggcgaccttgtggttacgtatgtatagaggcaatttcaagcgtaaacagtgtgcacttctccttcctgttttgaacgctcttcaccgatggaggagggtctttctcaccagcccgtgcacagaccacattgggatacaggagagattaacgcaacgatactggaccgtcgacttccaggtctagttgtttccgggatcctcaaggtctgctaccaagatatcaaccttttaacagcgcacctcggattctagcctgatacaatgaacgccctcctgacccgttcaagtgctaaggcgagttaactcacggctggcacgttaggtggagatagtaatccgtctattagctcctcgtaagaccgcacgattcgggctgaaagatcttatgtaatgtggcggacacagggatactgatcctcgcgcttgtatacgaaatcgacctgcacgagtaacgttggtaaagttaacacttgcttaagacgtccagtgcccgggcgaattaccccaattaaaggacgtgagactcggaagtacgagctggcgatggagtggaaaaagcgacggatatgttgataccgttgcccagaagacatactgcttgggcccactccacgctgcacgttgtagctgttcacagagggaccc"

    transform = bwt_with_bwm_correct(string)
    transform_long = bwt_with_bwm_correct(string_long)
    transform_dna = bwt_with_bwm_correct(string_dna)
    print(transform)
    print(transform_long)
    print(transform_dna)

    print("\n________________4_______________________")
    print(transformation_to_first_colum_correct(transform))

    print("\n_________________5_______________________")
    print(transformation_to_dict_occurrences_correct(bwt_with_bwm_correct(string)))

    print("\n_________________6_______________________")
    print(bwm_first_column_interval_form_from_transform_correct(transform))

    print("\n_________________7_______________________")
    print(reverse_bwt_correct(transform))


if __name__ == "__main__":
    main()