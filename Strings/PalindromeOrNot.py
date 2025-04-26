def Palindrome(word):
        word2 = word[::-1]  #It will reverse the string i.e [::-1]
        if word2==word:
            print ("Palindrome")
        else:
            print ("Not a Palindrome")

#Example Usage
word = input("Enter any word: ")
result = Palindrome(word)