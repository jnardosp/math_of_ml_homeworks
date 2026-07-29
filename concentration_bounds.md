## Concentration bounds
They are probabilistic inequalities that quantify how likely a random variable is to deviate from a specific expected value. We explore three fundamental concentration inequalities: 
## Markov's inequality
Let $X$ a continuous random variable, its expected value is defined as:
```math
\mathbb{E}[X]=\int_{0}^{\infty} Xf_{X}(X) dX
```
If we have a constant $\alpha > 0$. Then
```math
\mathbb{E}[X]=\int_{0}^{\infty} Xf_{X}(X) dX ≥ \int_{\alpha}^{\infty} Xf_{X}(X) dX
```
We observe that if we fix $X$ as $X≥\alpha$, then we always get the following inequality
```math
\mathbb{E}[X] ≥ \int_{\alpha}^{\infty} \alpha f_{X}(X) dX
```
We can rewrite it as:
```math
\mathbb{E}[X] ≥ \int_{\alpha}^{\infty} \alpha f_{X}(X) dX = \alpha \int_{\alpha}^{\infty} f_{X}(X) dX = \alpha \mathbb{P}(X>=\alpha)
```
Finally, we obtain Markov's inequality:
```math
\frac{\mathbb{E}[X]}{\alpha} ≥ \mathbb{P}(X≥\alpha)
```
## Chebyshev's inequality
Let $X$ a continuous random variable and Markov's inequality such that:
```math
\frac{\mathbb{E}[X]}{\alpha} ≥ \mathbb{P}(X≥\alpha)
```
If we have the inequality $\mathbb{P}(X≥\alpha)$, then $\mathbb{P}(X^{2}≥\alpha^{2})$ holds. Moreover, given that $X$ is a continuous random variable, we know that $X-\mathbb{E}[X]$ is a continuous random variable too.
We can define the next probability such that:
```math
\mathbb{P}((X-\mathbb{E}[X])^{2}≥\alpha^{2})
```
Now, using Markov's inequality
```math
\mathbb{P}((X-\mathbb{E}[X])^{2}≥\alpha^{2}) ≤ \frac{\mathbb{E}[(X-\mathbb{E}[X])^{2}]}{\alpha^{2}}
```
Remember the variance of a continuous random variable is defined as $Var[X]=\mathbb{E}[(X-\mathbb{E}[X])^{2}]$. Then, we obtain Chebyshev's inequality such that
```math
\mathbb{P}(|(X-\mathbb{E}[X])|≥\alpha) ≤ \frac{Var[X]}{\alpha^{2}}
```
## Hoeffding's inequality
Let $(X_1, X_2, \dots, X_n)$ be independent random variables satisfying $a_i ≤ X_i ≤ b_i$,
and define 
```math
\mu_i = \mathbb{E}[X_i]
```
Our goal is to bound the probability
```math
\mathbb{P}\left(\sum_{i=1}^{n}(X_i-\mu_i) ≥ t\right)
```
For any $\lambda > 0$
```math
\mathbb{P}\left(\sum_{i=1}^{n}(X_i-\mu_i)≥ t\right)=\mathbb{P}\left(e^{\lambda\sum_{i=1}^{n}(X_i-\mu_i)}≥ e^{\lambda t}\right)
```
Applying Markov's inequality to the exponential yields
```math
\mathbb{P}\left(\sum_{i=1}^{n}(X_i-\mu_i)≥ t\right)≤e^{-\lambda t}\mathbb{E}\left[e^{\lambda\sum_{i=1}^{n}(X_i-\mu_i)}\right]
```
Since the random variables are independent,
```math
\mathbb{E}\left[e^{\lambda\sum_{i=1}^{n}(X_i-\mu_i)}\right]=\prod_{i=1}^{n}\mathbb{E}\left[e^{\lambda(X_i-\mu_i)}\right]
```
Then,
```math
\mathbb{P}\left(\sum_{i=1}^{n}(X_i-\mu_i)≥ t\right)≤e^{-\lambda t}\prod_{i=1}^{n}\mathbb{E}\left[e^{\lambda(X_i-\mu_i)}\right]
```
We assumed Hoeffding's lemma so if a random variable $(X)$ satisfies $a ≤ X ≤ b$, then
```math
\mathbb{E}\left[e^{\lambda(X-\mathbb{E}[X])}\right]≤\exp\left(\frac{\lambda^2(b-a)^2}{8}\right)
```
Applying the lemma to each $(X_i)$,
```math
\mathbb{E}\left[e^{\lambda(X_i-\mu_i)}\right]≤\exp\left(\frac{\lambda^2(b_i-a_i)^2}{8}\right)
```
Therefore,
```math
\prod_{i=1}^{n}\mathbb{E}\left[e^{\lambda(X_i-\mu_i)}\right]≤\exp\left(\frac{\lambda^2}{8}\sum_{i=1}^{n}(b_i-a_i)^2\right)
```
Substituting into the previous inequality gives
```math
\mathbb{P}\left(\sum_{i=1}^{n}(X_i-\mu_i)≥ t\right)≤\exp\left(-\lambda t+\frac{\lambda^2}{8}\sum_{i=1}^{n}(b_i-a_i)^2\right)
```
Now, we have to optimize with respect to $\lambda$. Therefore,
```math
\mathbb{P}\left(\sum_{i=1}^{n}(X_i-\mu_i)≥ t\right)≤\exp\left(-\frac{2t^2}{\sum_{i=1}^{n}(b_i-a_i)^2}\right)
```
This is the one-sided version of Hoeffding's inequality.
To obtain the two-sided Hoeffding inequality, we have to apply the same argument to $(-X_i)$ gives
```math
\mathbb{P}\left(\sum_{i=1}^{n}(X_i-\mu_i)≤ -t\right)≤\exp\left(-\frac{2t^2}{\sum_{i=1}^{n}(b_i-a_i)^2}\right)
```
Using the union bound, we obtain
```math
\mathbb{P}\left(\left|\sum_{i=1}^{n}(X_i-\mu_i)\right|≥ t\right)≤2\exp\left(-\frac{2t^2}{\sum_{i=1}^{n}(b_i-a_i)^2}\right)
```
which is the classical two-sided Hoeffding inequality.