

def num2str(n, k=6):
    ans = str(n)
    while(len(ans) < k):
        ans = '0' + ans
    return ans

def longest_common_child(X, Y):
    # find the length of the strings
    m, n = len(X), len(Y)

    # declaring the array for storing the dp values
    lcc_length = [[None for _ in range(n+1)] for _ in range(m + 1)]
    lcc_content = [[None for _ in range(n+1)] for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                lcc_length[i][j] = 0
                lcc_content[i][j] = ''

            elif X[i - 1] == Y[j - 1]:
                lcc_length[i][j] = lcc_length[i-1][j-1] + 1
                lcc_content[i][j] = lcc_content[i-1][j-1] + '|' + X[i - 1]

            elif lcc_length[i - 1][j] > lcc_length[i][j - 1]:
                lcc_length[i][j] = lcc_length[i-1][j]
                lcc_content[i][j] = lcc_content[i-1][j]

            else: #lcc_length[i - 1][j] < lcc_length[i][j - 1]:
                lcc_length[i][j] = lcc_length[i][j-1]
                lcc_content[i][j] = lcc_content[i][j-1]

    lcc_content_ = lcc_content[m][n][1:].split('|')
    lcc_content_ = ''.join(lcc_content_)
    return lcc_content_

def matching_score(str_1, str_2, stop_words=''):
    for c in stop_words:
        str_1 = str_1.replace(c, '')
        str_2 = str_2.replace(c, '')
    lcc_content = longest_common_child(str_1, str_2)
    matching_score = 2 * len(lcc_content) / (len(str_1) + len(str_2))
    return lcc_content, matching_score

if __name__ == '__main__':
    print (matching_score('', 'efaced', ','))