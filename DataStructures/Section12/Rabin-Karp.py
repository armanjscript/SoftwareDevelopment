#String matching by Rabin-Kap algorithm

def generate_hash(text, pattern):
    ord_text = [ord(i) for i in text]
    ord_pattern = [ord(i) for i in pattern]
    len_text = len(text)
    len_pattern = len(pattern)
    len_hash_array = len_text - len_pattern + 1
    hash_text = [0]*(len_hash_array)
    hash_pattern = sum(ord_pattern)

    for i in range(0, len_hash_array):
        if i == 0:
            hash_text[i] = sum(ord_text[:len_pattern])
        else:
            hash_text[i] = ((hash_text[i - 1] - ord_text[i - 1]) + ord_text[i+len_pattern-1])
    return [hash_text, hash_pattern]


def Rabin_Karp_Matcher(text, pattern):
    text = str(text) 
    pattern = str(pattern)
    hash_text, hash_pattern = generate_hash(text, pattern)
    len_text = len(text) 
    len_pattern = len(pattern)
    flag = False
    for i in range(len(hash_text)):
        if hash_text[i] == hash_pattern:
            count = 0
            for j in range(len_pattern):
                if pattern[j] == text[i + j]:
                    count+=1
                else:
                    break
            if count == len_pattern:
                flag = True
                print("\nPattern occurs at index ", i)
    if not flag:
        print("Pattern is not at all present in the text")


#Output of Rabin-Karp
Rabin_Karp_Matcher("101110000011010010101101","1011")
Rabin_Karp_Matcher("ABBACCADABBACCEDF","ACCE")
