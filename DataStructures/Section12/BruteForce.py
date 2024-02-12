def brute_force(text, pattern):
    l1 = len(text)
    l2 = len(pattern)

    i=0
    j=0

    flag = False
    while i < l1:
        j = 0
        count = 0
        while j < l2:
            if i+j < l1 and text[i+j] == pattern[j]:
                count += 1
            j +=1
        if count == l2:
            print("\nPattern occurs at index ", i)
            flag = True
        i += 1
    if not flag:
        print('\nPattern is not at all present in the array')


#Output of string matching with Brute force
brute_force('acbcabccababcaacbcac','acbcac')
