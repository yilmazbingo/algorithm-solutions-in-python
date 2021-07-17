"""
Given a string, that contains special character together with alphabets (‘a’ to ‘z’ and ‘A’ to ‘Z’),
reverse the string in a way that special characters are not affected.
"""


def reverse_only_alpha(S: str)->str:
    list_of_S = list(S)
    i = 0
    j = len(S) - 1
    while i < j:
        if not list_of_S[i].isalpha():
            i += 1
        elif not list_of_S[j].isalpha():
            j -= 1
        else:
            list_of_S[i], list_of_S[j] = list_of_S[j], list_of_S[i]
            i += 1
            j -= 1
    new_S = "".join(list_of_S)
    return new_S


reverse_only_alpha("ad,W!@,ddsdnsad")
