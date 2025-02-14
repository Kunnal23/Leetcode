def longestCommonPrefix(strs):
    pref=strs[0]
    for i in range(len(pref)):
        for word in strs[1:]:
            if i == len(word) or pref[i] != word[i]:
                return pref[:i]
    return pref

print(longestCommonPrefix(strs = ["flower","flow","flight"]))