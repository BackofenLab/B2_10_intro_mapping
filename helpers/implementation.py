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


def transformation_ranking_occurrences_correct(t):
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
    return ranks, dict_occurrences


def bwm_first_column_interval_form_from_transform(t):
    """
    This function takes the string transformation (t) and returns
    the first column of the BW matrix in the interval form.
    I.E. the dictionary where the keys are the characters
    and the values are tuples (start, end) of the character occurrences.
    """
    f_colum_cumulative = {}
    c_sum = 0
    _, dict_occurrences = transformation_ranking_occurrences_correct(t)
    for c, o in sorted(dict_occurrences.items()):
        f_colum_cumulative[c] = c_sum, c_sum + o
        c_sum += o
    return f_colum_cumulative


def reverse_bwt_correct(t):
    """
    This function takes the BW transformation string (t) and returns the original string.
    """
    ranks, occurrences = transformation_ranking_occurrences_correct(t)
    first_column_intervals = bwm_first_column_interval_form_from_transform(t)
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
    for r in bwm:
        print(r)

    print("\n_________________3_______________________")
    transform = bwt_with_bwm_correct(string)
    print(transform)

    print("\n________________4_______________________")
    print(transformation_to_first_colum_correct(transform))

    print("\n_________________5_______________________")
    print(transformation_ranking_occurrences_correct(bwt_with_bwm_correct(string)))

    print("\n_________________6_______________________")
    print(reverse_bwt_correct(transform))


if __name__ == "__main__":
    main()