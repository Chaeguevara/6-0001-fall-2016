"""
Tuple
"""

"""
Delete # mark with your interpreter when you run it.
"""
# te = ()
# t = (2,"mit",3)
# print("The value of t[0] is " + str(t[0]))
# print("The value of t[1:2] is " + str(t[1:2]))
# print("The value of t[1:3] is " + str(t[1:3]))
# print("The value of len(t) is " + str(len(t)))
# t[1] = 4


"""
Tuple swap
"""

"""
Typical way
"""

# x = 5
# y = 7
# print("The values of x, y are: " + str(x) + ", " + str(y))

# temp = x
# x = y
# y = temp

# print("The swapped values of x, y are: " + str(x) + ", " + str(y))

"""
with tuple
"""
# x = 5
# y = 7
# print("The values of x, y are: " + str(x) + ", " + str(y))

# (x,y) = (y,x)
# print("The swapped values of x, y are: " + str(x) + ", " + str(y))

# a = 5
# b = 7
# c = 12
# print("The values of a, b, c are: " + str(a) + ", " + str(b)+ ", " + str(c))

# (a,b,c) = (c,b,a)
# print("The swapped values of a, b, c are: " + str(a) + ", " + str(b)+ ", " + str(c))

"""
return more than 2 values
"""

# def quotient_and_remainder(x,y):
#     q = x // y #quotient, 몫
#     r = x % y #remainder, 나머지
#     return (q,r)

# (quot, rem) = quotient_and_remainder(4,5)

# print("The quotient and remainder 4 divided by 5 are " + str(quot) + ", " + str(rem))

"""
iterate over tuples
"""

# def get_data(aTuple):
#     nums = () # empty tuple
#     words = () # where unique words will be contained
#     for t in aTuple:
#         nums = nums + (t[0],) # get the integer of tuple in tuple
#         if t[1] not in words:
#             words = words + (t[1],) # if the string in tuple in tuple is a unique word, add to tuple 'words'
#     min_n = min(nums)
#     max_n = max(nums)
#     unique_words = len(words)
#     return (min_n, max_n, unique_words)

# test = ((1,"a"),(2, "b"),
#         (1,"a"),(7,"b"))
# (min, max, uniqueWords) = get_data(test)
# print("min:",min,"max:",max,"uniqueWords:",uniqueWords)

# tswift = ((2014,"Katy"),
#           (2014, "Harry"),
#           (2012,"Jake"), 
#           (2010,"Taylor"), 
#           (2008,"Joe"))    
# (min_year, max_year, num_people) = get_data(tswift)
# print("From", min_year, "to", max_year, \
#         "Taylor Swift wrote songs about", num_people, "people!")

"""
list
"""

# a_list = []
# L = [2, 'a', 4, [1,2]]
# print("len(L):",len(L))
# print("L[0]:",L[0])
# print("L[2]+1:",L[2]+1)
# print("L[3]:",L[3])
# i = 2
# print("L[i-1]:",L[i-1])
# L[4]

"""
mutable
"""

# L = [2, 1, 3]
# L[1] = 5
# print(L)

"""
iterate
"""
# def sum_elem_method1(L):
#   total = 0 
#   for i in range(len(L)): 
#       total += L[i] 
#   return total
  
# def sum_elem_method2(L):
#     total = 0 
#     for i in L: 
#         total += i 
#     return total

# print(sum_elem_method1([1,2,3,4]))
# print(sum_elem_method2([1,2,3,4]))

"""
add list
"""
# L1 = [2, 1, 3]
# L2 = [4, 5, 6]
# L3 = L1 + L2
# print("L1",L1,"L2",L2,"L3",L3)

# L1.extend([0, 6])
# print("L1",L1)

"""
remove list
"""
# L = [2,1,3,6,3,7,0]
# print("L.remove(2)",L.remove(2))
# print("L",L)
# print("L.remove(3)",L.remove(3))
# print("L",L)
# del(L[1])
# print("L",L)
# print("L.pop()",L.pop())
# print("L",L)

"""
Convert string to list
"""

# s = "I<3 cs"
# print("list(s)",list(s))
# print("s",s)
# print("s.split('<')",s.split('<'))
# print("s",s)

# L = ['a','b','c']
# print("''.join(L)",''.join(L))
# print("'_'.join(L)",'_'.join(L))

"""
Other operations
"""
# L=[9,6,0,3]
# print("sorted(L)",sorted(L))
# print("L",L)
# print("L.sort()",L.sort())
# print("L",L)
# print("L.reverse()",L.reverse())
# print("L",L)

#########################
## EXAMPLE: aliasing
#########################
# a = 1
# b = a
# print(a)
# print(b)

# warm = ['red', 'yellow', 'orange']
# hot = warm
# hot.append('pink')
# print(hot)
# print(warm)

#########################
## EXAMPLE: cloning
#########################
# cool = ['blue', 'green', 'grey']
# chill = cool[:]
# chill.append('black')
# print("chill",chill)
# print("cool",cool)


#########################
## EXAMPLE: sorting with/without mutation
#########################
# warm = ['red', 'yellow', 'orange']
# sortedwarm = warm.sort()
# print("warm",warm)
# print("sortedwarm",sortedwarm)

# cool = ['grey', 'green', 'blue']
# sortedcool = sorted(cool)
# print("cool",cool)
# print("sortedcool",sortedcool)

#########################
## EXAMPLE: lists of lists of lists...
#########################
# warm = ['yellow', 'orange']
# hot = ['red']
# brightcolors = [warm]
# brightcolors.append(hot)
# print("brightcolors",brightcolors)
# hot.append('pink')
# print("hot",hot)
# print("brightcolors",brightcolors)

# warm = ['yellow', 'orange']
# hot = ['red']
# brightcolors = warm
# brightcolors.append(hot)
# print("brightcolors",brightcolors)
# hot.append('pink')
# print("hot",hot)
# print("brightcolors",brightcolors)


#########
##final##
#########
# def remove_dups(L1, L2):
# 	for e in L1:
# 		if e in L2:
# 			L1.remove(e)

# L1 = [1, 2, 3, 4]
# L2 = [1, 2, 5, 6]
# remove_dups(L1,L2)

# print("L1",L1,"L2",L2)

def remove_dups_new(L1, L2):
    L1_copy = L1[:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)

L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
remove_dups_new(L1, L2)
print("L1",L1,"L2",L2)