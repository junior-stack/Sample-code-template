from collections import defaultdict, deque
from typing import Dict, List
# G is a graph, represented by a dictionary
# each key is a vertex, each value is a list of vertices that are adjacent vertex

def dfs_traversal(G: Dict[str, List[str]], s: str, vertexState: Dict[str, int]):
    stack = deque()
    stack.append([s, 0]) # stack is used to hold the vertex on the path and its child index
    vertexState[s] = 1
    while stack:
        vertex, index = stack[-1]

        child_index = index


        child = vertex # should point to G[vertex][child_index], just to prevent error if child_index == len(G[vertex]) since we need to define it outside the loop and use  it in line 26 block

        # if this child index is visited , point to the next
        while child_index < len(G[vertex]):
            child = G[vertex][child_index]
            if vertexState[child] != 0:
                child_index += 1
            else:
                break

        if child_index < len(G[vertex]):
            stack[-1][1] = child_index + 1 # update parent's index to be the next child right after curr child
            vertexState[child] = 1
            stack.append([child, 0])
            continue

        else:
            vertexState[vertex] = 2
            stack.pop()

def dfs(G: Dict[str, List[str]]):
    vertexState = defaultdict(lambda :0)
    for v in G.keys():
        if vertexState[v] == 0:
            dfs_traversal(G, v, vertexState)

if __name__ == '__main__':
    G = {'a': ['b', 'c'], 'b': [], 'c': []}
    dfs(G)
    print("passed")

