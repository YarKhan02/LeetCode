def palindromic_partitioning(s):
    result = []
    part = []

    def isPalindrome(s, l, r): 
        while l < r:
            if s[l] != s[r]:
                return False

            l, r = l + 1, r - 1
        
        return True
 

    def dfs(i):
        if i >= len(s):
            result.append(part.copy())
            return

        for j in range(i, len(s)):
            if isPalindrome(s, i, j):
                part.append(s[i:j + 1])
                dfs(j + 1)
                part.pop()

    dfs(0)

    return result

s = 'aab'
print(palindromic_partitioning(s))