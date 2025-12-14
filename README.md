# Robot Baseball – Markov Game

Mathematical and computational model of the **Robot Baseball** problem (Jane Street Monthly Puzzle - October 2025)

The game is modeled as a **stochastic zero-sum Markov game** between a pitcher and a batter, using **optimal mixed strategies** to:
- Compute the probability of reaching a full count (3 balls, 2 strikes).
- Find the optimal value of `p` (home run probability) that maximizes this probability.

## Contents
- Model formulation and Bellman equations
- Mixed-strategy equilibrium
- Recursion for full-count probability
- Numerical optimization of `p`

## Key result
- `p* ≈ 0.227`
- Maximum full-count probability ≈ **29.6%**

## Author
Antón Seijo Barrio
