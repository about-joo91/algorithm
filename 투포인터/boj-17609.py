def is_palindrome(word, left, right):
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

def palindrome_type_of_str(word, left, right):
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            if is_palindrome(word, left+1, right) or is_palindrome(word, left, right-1):
                return 1
            return 2
    return 0
T = int(input())
for _ in range(T):
    word = input()
    print(palindrome_type_of_str(word, 0, len(word)-1))
