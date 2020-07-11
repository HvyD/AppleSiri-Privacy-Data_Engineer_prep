from collections import Counter

def min_window(S, T):
    result_char, missing_char = Counter(T), len(T)
    i = p = q = 0
    for j, c in enumerate(S, 1):
        missing_char -= result_char[c] > 0
        result_char[c] -= 1
        if not missing_char:
            while i < q and result_char[S[i]] < 0:
                result_char[S[i]] += 1
                i += 1
            if not q or j - i <= q - p:
                p, q = i, j
    return S[p:q]



S = "ADOBECODEBANC"
T = "ABC"
print(min_window(S,T)) #=> "BANC"
