# Longest_Valid_Parentheses
def longestValidParentheses(s):
    stack = [-1]
    max_length = 0
    
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_length = max(max_length, i - stack[-1])
    
    return max_length



str = "(()(())"

i = 0
# stack = -1(
stack = 0
max_length = 0

i = 1
# stack = -1((
stack = 0 1
max_length = 0

i = 2
# stack = -1(
stack = 0
max_length = 2 - 0 = 2

i = 3
# stack = -1((
stack = 0 3
max_length = 2

i = 4
# stack = -1(((
stack = 0 3 4
max_length = 2

i = 5
# stack = -1((
stack = 0 3
max_length = 5 - 3 = 5

i = 6
# stack = -1(
stack = 0
max_length = 6 - 0 = 6


