## Perceptron

The perceptron is the simplest type of **artificial neural network**. Is a type of **linear classifier** which makes its predictions based on:
- A set of input signals.
- A set of weights (each one associated with an input signal).
- A bias term.
- An activation function.

In the most classical perceptron we will use the **step activation function** so the perceptron will look like this:
$$f(x) = \begin{cases} 1 & \text{if }w^\top x + b > 0 \\ 0 & \text{else} \end{cases}$$

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