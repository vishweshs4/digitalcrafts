def isPalindrome(string):
    value = True
    for i in range(0, int(len(string)/2)):
        if string[i] != string[len(string)-1-i]:
            value = False
    return value

print("I check for palindromes!")
# string = raw_input("Type in a string: ")

if isPalindrome(raw_input("Type in a string: ").lower()):
    print("That's a palindrome!")
else:
    print("That's not a palindrome!")
