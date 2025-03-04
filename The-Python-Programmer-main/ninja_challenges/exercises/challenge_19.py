# Challenge 19 - Count Servers that Communicate
# You are given a map of a server center, represented as a m * n integer matrix grid,
# where 1 means that on that cell there is a server and 0 means that it is no server.
# Two servers are said to communicate if they are on the same row or on the same column.
# Return the number of servers that communicate with any other server.

# Example 1:
# Input: grid = [[1,0],[0,1]]
# Output: 0
# Explanation: No servers can communicate with others.

# Example 2:
# Input: grid = [[1,0],[1,1]]
# Output: 3
# Explanation: All three servers can communicate with at least one other server.

# Example 3:
# Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
# Output: 4
# Explanation: The two servers in the first row can communicate with each other.


def count_servers(grid: list[list[int]]) -> int: ...
