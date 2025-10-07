"""https://leetcode.com/problems/valid-palindrome/"""
# def valid_palindrome(s: str):
#     if not len(s):
#         return True

#     ALPHABET_AND_NUMBERS = "abcdefghijklmnopqrstuvwxyz0123456789"

#     left_idx = 0
#     right_idx = len(s) - 1

#     while left_idx < len(s) and right_idx >= 0:
#         while s[left_idx].lower() not in ALPHABET_AND_NUMBERS:
#             if left_idx + 1 < len(s):
#                 left_idx += 1
#             else:
#                 return True

#         while s[right_idx].lower() not in ALPHABET_AND_NUMBERS:
#             if right_idx - 1 > 0:
#                 right_idx -= 1
#             else:
#                 return True

#         if s[left_idx].lower() != s[right_idx].lower():
#             return False

#         left_idx += 1
#         right_idx -= 1
#     return True


# def valid_palindrome(s: str):
#     if not len(s):
#         return True

#     left_idx, right_idx = 0, len(s) - 1

#     while left_idx < right_idx:
#         while not s[left_idx].isalnum():
#             if left_idx + 1 < len(s):
#                 left_idx += 1
#             else:
#                 return True

#         while not s[right_idx].isalnum():
#             if right_idx - 1 > 0:
#                 right_idx -= 1
#             else:
#                 return True

#         if s[left_idx].lower() != s[right_idx].lower():
#             return False

#         left_idx += 1
#         right_idx -= 1
#     return True


def valid_palindrome(s: str):
    if not len(s):
        return True

    left_idx, right_idx = 0, len(s) - 1

    while left_idx < right_idx:
        while left_idx < right_idx and not s[left_idx].isalnum():
            left_idx += 1
        while right_idx > left_idx and not s[right_idx].isalnum():
            right_idx -= 1

        if s[left_idx].lower() != s[right_idx].lower():
            return False

        left_idx += 1
        right_idx -= 1
    return True


def is_alpha_num(char: str) -> bool:
    return (
        ord("A") <= ord(char) <= ord("Z")
        or ord("a") <= ord(char) <= ord("z")
        or ord("0") <= ord(char) <= ord("9")
    )


# def valid_palindrome(s: str):
#     newS = ""
#     for c in s:
#         if c.isalnum():
#             newS += c.lower()
#     return newS == newS[::-1]
