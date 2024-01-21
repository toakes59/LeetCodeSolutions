def multiply(num1, num2):
    # Check if any of the numbers is zero, in which case the product is zero
    if num1 == "0" or num2 == "0":
        return "0"

    # Get the lengths of the input numbers
    len1, len2 = len(num1), len(num2)

    # Initialize an array to store the product
    result = [0] * (len1 + len2)

    # Iterate through each digit of num1 in reverse
    for i in range(len1 - 1, -1, -1):
        carry = 0  # Initialize a carry for each multiplication

        # Iterate through each digit of num2 in reverse
        for j in range(len2 - 1, -1, -1):
            # Calculate the product of the current digits and add it to the result
            temp_sum = (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0")) + result[i + j + 1] + carry
            result[i + j + 1] = temp_sum % 10  # Update the current digit in the result
            carry = temp_sum // 10  # Update the carry for the next iteration

        result[i] += carry  # Add any remaining carry to the current digit in the result

    # Convert the result to a string
    result_str = "".join(map(str, result))
    
    # Remove leading zeros
    result_str = result_str.lstrip("0")

    return result_str if result_str else "0"

# Example usage:
num1 = "123"
num2 = "456"
result = multiply(num1, num2)
print(result)  # Output: "56088"
