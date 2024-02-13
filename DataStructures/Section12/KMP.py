#String matching by KMP algorithm

def pfun(pattern):
    n = len(pattern)
    prefix_fun = [0]*(n)

    k = 0
    for q in range(2, n):
        while k>0 and pattern[k + 1] != pattern[q]:
            k = prefix_fun[k]
        if pattern[k + 1] == pattern[q]:
             k += 1
        prefix_fun[q] = k
    return prefix_fun


def KMP_Matcher(text, pattern):
    m = len(text)
    n = len(pattern)
    flag = False
    text = '-' + text
    pattern = '-' + pattern
    prefix_fun = pfun(pattern)
    q = 0

    for i in range(1, m+1):
        while q > 0 and pattern[q + 1] != text[i]:
            q = prefix_fun[q]
        if pattern[q + 1] == text[i]:
            q += 1
        if q == n:
            print("Pattern occurs at positions ",i-n)     # print the index, where first match occurs.
            flag = True
            q = prefix_fun[q]
    if not flag:
        print('\nNo match found')


#Output of KMP algorithm
KMP_Matcher('aabaacaadaabaaba','aabaa')
