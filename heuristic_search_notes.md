(a) Fill in the implementation in heuristic search.py. The relevant places in the code are indicated by TODO comments. The file contains detailed comments for the classes and functions that you will have to use to do so. Include comments, explaining what you did, and (if not obvious) why it is correct! 

(b) Justify, on paper, whether the heuristic is actually admissible or not. If admissible, provide a formal argumentation why this is so. If not admissible, provide a counter example showing why it is not.

(i) The maximal Manhattan distance between the agent’s current location to any coin that has not been collected. Formally, h1(s) = maxc∈C\Cs d(⟨sx,sy⟩,⟨cx,cy⟩). To use h1 in the script, append--heuristic ManhattanMax to the command line parameters. 

(ii) The sum of the Manhattan distances to all coins that have not been collected. Formally, h2(s) = ∑︁ c∈C\Cs d(⟨sx,sy⟩,⟨cx,cy⟩). To use h2 in the script, append--heuristic ManhattanSum to the command line parameters. 

(iii) Let C \ Cs = {c1,...,cn}, and assume that c1,...,cn are ordered so that: 

(1) for all 1 < i ≤ n, it holds that d(⟨sx,sy⟩,⟨c1 x,c1 y⟩) ≤ d(⟨sx,sy⟩,⟨cix,ci y⟩),

(2) for all 1 ≤ i < n and i + 1 < j ≤ n it holds that d(⟨cix,ci y⟩,⟨ci+1 x ,ci+1 y ⟩) ≤ d(⟨cix, ci y⟩, ⟨cj x, cj y⟩). The heuristic is given by h3(s) = d(⟨sx,sy⟩,⟨c1 x,c1 y⟩) + ∑︁n−1 i=1 d(⟨cix, ci y⟩, ⟨ci+1 x ,ci+1 y ⟩). To use h3 in the script, append--heuristic ManhattanOrderedSum to the command line parameters. 

(iv) Come up with and implement an arbitrary other heuristic with the following properties: 

(1) Your heuristic is admissible. Justify why it is admissible (on paper)! 

(2) Your heuristic (and implementation) works for arbitrary maps, arbitrary initial positions, arbitrarily many coins, and arbitrary coin locations. 

(3) For the map, initial agent location, and coins as shown in Figure 1, A∗ with your heuristic expands less than 5000 states (less than about 50% of the states expanded by breadth-first search). To use your heuristic in the script, append--heuristic CallMeFancy to the command line parameters.