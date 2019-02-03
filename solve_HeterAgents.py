# Computational Method
# developed by Winberry (2016), "A Toolbox for Solving and Estimating Heterogeneous Agent Macro Models."
# Step 1: Approximate value function & distribution using finite-dimensional global approximations w.r.t. individual state variables
# Step 2: Compute the stationary eqm. of the finite-dimensional model (no agg. shocks, have idiosyncratic shocks)
# Step 3: Compute the agg. dynamics of th finite-dimensional model using Taylor expansion around the stationary eqm.

# Take Krusell-Smith Model as an example
# The model is described briefly as following: There is a continuum of households with preferences over consumption.
# Each household supplies epsilon_{jt} efficiency units of labor, which distributed independently across hh, but within hh follows a two-state Markov Chain with a constant transition probability.
# HH can only trade in capital s.t. borrowing constraint.
# Representative firm produces. There's aggregate productivity shock, which follows AR(1)

