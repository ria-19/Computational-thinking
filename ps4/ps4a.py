# Problem Set 4A
# Name: Riya
# Collaborators: None
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence
    
    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    
    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    #Base Case
    if len(sequence) <= 1:
        return sequence
    # Recursive Case
    else:
        perm_list = []
        first_char = sequence[:1]
        lst = get_permutations(sequence[1:]) 
        for elt in lst:
            for i in range(len(elt) + 1):
               new_str = elt[:i] + first_char + elt[i:]
               if new_str not in perm_list:
                   perm_list.append(new_str)
        return perm_list
               
if __name__ == '__main__':
#EXAMPLE: 1
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
#EXAMPLE: 2
    example_input = 'gig'
    print('Input:', example_input)
    print('Expected Output:', ['gig', 'ggi', 'igg'])
    print('Actual Output:', get_permutations(example_input))

#EXAMPLE: 3
    example_input = 'hey'
    print('Input:', example_input)
    print('Expected Output:', ['hey', 'hye', 'yeh', 'yhe', 'eyh', 'ehy'])
    print('Actual Output:', get_permutations(example_input))
    
#EXAMPLE: 4
    example_input = 'kzi'
    print('Input:', example_input)
    print('Expected Output:', ['kzi', 'kiz', 'zik', 'zki', 'ikz', 'izk'])
    print('Actual Output:', get_permutations(example_input))


   
