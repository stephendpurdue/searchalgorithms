(i) Calculate the row and column indexes of adjacent cells (top, bottom, left and right cells only). - Done

(ii) Append the row and column indexes of adjacent cells (the ones you calculated in the previous part) to the adj acent cel l s r ow, adj acent cel l s col list for the expansion by the DFS or BFS algorithm. Please note that the order of appending to these lists (rows and columns) is important. This means that the ith element (adjacent cell) of each list is expanded earlier than the (i + 1)th element by the search algorithm. The agent must expand the adjacent cells in the following order: 1. Left adjacent cell (Left move) 2. Bottom adjacent cell (Down move) 3. Right adjacent cell (Right move) 24. Top adjacent cell (Up move). - Done

(iii) Run DFS. How many expansions until the goal is found? - Done (22)

(iv) Implement BFS and run it. Which algorithm finds the goal earlier, i.e. less expansions? - DFS was quicker, it took 22 expansions, wheras BFS took 24.

(v) Change the code in a way that the agent can move into diagonal cells (you can consider any orders for the expansion). - Created two new funcitons: is_valid_diagonal to check if there was a diagonal that isn't a wall. And valid_move to determine if the move can be completed

(vi) How could you reduce the number of expansions that the DFS algorithm requires to find the goal? What is the lowest number of cell expansions you could achieve with DFS until the agent finds the goal? Explain your solution. - Repeated expansions can be reduced by creating a visited hashset and appending each visited position to the set.