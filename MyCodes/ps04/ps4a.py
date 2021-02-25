# Problem Set 4A
# Name: <your name here>
# Collaborators:
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
    
    
    # set a list to put all the permutations
    permutations_list = []
    # if the length is 1, return the inputpass #delete this line and replace with your code here
    if len(sequence) == 1:
        permutations_list.append(sequence)
        return permutations_list
    
    # if the length is 2, return 
    if len(sequence) ==2:
        permutations_list.append(sequence)
        permutations_list.append(sequence[1]+sequence[1])
    # divide and conquer
    #get the first letter and the rest
    first_letter = sequence[0]
    new_sequence = sequence[1:]

    # add the sequence to list
    permutations_list.append(sequence)
    # first letter is inserted into every between space of letters
    # ex) abcd -> a/bcd -> b'a'cd, bc'a'd
    for i in range (len(new_sequence)-1):
        permutation = new_sequence[:i] + first_letter + new_sequence[i:]

    # add the last
    permutations_list.append(new_sequence+first_letter)

    permutations_list.append(get_permutations(new_sequence))

    


    return permutations_list

if __name__ == '__main__':
   #EXAMPLE
   example_input = 'abc'
   print('Input:', example_input)
   print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
   print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

