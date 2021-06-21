"""
Given a list of numbers, return whether any two sums to k. For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""
def check_sums(array, k):
    potential_solutions = set()
    for num in array:
        if num in potential_solutions:
            return True
        potential_solutions.add(k - num)
    
    return False


assert not check_sums([], 17)
assert check_sums([10, 15, 3, 7], 17)
assert not check_sums([10, 15, 3, 4], 17)