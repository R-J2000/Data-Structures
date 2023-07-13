#### Suffix Array 

What is a Suffix? A non-empty substring at the end of a string of characters. The three possible suffixes of the string "cat" are "t", "at", "cat".

A suffix array contains are the sorted suffixes of a string. The sorting is done lexographic order. The suffix array also notes down the index at which a suffix began. The *actual* "suffix array" is the array of the sort indices. 

Let's consider an example to understand the concept of a suffix array. Suppose we have the string "banana". The suffixes of this string are as follows:

Suffixes: ("banana", "anana", "nana", "ana", "na", "a")

To construct the suffix array, we sort these suffixes lexicographically, resulting in the following:

Suffix Array: (a, ana, anana, banana, na, nana) which corresponds to (5, 3, 1, 0, 4, 2)

Each element in the suffix array represents the starting index of a suffix in the original string. For example, the first element "a" corresponds to the suffix starting at index 6, and the last element "nana" corresponds to the suffix starting at index 2. Sorting the indicies of the suffixes, instead of the suffix itself, allows us to compress the information needed to be stored.

**Longest Common Prefix Array**

The LCP (Longest Common Prefix) array is an auxiliary array associated with a suffix array. It stores the lengths of the longest common prefixes between adjacent suffixes in a sorted order. The LCP array provides valuable information about the similarity between suffixes, which is useful in various string algorithms.

Let's consider an example to understand the concept of the LCP array. Suppose we have the string "banana" and its corresponding suffix array and LCP array as follows:

String: "banana"
Suffix Array: (a, ana, anana, banana, na, nana)
LCP Array: (0, 1, 3, 0, 0, 2)

Each element in the LCP array represents the length of the longest common prefix between the corresponding pair of adjacent suffixes in the suffix array. For example, the LCP value at index 2 is 3, indicating that the suffixes "anana" and "ana" have a common prefix of length 3 ("ana").

Here's a breakdown of the LCP array for the given example:

The LCP value at index 0 is 0 because the first suffix "a" has no common prefix with the previous suffix.
The LCP value at index 1 is 1 because the second suffix "ana" shares a common prefix of length 1 ("a") with the previous suffix "a".
The LCP value at index 2 is 3 because the third suffix "anana" shares a common prefix of length 3 ("ana") with the previous suffix "ana".
The LCP value at index 3 is 0 because the fourth suffix "banana" does not have any common prefix with the previous suffix "anana".
The LCP values at indices 4 and 5 are both 0 because the last two suffixes "na" and "nana" have no common prefix with their respective previous suffixes.
