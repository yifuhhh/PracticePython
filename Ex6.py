def main():
    word = input("Input a string: ")
    l = len(word)
    m = 0
    if l % 2 == 0:
        i = 0
        while i < l / 2:
            if word[i] == word[l-i-1]:
                i = i + 1
            else:
                m = 1
                break
    else:
        i = 0
        while i < (l + 1) / 2:
            if word[i] == word[l-i-1]:
                i = i + 1
            else:
                m = 1
                break

    if m == 1:
        print ("Not a palindrome")
    else:
        print ("Palindrome")

if __name__ == "__main__":
    main()
