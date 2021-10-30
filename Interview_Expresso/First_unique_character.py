#LC 387
#First Unique Character
#https://leetcode.com/problems/first-unique-character-in-a-string/
'''
Edge cases:
there will be a situation where we have empty strings or 
where we have no unique characters

Assumptions is that we may have a combination of upper and lower case characters

each char appears 1 or more times
if a char apprears one time, it's unique
so we need to count the characters

we need to look at each character
    update the character count and store it within a loop
lookup each character in the table
    if it is unique (value==1) return index
none are uique? return -1


aaron

{
    'a':2,
    'r':1,
    'o':1,
    'n':1
}

this is not given in order. But it is possible to represent dictionaries in order: using another method
'''



def first_unique_char(s):
    hash_table = {}
    for char in s:
        if char in hash_table:
            hash_table[char] = hash_table[char] + 1 
        else: 
            hash_table(char) = 1

    for i, char in enumerate(s):
        if hash_table[char] == 1:
            return i
    return -1


#Second solution:
def first_unique_char(s):
    for i, char in enumerate(s):
        if s.index(char) == s.rindex(char):
            return i
        return -1
#time complexity: O(n2)
#space complexity:O(1)

