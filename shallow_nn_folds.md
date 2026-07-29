## Folds of a shallow NN
We defined a shallow neural network is a function
```math
y = f[\mathbf{x}, \boldsymbol{\phi}]
```
with parameters $\boldsymbol{\phi}$ that maps an input vector $\mathbf{x}$ to an output $y$.
For the one-dimensional example shown in Section 3.1, the network is defined as

* $y = \phi_0$
* $\phi_1 = a[\theta_{10}+\theta_{11}x]$
* $\phi_2 = a[\theta_{20}+\theta_{21}x]$
* $\phi_3 = a[\theta_{30}+\theta_{31}x]$

with:

- $\phi_0$ as the output bias
- $\phi_1$, $\phi_2$, $\phi_3$ are the output weights
- $\theta_{i0}$ are hidden layer biases
- $\theta_{i1}$ are hidden layer weights
- $a[\cdot]$ as the activation function

The hidden units are
```math
h_i(x) = a[\theta_{i0}+\theta_{i1}x]
```
In this example the activation function is the ReLU,
```math
a[z] = \text{ReLU}(z)=\begin{cases} 0, & z < 0, \\ z, & z \ge 0 \end{cases}
```

### Origin of the folds
The folds/junctions are the transition point of each hidden neuron between its inactive and active states. A hidden neuron changes behavior when its pre-activation becomes zero:
```math
\theta_{i0}+\theta_{i1}x=0
```
Solving for $x$ gives the location of the junction:
```math
x_i=-\frac{\theta_{i0}}{\theta_{i1}}
```
For values of $x$ smaller than this threshold,
```math
h_i(x)=0
```
while for larger values,
```math
h_i(x)=\theta_{i0}+\theta_{i1}x
```
Therefore, each hidden unit introduces a point where the slope of the function changes.

### Geometric Interpretation
A **shallow neural network with ReLU activations represents a piecewise linear function**. The following ideas are key to understanding shallow networks geometrically.

- Each hidden neuron contributes with one fold.
- Between two consecutive folds, the network behaves as a linear function.
- The expressive power of the network increases with the number of hidden neurons because more junctions can be created.

Thus, the junctions in a shallow neural network originate from the activation boundaries of the hidden ReLU units.