## Netflix Challenge Solution
The 2007 Netflix challenge was focused on predicting movie rating behaviour to upgrade movie recommendation systems.

First place winner method is described on "***KDD Cup 2007 Task 1 Winner Report***" co-authored by *Miklós Kurucz*, we explore the methods described here and its relationship with non-negative matrix factorization.

### Task problem
The task was predicting the probability that a user rated a movie in 2006 for a given list of 100.000 user/movie pairs of the Netflix Prize dataset. None of the pairs selected for the KDD Cup were rated in the training set, meaning they would have to estimate that a movie was (1) or wasn't (0) rated, the evaluation metric was RMSE (Root Mean Squared Error).

### What they used
* *SVD based recommendation*: Using the full 0-1 matrix of all known ratings; the rank k *Singular Value Decomposition* (SVD) approximation will yield a prediction. There is a theorem to find the best approximation with respect to the Frobenius norm, and the Frobenius norm will be the RMSE for the prediction of existing a rating on a movie (Only while user-movie pairs are selected uniform randomly), they ultmately implement Lanczos code from svdpack.

* *Item-item similarity based recommendation*: This recommender computes the adjusted cosine similarity based on not just 1 value of the matrix but a range of 5 ratings in the matrix. So an unrated movie $j$ is recommended to a given user $i$ based on the weighted average of the nearest $K$ movies $j'$ to $j$ rated by the user.

* *Association Rules in Sequences*: They used association rules via frequent sequences in the sets of movies rated by a user ordered by the time of the rating using an APRIORI algorithm. Restricted to movies with less than or equal to 50k ratings and users that gave less than or equal to 3k ratings; because of CPU time constraints they got rules that matched only 20k of the 100k user-movie pairs.

After having all predictions they *combined them* using the *linear regression method* of the ML toolkit Weka, obtaining an equation as the final prediction that gets a RMSE of 0.256.

### Relationship with PMF (Positive Matrix Factorization)

The SVD method used on this article is a particular case of matrix factorization with low range, this is the conceptual base of PMF.

The article shows clearly that low range matrix factorization with methods like SVD is an effective component to predict existence of ratings, posterior methods like PMF will include:
* Non negativity increasing interpretability
* Probabilistic methods to take care of uncertainity (PMF models the noise variance)
* PMF models only the observed data. Doesn't treat missing entries as 0; instead treats them as unobserved random vars.