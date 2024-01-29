def isPalindrome(s):
    total = 0
    i = 0
    while i < len(s):
        if len(s[i]) >= 2:  # check for length of 2 or greater
            rev = ''.join(reversed(s[i]))  # reverse the string
            if rev == s[i]:  # compare reversed string with original
                total += 1
        i += 1
    print(total)


if __name__ == '__main__':
    s = ['abdefc', 'xygyz', 'abeba', '123321']
    isPalindrome(s)