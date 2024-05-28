'''Link to Hackerank - https://www.hackerrank.com/challenges/counting-valleys/problem'''

def counting_valleys(n, s):
    current_level = 0
    count = 0
    for i in range(n):
        if s[i] == 'U':
            current_level += 1
        elif s[i] == 'D':
            current_level -= 1
            if current_level == -1:
                count += 1
    return count