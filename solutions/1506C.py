from difflib import SequenceMatcher
for _ in range(int(input())):
    a = input()
    b = input()
    aa=len(a)
    bb=len(b)
    match = SequenceMatcher(None, a, b).find_longest_match(0, aa, 0, bb)
    print(aa+bb-(2*match.size))