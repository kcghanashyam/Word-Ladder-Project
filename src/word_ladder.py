import string
from collections import deque

letters = string.ascii_lowercase

def word_ladder(start, end, word_list):
    word_set = set(word_list)

    # Edge cases
    if end not in word_set:
        return None, "End word not in dictionary"

    if start == end:
        return [start], "Start equals end"

    if len(start) != len(end):
        return None, "Words have different lengths"

    # BFS
    queue = deque([[start]])
    visited = set([start])

    while queue:
        path = queue.popleft()
        current_word = path[-1]

        if current_word == end:
            return path, "Path found"

        for i in range(len(current_word)):
            for ch in letters:

                if ch == current_word[i]:
                    continue

                new_word = (
                    current_word[:i]
                    + ch
                    + current_word[i + 1:]
                )

                if (
                    new_word in word_set
                    and new_word not in visited
                ):
                    visited.add(new_word)
                    queue.append(path + [new_word])

    return None, "No valid transformation path found"