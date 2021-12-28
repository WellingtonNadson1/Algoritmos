# Longest Common Subsequence

def lcs(X, Y):
    n = len(X)
    m = len(Y)
    l = {}
    
    for i in range(n + 1):
        l[(i, 0)] = 0
    
    for j in range(m + 1):
        l[(0, j)] = 0
        
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if X[i - 1] == Y[j - 1]:
                l[(i, j)] = l[(i - 1, j - 1)] + 1
            else:
                l[(i, j)] = max(l[(i - 1, j)], l[(i, j - 1)])
                
    return l

# Driver program to test the above function
X = 'AGGTAB'
Y = 'GXTXAYB'
print = ('Length of LCS is ', lcs(X, Y))
                