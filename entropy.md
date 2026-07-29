## Entropy Formula Explanation
The inspiration for this homework is that **ID3 algorithm** uses entropy to train *decision-tree models*.

Entropy is a measure of the level of impurity, randomness, or disorder within a dataset in this context.

The formulation of data entropy is like this:
```math
H(X) = - \sum_{i=1}^{n} \mathbb{P}(X=i) \log_2 \mathbb{P}(X=i)
```
## Amount of information related to an event
Let $X$ any event with probability $\mathbb{P}(X)$, we define the amount of the information of $X$ as:
```math
I(X)=\log_2 (\frac{1}{\mathbb{P}(X)})=-\log_2 \mathbb{P}(X)
```
1. Why is $\frac{1}{\mathbb{P}(X)}$ used?
2. Why $log_2$?
### Role of $\frac{1}{\mathbb{P}(X)}$
A *fundamental principle of information theory* is: the **lower the probability of an event, the greater the amount of information it conveys when it occurs**.
So, an event with a high probability of occurring provides little information because its occurrence is expected. In contrast, an event with a low probability of occurring provides a large amount of information because its occurrence is surprising.
So, with the next equation
```math
\frac{1}{\mathbb{P}(X)}
```
When $\mathbb{P}(X)$ is large, then the amount of information is small. On the other hand, if $\mathbb{P}(X)$ is small, then $\frac{1}{\mathbb{P}(X)}$ becomes large.

### Role of $log_2$
In information theory, the information content of independent events is additive; the information obtained from two independent events occurring together is equal to the sum of the information provided by each event individually.
Notice that the logarithmic function transforms products into sums:
```math
\log(ab) = \log(a) + \log(b)
```
Which is consistent with the additive property of information for independent events.
Additionally, computers store information using bits. Therefore, the base two in the logarithm reflects the fact that a bit has two possible states and measures information in units of bits. For this reason, the amount of information is commonly measured using the logarithm base two.

## Definition of the entropy
Now we can define the information content of an entire random variable.
Since a random variable may produce different outcomes with different probabilities, the amount of information obtained is itself a random quantity.

Therefore, a natural measure of the uncertainty associated with the random variable is the expected amount of information produced by its outcomes.
This expected information is called the entropy of the random variable $X$ and is defined as
```math
H(X)=\mathbb{E}[I(X)]=- \sum_{i=1}^{n} \mathbb{P}(X=i) I(X)= - \sum_{i=1}^{n} \mathbb{P}(X=i) \log_2 \mathbb{P}(X=i)
```
So the entropy measures the average amount of information associated with the outcomes of the random variable $X$.