# Time & Space Complexity Reference Guide

A comprehensive cheat sheet for data structures and algorithms commonly tested in technical interviews.

---

## 📚 DATA STRUCTURES

### Array / List
| Operation | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Access by index | O(1) | O(1) | Direct index access |
| Search (unsorted) | O(n) | O(1) | Linear search |
| Search (sorted, binary search) | O(log n) | O(1) | Requires sorted array |
| Insert at end | O(1) amortized | O(1) | Dynamic array |
| Insert at beginning/middle | O(n) | O(1) | Need to shift elements |
| Delete by index | O(n) | O(1) | Need to shift elements |
| Delete by value (unsorted) | O(n) | O(1) | Linear search + shift |
| Sorting | O(n log n) | O(1) or O(n) | Depends on algorithm |

### Linked List (Singly/Doubly)
| Operation | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Access by index | O(n) | O(1) | Must traverse from head |
| Search | O(n) | O(1) | Linear search |
| Insert at head | O(1) | O(1) | |
| Insert at tail | O(1) | O(1) | If tail pointer maintained |
| Insert at position | O(n) | O(1) | O(n) to find position |
| Delete by value | O(n) | O(1) | O(n) to find node |
| Delete head | O(1) | O(1) | |
| Delete tail | O(n) | O(1) | Must find second-to-last |

### Stack
| Operation | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Push | O(1) | O(1) | |
| Pop | O(1) | O(1) | |
| Peek/Top | O(1) | O(1) | |
| Search | O(n) | O(1) | Must pop elements |
| Is Empty | O(1) | O(1) | |

### Queue
| Operation | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Enqueue | O(1) | O(1) | |
| Dequeue | O(1) | O(1) | |
| Front | O(1) | O(1) | |
| Search | O(n) | O(1) | Must dequeue elements |
| Is Empty | O(1) | O(1) | |

### Hash Table / Hash Map / Dictionary
| Operation | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Insert/Set | O(1) average, O(n) worst | O(n) | Worst case: all collisions |
| Search/Get | O(1) average, O(n) worst | O(1) | Worst case: all collisions |
| Delete | O(1) average, O(n) worst | O(1) | Worst case: all collisions |
| Contains Key | O(1) average, O(n) worst | O(1) | |
| Iterate all elements | O(n) | O(1) | Must visit all buckets |

**Note:** Hash table operations are O(1) average case but O(n) worst case due to collisions. Good hash function + load factor management keeps it near O(1).

### Binary Search Tree (BST)
| Operation | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Search | O(log n) average, O(n) worst | O(1) | Worst: skewed tree |
| Insert | O(log n) average, O(n) worst | O(1) | Worst: skewed tree |
| Delete | O(log n) average, O(n) worst | O(1) | Worst: skewed tree |
| Find Min/Max | O(log n) average, O(n) worst | O(1) | Worst: skewed tree |
| In-order traversal | O(n) | O(h) | h = height, O(log n) average |
| Pre-order traversal | O(n) | O(h) | |
| Post-order traversal | O(n) | O(h) | |

**Note:** Self-balancing BSTs (AVL, Red-Black) guarantee O(log n) for all operations.

### Heap (Min/Max Heap)
| Operation | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Find Min/Max | O(1) | O(1) | Root element |
| Insert/Push | O(log n) | O(1) | Bubble up |
| Delete Min/Max | O(log n) | O(1) | Extract root + heapify |
| Build Heap | O(n) | O(1) | From unsorted array |
| Heapify | O(log n) | O(1) | Fix one violation |
| Search | O(n) | O(1) | Not designed for search |

### Trie (Prefix Tree)
| Operation | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Insert | O(m) | O(m) | m = length of string |
| Search | O(m) | O(1) | m = length of string |
| Delete | O(m) | O(1) | m = length of string |
| Prefix Search | O(m) | O(1) | m = length of prefix |
| Space: n words of avg length m | O(ALPHABET_SIZE × m × n) | | |

### Graph (Adjacency List)
| Operation | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Add vertex | O(1) | O(1) | |
| Add edge | O(1) | O(1) | |
| Remove vertex | O(V + E) | O(1) | Must remove all edges |
| Remove edge | O(E) worst, O(1) average | O(1) | |
| Check if edge exists | O(E) worst, O(1) average | O(1) | |
| Get neighbors | O(degree) | O(1) | |

### Graph (Adjacency Matrix)
| Operation | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Add vertex | O(V²) | O(V²) | Must resize matrix |
| Add edge | O(1) | O(1) | |
| Remove vertex | O(V²) | O(1) | |
| Remove edge | O(1) | O(1) | |
| Check if edge exists | O(1) | O(1) | Direct lookup |
| Get neighbors | O(V) | O(V) | Scan entire row |

**Space:** O(V²) for adjacency matrix, O(V + E) for adjacency list

---

## 🔄 SORTING ALGORITHMS

| Algorithm | Best | Average | Worst | Space | Stable? | Notes |
|-----------|------|---------|-------|-------|---------|-------|
| **Bubble Sort** | O(n) | O(n²) | O(n²) | O(1) | Yes | Only O(n) if already sorted |
| **Selection Sort** | O(n²) | O(n²) | O(n²) | O(1) | No | Always makes O(n²) comparisons |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) | Yes | O(n) if already sorted |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | Divide & conquer |
| **Quick Sort** | O(n log n) | O(n log n) | O(n²) | O(log n) | No | O(n²) if pivot is always min/max |
| **Heap Sort** | O(n log n) | O(n log n) | O(n log n) | O(1) | No | Uses heap data structure |
| **Counting Sort** | O(n + k) | O(n + k) | O(n + k) | O(k) | Yes | k = range of values |
| **Radix Sort** | O(d(n + k)) | O(d(n + k)) | O(d(n + k)) | O(n + k) | Yes | d = number of digits |
| **Bucket Sort** | O(n + k) | O(n + k) | O(n²) | O(n) | Yes | k = number of buckets |

---

## 🔍 SEARCHING ALGORITHMS

| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| **Linear Search** | O(n) | O(1) | Works on unsorted arrays |
| **Binary Search** | O(log n) | O(1) | Requires sorted array |
| **Ternary Search** | O(log₃ n) | O(1) | Divides into 3 parts |
| **Jump Search** | O(√n) | O(1) | Optimal block size = √n |
| **Interpolation Search** | O(log log n) avg, O(n) worst | O(1) | Requires sorted + uniformly distributed |

---

## 🌳 TREE ALGORITHMS

| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| **DFS (Recursive)** | O(V + E) | O(h) | h = height, O(V) worst |
| **DFS (Iterative)** | O(V + E) | O(V) | Stack can hold all nodes |
| **BFS (Level-order)** | O(V + E) | O(V) | Queue holds all nodes in worst case |
| **In-order Traversal** | O(n) | O(h) | h = height |
| **Pre-order Traversal** | O(n) | O(h) | h = height |
| **Post-order Traversal** | O(n) | O(h) | h = height |
| **Height of Tree** | O(n) | O(h) | Must visit all nodes |
| **Check if Balanced** | O(n) | O(h) | |

**For Binary Tree:** V = n (number of nodes), E = n-1 (number of edges)

---

## 📊 GRAPH ALGORITHMS

| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| **BFS** | O(V + E) | O(V) | Queue stores vertices |
| **DFS** | O(V + E) | O(V) | Recursion stack |
| **Dijkstra's (Binary Heap)** | O((V + E) log V) | O(V) | Single source shortest path |
| **Dijkstra's (Fibonacci Heap)** | O(E + V log V) | O(V) | Better for dense graphs |
| **Bellman-Ford** | O(VE) | O(V) | Handles negative weights |
| **Floyd-Warshall** | O(V³) | O(V²) | All pairs shortest path |
| **Kruskal's MST** | O(E log E) = O(E log V) | O(V) | Union-Find data structure |
| **Prim's MST (Binary Heap)** | O(E log V) | O(V) | |
| **Prim's MST (Fibonacci Heap)** | O(E + V log V) | O(V) | |
| **Topological Sort (DFS)** | O(V + E) | O(V) | |
| **Topological Sort (Kahn's)** | O(V + E) | O(V) | BFS-based |
| **Detect Cycle (DFS)** | O(V + E) | O(V) | |
| **Detect Cycle (Union-Find)** | O(V log V) | O(V) | |
| **Strongly Connected Components (Kosaraju)** | O(V + E) | O(V) | |
| **Articulation Points (Tarjan)** | O(V + E) | O(V) | |

**V = vertices, E = edges**

---

## 🔢 DYNAMIC PROGRAMMING

| Pattern | Time Complexity | Space Complexity | Notes |
|---------|----------------|------------------|-------|
| **1D DP** | Usually O(n) | O(n) or O(1) | Can often optimize to O(1) space |
| **2D DP** | Usually O(n × m) | O(n × m) | Can often optimize to O(min(n, m)) |
| **Memoization** | # of subproblems | # of subproblems | Trade-off: recursion overhead |
| **Tabulation** | # of subproblems | Usually same as memoization | |

**Examples:**
- Fibonacci: O(n) time, O(1) space (optimized)
- Longest Common Subsequence: O(n × m) time, O(min(n, m)) space (optimized)
- 0/1 Knapsack: O(n × W) time, O(W) space (optimized)

---

## 🎯 COMMON ALGORITHM PATTERNS

### Two Pointers
- **Time:** Usually O(n)
- **Space:** O(1)
- Use cases: Sorted arrays, palindromes, removing duplicates

### Sliding Window
- **Time:** O(n)
- **Space:** O(k) where k = window size
- Use cases: Subarrays, substring problems

### Binary Search (on Answer Space)
- **Time:** O(log(max - min) × cost_of_check)
- **Space:** O(1)
- Use cases: Search space problems (e.g., capacity problems)

### Backtracking
- **Time:** Often exponential O(b^d) where b = branching factor, d = depth
- **Space:** O(d) for recursion stack
- Use cases: Permutations, combinations, N-Queens

### Divide & Conquer
- **Time:** Usually O(n log n)
- **Space:** O(log n) for recursion
- Use cases: Merge sort, quicksort, binary search

### Greedy
- **Time:** Varies, often O(n log n) due to sorting
- **Space:** Usually O(1) or O(n) for sorting
- Use cases: Activity selection, fractional knapsack

---

## 📐 USEFUL COMPLEXITY RANGES

For interview purposes, common constraints and expected complexities:

| Input Size | Expected Complexity | Examples |
|------------|---------------------|----------|
| n ≤ 10 | O(n!) | Permutations, brute force |
| n ≤ 20 | O(2ⁿ) | Subset generation, backtracking |
| n ≤ 100 | O(n³) | 3 nested loops, Floyd-Warshall |
| n ≤ 1,000 | O(n²) | Nested loops, DP |
| n ≤ 10,000 | O(n log n) | Sorting, divide & conquer |
| n ≤ 1,000,000 | O(n) or O(n log n) | Single pass, binary search |
| n > 1,000,000 | O(n) or O(log n) | Single pass, binary search |

---

## 💡 QUICK REFERENCE

### Most Common in Interviews:
- **Hash Map operations:** O(1) average
- **Binary search:** O(log n)
- **Tree traversal:** O(n)
- **Graph BFS/DFS:** O(V + E)
- **Sorting:** O(n log n)
- **DP:** Usually O(n) or O(n²)

### Red Flags (Too Slow):
- O(n³) or worse for large inputs (unless necessary)
- Nested loops without optimization
- Repeated calculations (should use memoization)

### Optimization Techniques:
- Sort first: Often converts O(n²) to O(n log n)
- Hash map: Convert O(n) search to O(1) lookup
- Two pointers: Convert O(n²) to O(n) for sorted arrays
- Binary search: Convert O(n) to O(log n) for sorted/search space problems
- Sliding window: Convert O(n²) to O(n) for subarray problems

---

## 🎓 MEMORY AIDS

- **Tree height in balanced tree:** O(log n)
- **Tree height in worst case (skewed):** O(n)
- **Graph with V vertices can have:** Up to V(V-1)/2 edges (complete graph)
- **Hash table:** O(1) on average, O(n) worst case (all collisions)
- **Heap operations:** O(log n) - think "tree height"
- **String operations:** Often O(m) where m = string length

---

**Remember:** Always state both average and worst-case complexities when relevant, and mention space complexity alongside time complexity!
