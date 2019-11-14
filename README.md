# Movie-Ranking

# What does this do?
This software takes a list of rankings and executes 25 rounds of [Schulze Method Electoral Voting](https://en.wikipedia.org/wiki/Schulze_method) in order to produce a final list of Condorcet winners

# How does it work?
1. The lists are loaded as ballots, in which number 1 is first choice, 2 is second, and so on.
2. The Schulze method is executed, each candidate competes against every other candidate and a pair-wise winner is calculated
*"How many people prefer movie x to movie y?"*
3. When all candidates have competed against every other candidate, the strongest is considered the winner
4. The winner is removed from all lists and then the Schulze method is executed until no more candidates remain, the winner of each of these *master rounds* is then the next on the master list.

# What if there's a draw?
Picks them at random I think 👀

# To do
Joint positions for candidates that draw with one another. Removing the random choice as a winner for the next round affects the future ordering of candidates, in this case, the drawing winners should all be given the same ranking and all be removed.
