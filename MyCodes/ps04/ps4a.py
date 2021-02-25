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
    
    # divide and conquer
    #get the first letter and the rest
    first_letter = sequence[0]
    new_sequence = sequence[1:]

    # a -> a
    # ab -> [a'b', 'b'a]
    # abc -> ['c'ab, a'c'b, ab'c'], ['c'ba, b'c'a, ba'c']
    # abcd -> ['d'cab, c'd'ab, ca'd'b, cab'd'],...
    #permutation can be defined by putting first letter at every space in string
    prev_result = get_permutations(new_sequence)
    
    #enumerate over all the sequece in list
    for i,item in enumerate(prev_result):
        # first 'a' + bcdef...
        permutations_list.append(first_letter + item)
        # now b'a'cd....,bc'a'd..... 
        for j in range(1,len(item)):
            permutations_list.append(item[:j]+first_letter+item[j:])
        # bcdef....+'a'
        permutations_list.append(item+first_letter)

    

    return permutations_list

if __name__ == '__main__':
   #EXAMPLE
   example_input = 'abc'
   print('Input:', example_input)
   print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
   print('Actual Output:', get_permutations(example_input))
   print('Size: ',len(get_permutations(example_input)))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

