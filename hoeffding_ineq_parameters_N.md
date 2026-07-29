## Hoeffding inequality parameters $\epsilon$ and $\delta$ control N
We defined Hoeffding's inequality as:
```math
  \mathbb{P}(|E_{in}-E_{out}| ≥ \epsilon) ≤ 2Me^{-2N\epsilon^{2}}
```
With $E_{out}$ being the model's true error on new data and $E_{in}$ being the model's error on the training data.

We want to determine which parameter is best to control in order to manage the amount of data required for the inequality to hold ($N$). We have:
*   A desired precision $\epsilon$
*   A hypothesis set size $M$
*   A failure probability $\delta$

Then, if we require the failure probability to be at most $\delta$, we have:
```math
  2Me^{-2N\epsilon^{2}} ≤ \delta
```
Solving for $N$, we obtain:
```math
  e^{-2N\epsilon^{2}} ≤ \frac{\delta}{2M}
```
Then,
```math
  2N\epsilon^{2} ≥ \ln(\frac{\delta}{2M})
```
So:
```math
N ≥ \frac{1}{2\epsilon^{2}} \ln(\frac{\delta}{2M})
```
So $N$ **depends quadratically on $1/\epsilon$ and logarithmically on $1/\delta$**. Therefore, small variations in $\epsilon$ produce much larger changes in $N$ than comparable variations in $\delta$.

Example:
* If $\epsilon$ is halved, then
```math
  N ≥ \frac{1}{2(\frac{\epsilon}{2})^{2}} \ln(\frac{\delta}{2M}) = N ≥ \frac{2}{\epsilon^{2}} \ln(\frac{\delta}{2M})
```
the amount of data required would double.
* If we compare $\delta = 1/10$ and $\delta = 1/100$, then $\ln(10) = 2.3$ and $\ln(100) = 4.6$.
We see that the associated term merely doubles, even though $\delta$ is reduced tenfold.

We conclude that it is **more feasible to control the value of $\epsilon$** than that of $\delta$.