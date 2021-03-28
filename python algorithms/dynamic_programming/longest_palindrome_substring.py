"""
Problem: 
Find the longest palindrome substring from the string. Return the Length.

Solution: 
Base Condition : If sub-string is  palindrome return : length of sub-string. 
Recurse condition:
    If a substring is not palindrome , then there are two possibilities:
        1. Recurse the sub-string without 1st character 
        2. Recurse the sub-string without last character.
        3. Return max length of palindrome encountered in 1 & 2.. 
To solve the problem in Quadratic O(n^2) , we can store the intermediary results of sub-strings 
in dictionary and return from dictionary if same is encountered in subsequent calls. 

"""


# Check if given string is palindrome 

def isPal(s1):
    if s1 == s1[::-1]:
        return True
    else:
        return False


memo = {}


def find_pal(s, i=0, j=0):
    global memo, c
    c += 1  # To keep track of the recursive calls. 
    """
    If the substring is already encountered return from the memo dictionary.
    
    """
    if s in memo:
        return memo[s]

    """
    Check if a substring is palindrome or not. If palindrome store its length in memo dict  and return length.

    """
    if isPal(s):
        memo[s] = len(s)
        return memo[s]
    else:
        """
        If a substring is not palindrome , then there are two possibilities:
        1. Recurse the sub-string without 1st character 
        2. Recurse the sub-string without last character.
        3. Store the max length of palindrome encountered in 1 & 2 in the memo dictionary and return the same. 

        """

        s1 = s[i:j - 1]
        s2 = s[i + 1:j]
        memo[s] = max(find_pal(s1, i, j - 1), find_pal(s2, i + 1, j))
        return memo[s]


if __name__ == '__main__':
    string = 'hkahgahhflkghghhgJSuagbaanaanana'
    c = 0
    x = find_pal(string, 0, len(string))
    print(c, len(string), x)
    """
    Output: 941 32 6 
    i.e 941 function calls for 32 length of string & string of length 6 is found as palindrome. 
    Which proves the Complexity is O(32*32)~ (n2) ; where n is length of string. 

    """
