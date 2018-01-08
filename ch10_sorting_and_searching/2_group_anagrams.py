from collections import defaultdict

def group_anagrams(strings):
    anagrams = defaultdict(list)

    for string in strings:
        s_anagram = "".join(sorted(string)).replace(" ", "")
        anagrams[s_anagram].append(string)

    all_anagrams = []
    for anagram_strings in anagrams.values():
        all_anagrams += anagram_strings

    return all_anagrams


strings = ["ma n", "  tree", "ret e", "nam"]
print(group_anagrams(strings))
