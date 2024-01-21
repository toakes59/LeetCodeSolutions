# Count_and_Say
def countAndSay(n):
    if n == 1:
        return "1"

    prev = countAndSay(n - 1)
    result = ""
    count = 1

    for i in range(len(prev)):
        # Check if the current character is the same as the next one
        if i + 1 < len(prev) and prev[i] == prev[i + 1]:
            count += 1
        else:
            # Append the count and the character to the result
            result += str(count) + prev[i]
            count = 1  # Reset count for the next character

    return result

# Example usage:
n = 4
result = countAndSay(n)
print(result)  # Output: "1211"
