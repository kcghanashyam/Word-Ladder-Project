# Word Ladder Solver

## Author
Ghanashyam KC 
Internship Task Submission  

---

## Problem Overview

This project solves the Word Ladder problem, where a start word is transformed into an end word by changing one letter at a time.

Rules:
- Only one letter can change at each step
- Each intermediate word must exist in the dictionary
- All words must have the same length

Example:

CAT → COT → DOT → DOG

---

## Approach

This solution uses Breadth-First Search (BFS) because BFS guarantees the shortest transformation path.

BFS explores all possible valid transformations level by level. The first time the end word is reached, the path obtained is guaranteed to be the shortest possible sequence.

This approach is suitable for graph traversal problems where each word can be treated as a node connected to other words differing by one letter.

---

## Data Structures Used

### Queue (`collections.deque`)
- Used to implement BFS traversal
- Stores transformation paths currently being explored
- Supports efficient insertion and deletion operations

### Set for Dictionary
- Stores all valid dictionary words
- Provides O(1) lookup time for checking valid words

### Visited Set
- Prevents revisiting already explored words
- Avoids repeated computation and infinite loops

---

## Algorithm Steps

1. Validate edge cases:
   - Check whether start and end words have the same length
   - Check whether the end word exists in the dictionary
   - Check whether start and end words are identical

2. Initialize:
   - Queue with the starting word path
   - Visited set containing the start word

3. While the queue is not empty:
   - Remove the first path from the queue
   - Get the current word from the path
   - Generate all possible one-letter transformations
   - Check whether generated words:
     - Exist in the dictionary
     - Have not been visited
   - Add valid transformations to the queue
   - If the end word is reached, return the path

4. If the queue becomes empty:
   - No valid transformation exists

---

## Test Cases

### Test Case 1 — Solvable

Input:
- Start Word: CAT
- End Word: DOG

Output:
CAT → COT → DOT → DOG

Result:
- Valid transformation path found

---

### Test Case 2 — Different Length Words

Input:
- Start Word: CAT
- End Word: PART

Output:
Words have different lengths

---

### Test Case 3 — Start Equals End

Input:
- Start Word: CAT
- End Word: CAT

Output:
Start equals end word

---
### Test Case 4 — Unsolvable (no path)

Input:
- Start Word: CAT
- End Word: ZOO

Output:
End word not in dictionary

Reason:
- No connecting transformation sequence exists in the dictionary

---

### Test Case 5 — Another Solvable Path

Input:
- Start Word: COLD
- End Word: MOST

Output:
COLD → BOLD → BOLT → BOAT → MOAT → MOST

Result:
- Valid transformation path found

## Time Complexity

Time Complexity:

O(26 × L × N)

Where:
- L = length of each word
- N = number of words in the dictionary

For each character position, the algorithm tries all possible alphabet substitutions.

---

## Space Complexity

Space Complexity:

O(N)

Space is required for:
- Queue storage
- Visited set
- Dictionary set

---

## Risks with Large Dictionaries

If the dictionary size increases significantly (for example, 1 million words), the following issues may occur:

### Memory Usage
- Storing complete transformation paths in the queue may consume large amounts of memory

### Performance
- BFS may require significant processing time due to the large search space
- A large number of transformations are generated during execution

---

## Possible Optimizations

### Bidirectional BFS
Instead of searching only from the start word:
- Search simultaneously from both start and end words
- Stop when both searches meet
- Reduces search space significantly

### Pattern-Based Preprocessing
Generate patterns such as:

CAT → *AT, C*T, CA*

This allows faster lookup of neighboring words.

### Parent Pointer Storage
Instead of storing complete paths:
- Store parent references only
- Reconstruct the final path after reaching the destination
- Reduces memory usage

---

## Project Structure

word-ladder-project
│
├── src
│   ├── __init__.py
│   ├── dictionary.py
│   └── word_ladder.py
│
├── tests
│   └── test_cases.py
│
├── .gitignore
├── README.md
├── requirements.txt
└── run.py 

---

## How to Run

Run the main program:

```bash
python run.py

```bash
python -m tests.test_cases