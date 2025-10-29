#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

def solve_for_p(p):
    V = np.zeros((5,4))
    x_star = np.zeros((4,3))
    y_star = np.zeros((4,3))

    V[4,:] = 1.0  # walk
    V[:,3] = 0.0  # strikeout

    for s in range(2,-1,-1):
        for b in range(3,-1,-1):
            A = V[b+1,s]
            B = V[b,s+1]
            D = 4*p + (1-p)*B

            denom = p*(4 - B) + (A - B)
            if abs(denom) < 1e-12:
            # Degenerate case: all columns equal, take average
                y = 0.5
            else:
                y = (A - B) / denom
                x = y
            if 0 <= x <= 1:
                # mixed equilibrium
                V[b,s] = (
                    (1-x)*(1-y)*A
                    + ((1-x)*y + x*(1-y) + x*y*(1-p))*B
                    + 4*p*x*y
                )
            else:
                # pure equilibrium
                # pitcher chooses row minimizing column maxima
                if max(A,B) <= max(B,D):
                    # pitcher throws ball
                    if A >= B:
                        y = 0; V[b,s] = A
                    else:
                        y = 1; V[b,s] = B
                else:
                    # pitcher throws strike
                    if B >= D:
                        y = 0; V[b,s] = B
                    else:
                        y = 1; V[b,s] = D
                x = 0 if max(A,B) <= max(B,D) else 1

            x_star[b,s] = x
            y_star[b,s] = y

    # compute probability of reaching (3,2)
    r = np.zeros((5,4))
    r[3,2] = 1.0
    r[4,:] = 0.0
    r[:,3] = 0.0

    for s in range(2,-1,-1):
        for b in range(3,-1,-1):
            if (b,s)==(3,2): continue
            x = x_star[b,s]; y = y_star[b,s]
            r[b,s] = (
                (1-x)*(1-y)*r[b+1,s]
                + ((1-x)*y + x*(1-y) + x*y*(1-p))*r[b,s+1]
            )
    return r[0,0]

def find_optimal_q():
    best_q, best_p = -1, 0.5
    for p in np.linspace(0,1,1001):
        q = solve_for_p(p)
        if q > best_q:
            best_q, best_p = q, p
    return best_p, best_q

p_star, q_star = find_optimal_q()
print(f"p* = {p_star:.10f}")
print(f"q_max = {q_star:.10f}")


# In[ ]:




