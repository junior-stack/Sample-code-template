from typing import List
# Consider an array Arr[] = {1, 4, 5, 3, 12, 10}
# For i = 0: stk = {1}
# For i = 1: stk = {1, 4}
# For i = 2: stk = {1, 4, 5}
# For i = 3: stk = {1, 3}  [pop 4 and 5 as 4 > 3 and 5 > 3]
# For i = 4: stk = {1, 3, 12}
# For i = 5: stk = {1, 3, 10} [pop 12 as 12 > 10]
# the added element that pops the elements in the stack is the element next to the last popped elment in the array, fals
# [1, 6, 7, 3, 2, 4], 3 pops 6, 7 but 4 is closer to 6, 7
# the poped elements in the stack are next to each other in the array


# What problem uses monostack:
# simple explanation: if we need to use the next greate element and prev great element or each array element to solve a problem, a monostack is needed
# formally, as below
# let arr be an array, let i be an integer where arr[i] in arr
# let tuple ti = (arr[i], nextGreatElement(arr[i])) be a tuple
# if we need to construct relationship that R = f(t0, t1, ... tn-1), then we need monostack

# {12, 5, 4, 8, 3, 6}
# monotonically decreasing stack: 
# it can be used to find next greate element and prev great element of each element in the array by popping the element from the stack
# Next Great element: Find the first value on the right that is greater than the element
# prev great element: find the last value on the left that is greater than the element
#   - for each element that is popped,  the next Great element of each popped elements: the newly inserted element
#   -                                   the prev great element of each popped element: the element before this element in the stack
# https://itnext.io/monotonic-stack-identify-pattern-3da2d491a61e                          

# mono-decreasing stack
mono_decreasing_stack = []

mono_increasing_stack = []

def mono_increase_load_elements(mono_increasing_stack: List[int], arr: List[int]):
    for i in range(len(arr)):
        while mono_increasing_stack and arr[mono_increasing_stack[-1]] > arr[i]:
            mono_increasing_stack.pop()
        mono_increasing_stack.append(i)

def mono_decrease_load_elements(mono_decreasing_stack: List[int], arr: List[int]):
    for i in range(len(arr)):
        while mono_decreasing_stack and arr[mono_decreasing_stack[-1]] < arr[i]:
            mono_decreasing_stack.pop()
        mono_decreasing_stack.append(i)
