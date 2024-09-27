def is_match(message, pattern):
   
    m, p = len(message), len(pattern)

   
    dp = [[False] * (p + 1) for _ in range(m + 1)]

    
    dp[0][0] = True

    
    for j in range(1, p + 1):
        if pattern[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

   
    for i in range(1, m + 1):
        for j in range(1, p + 1):
            if pattern[j - 1] == message[i - 1] or pattern[j - 1] == '?':
              
                dp[i][j] = dp[i - 1][j - 1]
            elif pattern[j - 1] == '*':
              
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

    return dp[m][p]


message = input("Enter the secret message: ")
pattern = input("Enter the decoder pattern: ")


if is_match(message, pattern):
    print("The pattern matches the secret message!")
else:
    print("The pattern does not match the secret message.")
