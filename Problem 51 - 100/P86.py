# Write a function to check palindrome.							

def Palindrome(Sequence):
    Sequence_R = ''.join(reversed(Sequence))
    if Sequence == Sequence_R:
        print("Given Word is Palindrom !!")
    else:
        print("Print Given Word is not palindrome !!!!!!!!!!!!!!")

Palindrome("RAR")
