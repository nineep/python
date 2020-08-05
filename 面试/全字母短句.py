import string
letters = string.ascii_lowercase

def get_missing_letter(a):
    s1 = set(letters)
    s2 = set(a.lower())
    ret = ''.join(sorted(s1-s2))
    return ret

print(get_missing_letter('python'))