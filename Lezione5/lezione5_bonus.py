'''1. Two Sum

Given a list of integers and a target sum, find all unique pairs of integers within the list that sum up to the target.'''

def two_sum(num: list, n: int):
    ris = []
    pair = []
    for x in num:
        for y in num:
            if x+y == n:
                pair = [x,y]
            if x not in ris and y not in ris:
                ris.append(pair)
    return pair

x = two_sum([1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9], 12)
print(x)

'''2. Longest Increasing Subsequence

Given a list of integers, find the length of the longest increasing subsequence within the list. 
An increasing subsequence is a sequence of elements from the array where each element is greater than or equal to the previous element.'''


'''3. Longest Common Subsequence

Given two strings, find the length of the longest common subsequence (LCS) between them. 
An LCS is a subsequence of one string that is also a subsequence of the other string while maintaining the relative order of elements.'''

'''4. Word Break Problem: 

Given a string and a dictionary of words, determine whether the string can be segmented into a space-separated sequence of one or more dictionary words. 
Each word in the dictionary must be a contiguous substring of the input string.'''


'''5. Longest Palindrome Subsequence:

A palindrome is a word, phrase, or sequence that reads the same backwards as forward. Given a string, the task is to find the longest palindrome subsequence within the string. 
A subsequence is obtained from a string by deleting zero or more elements without changing the order of the remaining elements.'''

'''6. Armstrong Number Checker:

Develop a function to check if a given number is an Armstrong number (the sum of its digits raised to the power of the number of digits equals the number itself).'''

'''7. Merge Two Sorted Lists: 

Implement a function to merge two sorted lists into a single sorted list.'''
def sort_two_list(list1: list, list2: list):
    merge = list1.copy()
    for y in list2:
        x = 0
        while x < len(merge):
            print("////////////")
            print(x)
            print(list2[x])
            print(y)
            print("////////////")
            if y <= list2[x]:
                merge.insert(x,y)
                print(f"{x}-----{y}----{merge}")
                break
            else:
                x += 1


    return merge

print(sort_two_list([1,2,3,4,5,6,7,8,9],[2,3,4,5,6,7,8]))

'''8. Find the Most Frequent Element:

Create a function that finds the element that appears most frequently in a given list.'''

def most_frequent(num: list) -> int:
    n: int = 0
    c: int = 0
    c1: int = 0
    for x in num:
        if x not in num:
            continue
        for y in num:
            if x == y:
                c+=1
        if c > c1:
            c1 = c
            n = x
        elif c < c1:
            break
'''9. Find the Second Largest Element in an Array:

Implement a function to find the second largest element in an unsorted list without using sorting algorithms.'''

'''10. Find the Intersection of Two Sorted Arrays:

Implement a function to find the elements that are present in both of the two sorted lists'''

def intersections(num: list, num1: list):
    ris = []
    for x in num:
        if x in num1:
            ris.append(x)

    return ris

print(intersections([1,23,4,5,7,8,9],[2,3,4,5,6,7,8]))