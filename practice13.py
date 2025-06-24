def is_palindrome(text: str) -> bool:
    if text == text[::-1] :
        text = "matn palindrom"
    else:
        text = "matn palindrom emas"
    return text

words = input("sozni kiriting: ")
print(is_palindrome(words))