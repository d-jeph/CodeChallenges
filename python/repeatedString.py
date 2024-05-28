#Hackerank Link = https://www.hackerrank.com/challenges/repeated-string/problem

def repeatedString(s, n):
    char_count = n//len(s) * s.count('a')
    reminder_string = n%len(s)
    char_count = char_count + s[:reminder_string].count('a')
    return char_count
