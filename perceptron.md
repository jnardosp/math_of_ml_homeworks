## Perceptron

The perceptron is the simplest type of **artificial neural network**. Is a type of **linear classifier** which makes its predictions based on:
- A set of input signals.
- A set of weights (each one associated with an input signal).
- A bias term.
- An activation function.

In the most classical perceptron we will use the **step activation function** so the perceptron will look like this:

$$f(x) = \begin{cases}
 1 & \text{if }w^\top x + b \geq 0 \\
  0 & \text{else} \end{cases}$$

This is a pseudocode for the implementation:
```
Algorithm: Perceptron Learning Algorithm
P <- inputs with label 1;
N <- inputs with label 0;
initialize w randomly;

while !convergence do
    Pick random x ∈ P or N;
    if x ∈ P and sum(w,x) < 0 then
        w = w + x;
    end
    if x ∈ N and sum(w,x) >= 0 then
       w = w - x;
    end
end
//the algorithm converges when all inputs are classified correctly.
```

### The **exercise 1.3** states that:
The weight update rule has the nice interpretation that it moves in the direction of classifying x(t) correctly.

**a) Show that $ y(t)w^\top(t)x(t) < 0 $ [Hint: $x(t)$ is misclassified by $w(t)$].**

**b) Show that $ y(t)w^\top(t+1)x(t) > y(t)w^\top(t)x(t)$.**

**c) As far as classifying $x(t)$ is concerned, argue that the move from w(t) to w(t+1) is a move 'in the right direction'.**

Remember $y(t)$ will be the label for input $x(t)$, perceptron **predicts**:

$$f(x) = \begin{cases}
 1 & \text{if }w^\top x + b \geq 0 \\
 0 & \text{if }w^\top(t)x(t) < 0 \end{cases}$$

### When **$y(t)w^\top(t)x(t) < 0$**?

| True Label $y(t)$ | Condition on $w^\top(t)x(t)$ | Product $y(t)w^\top(t)x(t)$ | Interpretation |
|---|---|---|---|
| $+1$ (positive) | $< 0$ | Negative | Misclassified as negative |
| $0$ | Nothing | Nothing | $y(t)w^\top(t)x(t) < 0$ will never occur |

So when $y(t) = 1$ and the perceptron is misclassifying it we update the weight.

Notice that $w(t+1) = w(t) + x(t)$ so in $t+1$ we will have:

$$\begin{aligned}
w(t+1)^\top x &= [w+x]^\top x \\
            &= w^\top x + x^\top x \\
            &= w^\top x + ||x||^2
\end{aligned}$$

Because $||x||^2$ is always positive: $$w(t+1)^\top x > w(t)^\top x$$ moving the decision boundary in the positive direction. *(This will always happen in the positive misclassification case, in the negative we would need a (-1, 1) perceptron)*.

### Case **$w^\top(t)x(t) \geq 0$**:

The argument is similar, if $x \in N$ and **$w^\top(t)x(t) \geq 0$** then x is misclassified as positive.

So we update the weight $ w(t+1) = w(t) - x $ like:

$$\begin{aligned}
w(t+1)^\top x &= [w-x]^\top x \\
            &= w^\top x - x^\top x \\
            &= w^\top x - ||x||^2
\end{aligned}$$

We move the decision boundary in the negative direction, moving the hiperplane in the right direction.