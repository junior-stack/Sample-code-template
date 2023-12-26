from typing import List

# probably use heapq library is better than this implemented one

# below will be max-heap implementation, if we wish to implement min heap, just change the comparator value


# see https://cs.stackexchange.com/questions/130167/why-does-the-formula-floori-1-2-find-the-parent-node-in-a-binary-heap
# i = 0, 1, 2... n-1
# parent(i) = (i - 1) // 2
# left_child(i) = 2*i + 1
# right_child(i) = 2 * i + 2
# this is also called max_heapify
def bubble_down(heap: List[int], i: int):
    curr_index = i
    while curr_index < len(heap):
        l = 2 * curr_index + 1
        r = 2 * curr_index + 2
        curr = heap[curr_index]
        largest_index = curr_index
        largest_element = curr
        if r < len(heap) and largest_element < heap[r]:
            largest_index = r
            largest_element = heap[r]

        if l < len(heap) and largest_element < heap[l]:
            largest_index = l
            largest_element = heap[l]
        
        if curr_index != largest_index:
            heap[curr_index], heap[largest_index] = heap[largest_index], heap[curr_index]
            curr_index = largest_index
        else:
            break 

def bubble_up(heap: List[int], i: int):
    curr_index = i
    while curr_index != 0:
        parent_index = (curr_index - 1) // 2

        if heap[curr_index] > heap[parent_index]:
            heap[curr_index], heap[parent_index] = heap[parent_index], heap[curr_index]
            curr_index = parent_index
        else:
            break
        

def build_heap(arr: List[int]):
    if len(arr) >= 2:
        i = (len(arr) - 2) // 2  # parent index of the last element
        while i > -1:
            bubble_down(arr, i)


def heappush(heap: List[int], element: int):
    heap.append(element)
    bubble_up(heap, len(heap) - 1)

def heappop(heap: List[int]):
    min_value = heap[0]
    heap[0] = heap[len(heap) - 1]
    heap.pop()
    bubble_down(heap, 0)
    return min_value

# combination of heappop() followed by heappush() but more efficient
def heapreplace(heap: List[int], element: int):
    min_value = heap[0]
    heap[0] = element
    bubble_down(heap, 0)
    return min_value

# combination of heappush() followed by heappop() but more efficient
def heappushpop(heap:List[int], element: int):
    min_value = heap[0]
    if min_value >= element:
        return element
    else:
        return heapreplace(heap, element)

def heap_sort(arr: List[int]):
    build_heap(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        bubble_down(arr, 0)


if __name__ == '__main__':
    arr = [1, 2]
    print(arr[0])
    print(arr[1])

    