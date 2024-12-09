def first_non_repeating_char_bruteforce(s):
    for i in range(len(s)):
        found_duplicate = False
        for j in range(len(s)):
            # print(f"Cheking: {s[i]}=={s[j]}")
            if s[i] == s[j] and i != j:
                found_duplicate = True
                break
        if not found_duplicate:
            return s[i]
    return ""


def _search_duplicate(s, i):
    for j in range(len(s)):
        # print(f"Cheking: {s[i]}=={s[j]}")
        if s[i] == s[j] and i != j:
            return True
    return False


def first_non_repeating_char_bruteforce_split(s):
    for i in range(len(s)):
        if not _search_duplicate(s, i):
            return s[i]
    return ""


def first_non_repeating_char_hashmap(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    for char in s:
        if freq[char] == 1:
            return char
    return None
