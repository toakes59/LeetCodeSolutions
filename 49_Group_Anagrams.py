# Group_Anagrams
from collections import defaultdict

# Define a function named 'groupAnagrams' that takes a list of strings 'strs' as input
# and returns a list of lists of strings, grouping anagrams together.
def groupAnagrams(strs):
    # Create a defaultdict 'anagram_groups' to store lists of anagrams based on their sorted forms.
    anagram_groups = defaultdict(list)

    # Iterate through each word in the input list 'strs'.
    for word in strs:
        # Sort the characters in the word to identify anagrams.
        sorted_word = ''.join(sorted(word))
        
        # Append the original word to the list associated with its sorted form in 'anagram_groups'.
        anagram_groups[sorted_word].append(word)

    # Return a list containing the values (lists of anagrams) from the 'anagram_groups' dictionary.
    return list(anagram_groups.values())


# Example usage:
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = groupAnagrams(strs)
print(result)


strs = ["abc", "cde", "acb", "bac", "dec", "qew"]
1. sort all words so they become duplicates if they are anagrams
sorted_word = ''.join(sorted(word))
2. Append the original word to the list associated with its sorted form in 'anagram_groups'.
anagram_groups[sorted_word].append(word)
3. Return a list containing the values (lists of anagrams) from the 'anagram_groups' dictionary.

["abc", "cde", "acb", "bac", "dec", "qew"]

sorted word = "abc"
anagram_groups["abc"] = ["abc"]

sorted word = "cde"
anagram_groups["cde"] = ["cde"]

sorted word = "acb" -> "abc"
anagram_groups["abc"] = ["abc", "acb"]

sorted word = "bac" -> "abc"
anagram_groups["abc"] = ["abc", "acb", "bac"]

sorted word = "dec" -> "cde"
anagram_groups["cde"] = ["cde", "dec"]

sorted word = "qew" -> "eqw"
anagram_groups["eqw"] = ["qew"]

anagram_groups = [["abc", ["abc", "acb", "bac"]], ["cde", ["cde", "dec"]], ["eqw", ["qew"]]


