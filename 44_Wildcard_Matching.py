# Wildcard_Matching
def isMatch(s, p):
    # Get the lengths of the input strings
    m, n = len(s), len(p)

    # Create a 2D array 'dp' to store the intermediate results of subproblems
    # dp[i][j] will be True if the first i characters of string s match the first j characters of pattern p
    dp = [[False] * (n + 1) for _ in range(m + 1)]

    # Base case: empty pattern matches empty string
    dp[0][0] = True

    # Handle patterns starting with '*'
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    # Fill in the rest of the dp array using dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If the current character in the pattern is '*', the result depends on
            # whether we consider '*' as an empty sequence or match it with the current character in the string.
            if p[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
            # If the current character in the pattern is '?' or matches the current character in the string,
            # the result depends on the previous characters' matching status.
            elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

    # The final result is stored in dp[m][n], indicating whether the entire string s matches the entire pattern p
    return dp[m][n]


bvottum up approach

# Example usage:
s = "adceb"
p = "*a*b"
result = isMatch(s, p)
print(result)  # Output: True
