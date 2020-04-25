def hammington(word1, word2):
    
    if len(word2) > len(word1):
        word1, word2 = word2, word1

    word2 += " " * (len(word1) - len(word2))
    word_len = len(word1)
    cnt = 0
    for i in range(word_len):
        if word1[i] != word2[i]:
            cnt += 1
    return cnt/len(word1)

def get_h(word1, word2):
    
    h = int(max(len(word1), len(word2))/2) - 1
    return h

def jaro(word1, word2):
    
    h = get_h(word1, word2)

    len1 = len(word1)
    len2 = len(word2)

    m = 0
    t = 0

    word1_check = [False]*len1
    word2_check = [False]*len2

    for i in range(len1):
        start_pos = max(0, i - h)
        end_pos = min(i+h+1,len2)
        #print(word1[start_pos:end_pos])

        for j in range(start_pos, end_pos):
            if word1[i] == word2[j] and not word2_check[j]:
                m += 1
                word1_check[i] = True
                word2_check[j] = True
                break

    if m == 0:
        return 0

    
    pos = 0
    for i in range(len1):
        if not word1_check[i]:
            continue
        while not word2_check[pos]:
            pos += 1
        if word1[i] != word2[pos]:
            t += 1
        pos += 1

    t = t / 2

    res = ((m/len1 + m/len2 + (m-t)/m)/3)

    "invert the result value to make in coparable"
    return res

def jaro_winkler(word1, word2, p = 0.1):

    
    len1 = len(word1)
    len2 = len(word2)
    
    d_j = jaro(word1, word2)

    same_prefix = 0

    for i in range(min(len1, len2)):
        if word1[i] == word2[i]:
            same_prefix += 1
    same_prefix = min(same_prefix, 4)

    res = d_j + (same_prefix * p * (1 - d_j))

    return res
    

