# You are given an array of variable pairs equations and an array of real numbers values, 
# where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. 
# Each Ai or Bi is a string that represents a single variable.

# You are also given some queries, 
# where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

# Return the answers to all queries. 
# If a single answer cannot be determined, return -1.0.

# Note: The input is always valid. 
# You may assume that evaluating the queries will not result in division by zero 
# and that there is no contradiction.

# Note: The variables that do not occur in the list of equations are undefined, 
# so the answer cannot be determined for them.

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Create and fill our database with equations
        data = dict()
        for (a_i, b_i), val in zip(equations, values):
            if not a_i in data:
                data[a_i] = {}
            if not b_i in data:
                data[b_i] = {}
            data[a_i][b_i] = val
            data[b_i][a_i] = 1.0/val
        
        # Search for appropriate equations
        def dfs(c_j, d_j):
            # Step 1. Rule exists
            if d_j in data[c_j]:
                return data[c_j][d_j]
            # Step 2. Division is equal to 1.0
            elif c_j == d_j:
                return 1.0
            # Step 3. Search for other rules while caching visited nodes
            else:
                visited.append(c_j)
                for b_j in data[c_j]:
                    if b_j not in visited:
                        r = dfs(b_j, d_j)
                        if r != -1.0:
                            out = data[c_j][b_j]*r
                            data[c_j][d_j] = out
                            data[d_j][c_j] = 1.0/out
                            return out
                return -1.0

        out = []
        for c_j, d_j in queries:
            if c_j in data and d_j in data:
                visited = []
                out.append(dfs(c_j, d_j))
            else:
                out.append(-1.0)
        return out        