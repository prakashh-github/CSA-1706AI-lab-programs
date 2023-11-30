from copy import deepcopy
from collections import deque

def is_valid(state):
    if state[0] < 0 or state[1] < 0 or state[2] < 0 or state[3] < 0 or state[4] < 0 or state[5] < 0:
        return False
    if state[0] > 3 or state[1] > 3 or state[2] > 1 or state[3] > 3 or state[4] > 3 or state[5] > 1:
        return False
    if state[0] < state[1] and state[0] != 0:
        return False
    if state[3] < state[4] and state[3] != 0:
        return False
    return True

def get_next_states(state):
    next_states = []
    if state[2] == 1:
        next_states.append([state[0] - 2, state[1], 0, state[3] + 2, state[4], 1])
        next_states.append([state[0], state[1] - 2, 0, state[3], state[4] + 2, 1])
        next_states.append([state[0] - 1, state[1] - 1, 0, state[3] + 1, state[4] + 1, 1])
        next_states.append([state[0] - 1, state[1], 0, state[3] + 1, state[4], 1])
        next_states.append([state[0], state[1] - 1, 0, state[3], state[4] + 1, 1])
    else:
        next_states.append([state[0] + 2, state[1], 1, state[3] - 2, state[4], 0])
        next_states.append([state[0], state[1] + 2, 1, state[3], state[4] - 2, 0])
        next_states.append([state[0] + 1, state[1] + 1, 1, state[3] - 1, state[4] - 1, 0])
        next_states.append([state[0] + 1, state[1], 1, state[3] - 1, state[4], 0])
        next_states.append([state[0], state[1] + 1, 1, state[3], state[4] - 1, 0])
    return [s for s in next_states if is_valid(s)]

def bfs(start, goal):
    queue = deque([[start]])
    visited = set([tuple(start)])
    while queue:
        path = queue.popleft()
        state = path[-1]
        if state == goal:
            return path
        for next_state in get_next_states(state):
            if tuple(next_state) not in visited:
                visited.add(tuple(next_state))
                new_path = list(path)
                new_path.append(next_state)
                queue.append(new_path)

start = [3, 3, 1, 0, 0, 0]
goal = [0, 0, 0, 3, 3, 1]
path = bfs(start, goal)

print("Missionaries and Cannibals Problem Solution:")
for state in path:
    print(state)
