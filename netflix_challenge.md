## Netflix Challenge Solution
The 2007 Netflix challenge was focused on predicting movie rating behaviour to upgrade movie recommendation systems.

First place winner method is described on "***KDD Cup 2007 Task 1 Winner Report***" co-authored by *Miklós Kurucz*, we explore the methods described here and its relationship with non-negative matrix factorization.

### Task problem
The task was predicting the probability that a user rated a movie in 2006 for a given list of 100.000 user/movie pairs of the Netflix Prize dataset. None of the pairs selected for the KDD Cup were rated in the training set, meaning they would have to estimate that a movie was (1) or wasn't (0) rated, the evaluation metric was RMSE (Root Mean Squared Error).

### What they used

### Relationship with PMF (Positive Matrix Factorization)