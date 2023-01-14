def Matching(text, pattern):
    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):
        j = 0

        # For current index i, check
        # for pattern match */
        while(j < m):
            if (text[i + j] != pattern[j]):
                break
            j += 1

        if (j == m):
            print("Pattern found at index ", i)

if __name__ == '__main__':
    text = input("Enter text :")
    pattern = input("Enter pattern :")
    Matching(text, pattern)
