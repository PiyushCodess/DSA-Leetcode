from collections import defaultdict

def groupAnagrams(strs):
    anagrams = defaultdict(list)
    
    for word in strs:
        key = ''.join(sorted(word))
        anagrams[key].append(word)
    
    return list(anagrams.values())


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

