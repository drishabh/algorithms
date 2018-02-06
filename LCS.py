##Author: Rishabh Dalal
##Description: Program to find the length of longest common substring

def LCS(stringA, stringB):
    
    table = [[0 for k in range(len(stringB)+1)] for l in range(len(stringA)+1)]
    result = 0
 
    for i in range(len(stringA) + 1):
        for j in range(len(stringB) + 1):
            if (i == 0 or j == 0):
                table[i][j] = 0
            elif (stringA[i-1] == stringB[j-1]):
                table[i][j] = table[i-1][j-1] + 1
                result = max(result, table[i][j])
            else:
                table[i][j] = 0
    
    return result
