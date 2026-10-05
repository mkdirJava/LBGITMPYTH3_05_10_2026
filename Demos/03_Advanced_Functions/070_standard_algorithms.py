# a concise tour of standard algorithm types with clear examples,
# typical use‑cases, and Python snippets.

# Sorting Algorithms
# Goal: Reorder items (often to speed up later searches or aggregations).
# - Bubble Sort (educational; O(n²))
# - Insertion Sort (good for nearly-sorted data; O(n²), best O(n))
# - Merge Sort (stable; O(n log n); divide‑and‑conquer)
# - Quick Sort (fast average O(n log n), worst O(n²); in-place)
# # Example – Merge Sort
def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a)//2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    # merge
    i=j=0; out=[]
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i]); i+=1
        else:
            out.append(right[j]); j+=1
    out.extend(left[i:]); out.extend(right[j:])
    return out

a =[3,6,5,8,2,4,1,7,10,9,8]
print(merge_sort(a))

# Searching Algorithms
# Goal: Find elements or positions.
# - Linear Search (O(n))
# - Binary Search (on sorted arrays; O(log n))

def binary_search(a, x):
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == x:
            return mid
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

# Binary search only works on sorted lists
a =[3,6,5,8,2,4,1,7,10,9,8]
a = merge_sort(a)
print(binary_search(a, 10))
names = ["Harry", "Mary", "Kamran", "Saeed", "Angelique", "Svetlana"]
names = merge_sort(names)
print(binary_search(names, "Saeed"))


# Hashing & Sets/Maps
# Goal: Fast membership, counting, grouping.
# - Hash Table / Dictionary (avg O(1) insert/lookup)
# - Frequency counting, deduplication, join‑like lookups
#
# Example – Frequency Count

from collections import Counter
counts = Counter(["USD","EUR","USD","GBP","USD"])
print(counts) # {'USD': 3, 'EUR': 1, 'GBP': 1}

# Greedy Algorithms
# Goal: Build solution by repeatedly taking the locally optimal choice.
# - Interval Scheduling (maximize non-overlapping intervals)
# - Huffman Coding (optimal prefix codes)
# - Minimum Spanning Tree (Prim’s/Kruskal’s)
#
# Example – Activity Selection (by earliest finish)
def select_intervals(intervals):
    intervals = sorted(intervals, key=lambda x: x[1])
    result, last_end = [], float("-inf")
    for s, e in intervals:
        if s >= last_end:
            result.append((s, e))
            last_end = e
    return result


intervals = [
    (1, 4),
    (3, 5),
    (0, 6),
    (5, 7),
    (3, 9),
    (5, 9),
    (6, 10),
    (8, 11),
    (8, 12),
    (2, 14),
    (12, 16)
]

selected = select_intervals(intervals)

print("Original intervals:")
print(intervals)

print("\nSelected intervals (non‑overlapping):")
print(selected)

# Practical Finance Use Cases for select_intervals
#
#
# Execution in “low‑spread” windows
# When algorithmic trading for FX or equities, you might precompute time windows
# during the day where the bid‑ask spread is below a threshold (i.e., cheaper to trade).
# To avoid overlapping logic and to keep the strategy simple, you select the largest set
# of non-overlapping windows to schedule passive child orders.

# --- Example: pick non-overlapping low-spread windows to execute child orders ---
# What this does
# - Uses select_intervals to pick the maximum number of non-overlapping low-cost windows.
# - Distributes the intended parent order quantity across the chosen windows.
# I- n practice, you might then pass these windows to your execution engine to place passive orders (e.g., pegged to mid or best bid/offer) only during those windows.

# Windows are represented as (start_minute, end_minute) from market open.
# Suppose these came from analytics tagging the minutes with spread <= threshold.
low_spread_windows = [
    (15, 30),   # 09:15–09:30
    (20, 25),   # 09:20–09:25 (overlaps with 15–30)
    (35, 45),   # 09:35–09:45
    (40, 50),   # 09:40–09:50 (overlaps with 35–45)
    (55, 60),   # 09:55–10:00
    (58, 70),   # 09:58–10:10 (overlaps with 55–60)
    (75, 85),   # 10:15–10:25
]

selected = select_intervals(low_spread_windows)

print("Candidate low-spread windows:")
print(low_spread_windows)

print("\nSelected (non-overlapping) execution windows:")
print(selected)

# You could now schedule child orders, e.g. 1 VWAP slice per window:
def schedule_child_orders(windows, total_qty):
    per_window = total_qty // max(1, len(windows))
    plan = []
    for (start, end) in windows:
        plan.append({
            "window": (start, end),
            "qty": per_window
        })
    # Allocate any remainder to the last window
    remainder = total_qty - per_window * len(windows)
    if plan:
        plan[-1]["qty"] += remainder
    return plan

order_plan = schedule_child_orders(selected, total_qty=10000)
print("\nChild order plan:")
for leg in order_plan:
    print(leg)

# Divide and Conquer
# Goal: Split problem, solve subproblems, combine.
# - Merge Sort, Quick Sort
# - Closest Pair of Points
# - Fast Fourier Transform (FFT)

# See merge sort above


# Dynamic Programming (DP)
# Goal: Optimal substructure + overlapping subproblems; reuse results.
# - Knapsack, Coin Change
# - Edit Distance (Levenshtein)
# - Longest Increasing Subsequence (LIS)
#
# Example – 0/1 Knapsack (tabulation)

def knapsack(weights, values, W):
    n = len(weights)
    dp = [[0]*(W+1) for _ in range(n+1)]
    for i in range(1, n+1):
        w, v = weights[i-1], values[i-1]
        for cap in range(W+1):
            dp[i][cap] = dp[i-1][cap]
            if w <= cap:
                dp[i][cap] = max(dp[i][cap], dp[i-1][cap-w] + v)
    return dp[n][W]

# Portfolio optimisation with a maximum risk budget
# Suppose you have several assets, each with:
# - a risk weight (e.g., volatility, VAR, or regulatory risk weight)
# - an expected return
#
# You want to pick assets that fit under a total risk budget (capacity W) while maximizing expected return.
# Example
# - weights = asset risk contribution
# - values = expected returns
# - W = max risk allowed in portfolio

# Asset risk weights (e.g., Value-at-Risk contribution)
weights = [5, 8, 3, 6, 2]

# Expected returns (arbitrary units)
values = [10, 15, 7, 12, 4]

# Maximum risk budget
W = 10

max_return = knapsack(weights, values, W)
print("Max return under risk budget:", max_return)

# Graph Algorithms
# Goal: Paths, connectivity, spanning trees, flows.
# - BFS/DFS (reachability, topological sort)
# - Dijkstra (shortest paths with non‑negative weights)
# - Bellman‑Ford (handles negative edges)
# - Floyd‑Warshall (all‑pairs shortest paths)
# - Kruskal/Prim (MST)
# - Topological Sort (DAG order)
# # Example – Dijkstra (using heap)

# FX Currency Conversion Routing (finding the cheapest conversion path)
# Many FX conversion paths aren’t direct. A trader may want to convert:
# GBP → JPY, but the best rate might be via:
# GBP → USD → JPY.
# Dijkstra can choose the lowest-cost conversion route, where:
# - nodes = currencies
# - edges = conversion costs/spreads
# - weights = negative log of exchange rate or actual spread cost
import heapq

def dijkstra(graph, src):
    # graph: dict[node] -> list[(neighbor, weight)]
    dist = {u: float('inf') for u in graph}
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist.get(v, float('inf')):
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist


graph = {
    "GBP": [("USD", 0.02), ("EUR", 0.015)],
    "USD": [("JPY", 0.02)],
    "EUR": [("JPY", 0.03), ("USD", 0.01)],
    "JPY": []
}

print(dijkstra(graph, "GBP"))
# expected output: {'GBP': 0, 'USD': 0.02, 'EUR': 0.015, 'JPY': 0.04}
# cheapest way to convert a chosen currency to chosen currency (GBP in this case):
# USD converts directly at 0.02, as does EUR (0.15).
# However, JPY has no direct conversion and could be converted:
# JPY -> EUR (0.03) - > GBP (0.015) => 0.045
# or
# JPY -> USD (0.02) -> GBP (0.02) => 0.04


# Backtracking & Constraint Search
# Goal: Systematically search with pruning.
# - N‑Queens, Sudoku
# - Subset / Combination generation
# - Path search with constraints
#
# Example – Subsets
# financial‑services example where generating all subsets of a set (the power set) is useful.
# Finding All Valid Trade Combinations Under Constraints
# If you have a set of possible trades and want to evaluate all combinations:
# - for capital budgeting
# - for portfolio construction
# - for brute‑force P&L maximisation
# - for risk‑limit checks
#
# Example
def subsets(nums):
    out, cur = [], []
    def dfs(i):
        if i == len(nums):
            out.append(cur[:]); return
        dfs(i+1)        # skip
        cur.append(nums[i])
        dfs(i+1)        # take
        cur.pop()
    dfs(0)
    return out

trades = ["Long AAPL", "Short EURUSD", "Buy Gold", "Sell BTC"]
trade_sets = subsets(trades)

for t in trade_sets:
    print("Trade combination:", t)

# Other standard algorithms:

# String Algorithms
# Goal: Search, match, parse.
# - KMP (O(n+m) pattern search)
# - Rabin‑Karp (rolling hash)
# - Trie (prefix queries)
# - Suffix Array/Tree (advanced)
# Example - Simple Rabin-Karp (rolling hash idea)
def find_substring(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0: return 0
    base, mod = 257, 2_000_003
    power = pow(base, m-1, mod)
    hp = 0; ht = 0
    for i in range(m):
        hp = (hp*base + ord(pattern[i])) % mod
        ht = (ht*base + ord(text[i])) % mod
    for i in range(n - m + 1):
        if hp == ht and text[i:i+m] == pattern:
            return i
        if i < n - m:
            ht = (ht - ord(text[i]) * power) % mod
            ht = (ht*base + ord(text[i+m])) % mod
            ht %= mod
    return -1

# Numerical & Optimization Algorithms
# Goal: Solve equations, optimize functions.
# - Binary Search on answer (parametric search)
# - Newton–Raphson (root finding)
# - Gradient Descent (ML optimization)
# - Linear Programming (Simplex, Interior‑Point)
# Example – Newton’s Method (scalar)
def newton(f, df, x0, tol=1e-8, iters=100):
    x = x0
    for _ in range(iters):
        step = f(x)/df(x)
        x_new = x - step
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x

# Probabilistic & Randomized Algorithms
# Goal: Use randomness for simpler/fast solutions.
# - Reservoir Sampling (stream sampling)
# - Monte Carlo (simulation; pricing/risk)
# - Randomized QuickSort
# Example – Reservoir Sampling (k=1)
import random

def reservoir_sample(stream):
    result = None
    for i, x in enumerate(stream, 1):
        if random.randrange(i) == 0:
            result = x
    return result

# Data Structure Patterns (Building Blocks)
# Frequently used for algorithmic efficiency:
# - Heaps/Priority Queues (e.g., top‑k, scheduling)
# - Union‑Find (Disjoint Set Union) (connectivity, Kruskal)
# - Segment Trees / Fenwick Trees (range queries)
# - LRU Cache (recently used eviction)
# Example – Union‑Find
class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0]*n
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb: return False
        if self.r[ra] < self.r[rb]:
            ra, rb = rb, ra
        self.p[rb] = ra
        if self.r[ra] == self.r[rb]:
            self.r[ra] += 1
        return True

# Concurrency / Parallel Patterns (High‑level)
# Goal: Speed up with multiple cores or I/O overlap.
# - Map‑Reduce (batch processing)
# - Producer–Consumer (pipelines)
# - Work stealing / task pools
# # (In Python, use concurrent.futures, asyncio, multiprocessing.)

# Practical Finance‑Flavoured Examples
# - Top‑k movers → heap (priority queue)
# - Risk bucketing → hashing and grouping
# - Best execution routes → shortest paths / min‑cost flow
# - P&L path simulation → Monte Carlo
# - Position netting → union/find across accounts, or grouping
# Example – Top‑k Movers with a Heap
import heapq

def top_k_moves(symbol_returns, k=5):
    # symbol_returns: list of (symbol, daily_return)
    return heapq.nlargest(k, symbol_returns, key=lambda x: abs(x[1]))


# def calculate_savings_balance(principal, interest_rate, monthly_deposit = 12):
#     """
#     Calculate the final balance after one year of simple interest.
#
#     principal: starting account balance (£)
#     interest_rate: annual interest rate as a decimal (e.g., 0.03 for 3%)
#     monthly_deposit: amount deposited each month (£)
#     """
#     # Total saved through monthly deposits
#     deposit_total = monthly_deposit * 12
#
#     # Interest earned on the opening balance only (simple interest)
#     interest_earned = principal * interest_rate
#
#     # Final balance after one year
#     final_balance = principal + deposit_total + interest_earned
#     return final_balance


# def calc_product(x, y, z):
#     print(f"product: {x * y * z}")
#
#
# numbers_tuple = 2, 4, 6
# calc_product(*numbers_tuple)


def calc_products(a, *nums):
    res = ""
    for n in nums:
        res += f"{str(a * n)} "
    print(res)

calc_products(5, 1, 2, 3, 4)


def calculate_savings_balance(principal, int_rate, /, monthly_deposit=12):
    print(f'principal: {principal}, rate: {int_rate}, deposit: {monthly_deposit}')

calculate_savings_balance(1000, 0.03, monthly_deposit=50)
calculate_savings_balance(1000, 0.05)
calculate_savings_balance(principal=1000, int_rate=0.03)
