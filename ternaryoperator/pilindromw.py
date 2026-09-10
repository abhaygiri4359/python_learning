#program accepting word or value and decide weather aword or value is palindrome
value=input("Enter the value:").lower()
res="pallindrome"if value==value[::-1] else "not palindrome"
print(res)