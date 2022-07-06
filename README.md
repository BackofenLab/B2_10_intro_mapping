<img src="./figures/banner.png" alt="UniFreiburg Banner"/>

Lehrstuhl für Bioinformatik - Institut für Informatik - *http://www.bioinf.uni-freiburg.de*

---
## Bioinformatics 2
###### SS 2021/2022
##### Exercise sheet 10: Introduction to mapping
---

### _Exercise 4 - Programming Assignment_
In this exersice you will implement Burrows-Wheeler Transform (BWT) and its inverse.

**a)** In order to start building the Burrows-Wheeler matrix you need to implement a helper function which return all the rotations of the given string.
Implement the function `rotations` which takes a string and returns a list of all its rotations.

<details>
  <summary>Example: (Spoiler)</summary>

  ```
   >>> all_rotations = rotations("abaaba$")
   >>> print(all_rotations)
   ['abaaba$', 'baaba$a', 'aaba$ab', 'aba$aba', 'ba$abaa', 'a$abaab', '$abaaba']
  ```
</details>

**b)** Build the Burrows-Wheeler matrix. Implement the function `bwm` which takes a string and returns the Burrows-Wheeler matrix.
The matrix should be a list of string rotations sorted alphabetically.

<details>
  <summary>Example: (Spoiler)</summary>

  ```
   >>> matrix = bwm("abaaba$")
   >>> print(matrix)
   ['$abaaba', 'a$abaab', 'aaba$ab', 'aba$aba', 'abaaba$', 'ba$abaa', 'baaba$a']
  ```
</details>

**с)** Implement the transformation with the Burrows-Wheeler matrix.
Implement the function `bwt_with_bwm` which takes a string and returns the Burrows-Wheeler transform as a string.

<details>
  <summary>Example: (Spoiler)</summary>

  ```
   >>> t = bwt_with_bwm("abaaba$")
   >>> print(t)
   abba$aa
  ```
</details>


**d)** Check your understandings of the Burrows-Wheeler transform.
Implement the function `transformation_to_first_colum` which takes the BW transform string t (the last column of the BW matrix) and returns the string which correspond to the first column of the matrix.
Note that you do not need to build the Burrows-Wheeler matrix to do this.

<details>
  <summary>Example: (Spoiler)</summary>

  ```
   >>> f = transformation_to_first_colum("abba$aa")
   >>> print(f)
   $aaaabb
  ```
</details>


**e)** Implement a helper function `transformation_to_dict_occurrences`.
This function takes the string transformation (t) and returns the dictionary with the number of occurrences of each character in the transformation.

<details>
  <summary>Example: (Spoiler)</summary>

  ```
   >>> occurrences = transformation_to_dict_occurrences("abba$aa")
   >>> print(occurrences)
   {'a': 4, 'b': 2, '$': 1}
  ```
</details>


**f)** Implement a helper function `transformation_b_ranking`. This function takes the string transformation (t) and returns the B-ranking of the characters in the transformation as a list.
<details>
  <summary>Example: (Spoiler)</summary>

  ```
   >>> ranks = transformation_b_ranking("abba$aa")
   >>> print(ranks)
   >>> print(occurrences)
   [0, 0, 1, 1, 0, 2, 3]
   {'a': 4, 'b': 2, '$': 1}
  ```
</details>

**g)** Implement the helper function `bwm_first_column_interval_form_from_transform`. This function takes the string transformation (t) and returns
    the first column of the BW matrix in the interval form
    i.e. the dictionary where the keys are the characters
    and the values are tuples (start, end) of the character occurrences. 

<details>
  <summary>Example: (Spoiler)</summary>

  ```
   >>> f_column_intervals = bwm_first_column_interval_form_from_transform("abba$aa")
   >>> print(f_column_intervals)
   {'$': (0, 1), 'a': (1, 5), 'b': (5, 7)}
  ```

</details>

**g)** Implement the function `reverse_bwt`.
This function takes the BW transformation string (t) and returns the original string.


<details>
  <summary>Example: (Spoiler)</summary>

  ```
   >>> s = reverse_bwt("abba$aa")
   >>> print(s)
   abaaba$
  ```

</details>