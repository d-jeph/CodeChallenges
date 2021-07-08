
#Link To Problem: https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

def jumpingOnClouds(c):
    # Write your code here
    jumps = 0
    n = 0
    while n < len(c) - 1:
        if (n + 2) < len(c) and c[n+2]==0:
            n += 2
        else:
            n += 1
            
        jumps += 1
    
    return jumps