## Convex Optimization Problem on Support Vector Machines

We have this convex optimization problem related to the training of a Support Vector Machine:

$$\text{Min: } \Vert w \Vert$$
$$\text{S.T  } y_{i}(wx_{i}-b) \geq 1\; \forall i = 1, ..., N$$

Remember for hard-margin SVMs we have that:
If the data is linearly separable, we can select **two parrallel hyperplanes** that separate the 2 classes of data, so that the distance between them is as large as possible.

With a normalized dataset, these hyperplanes are described by:

$$
\begin{cases}
    w^{\top} x - b = 1\; \text{(anything on or above this boundary with label 1)} \\
    w^{\top} x - b = -1\; \text{(anything on or below this boundary with label 0)} \\
\end{cases}
$$

Geometrically, the distance between these 2 hyperplanes is: $\frac{2}{\Vert w \Vert}$.

So to maximize the distance between the planes we want to minimize $\Vert w \Vert$.

The **w** and *b* that solve this problem determine the final classifier:

$$x \mapsto sgn(w^\top x - b)$$

### Why is it **Convex**?
For an optimization problem to be convex, we need to minimize a **convex objective function over a convex set**.

Remember convex definition, a function $f: {\rm I\!R}^n \mapsto {\rm I\!R}$ is convex if for any 2 points u, v in its domain and any $\lambda \in [0,1]$:

$$f(λu+(1−λ)v)≤λf(u)+(1−λ)f(v).$$

Checking **Euclidean norm** $\Vert w \Vert$

Take any 2 vectors $w_{1}, w_{2} \in {\rm I\!R}^n$ and any $\lambda \in [0,1]$.

We have the **triangle inequality**:

$$​∥λw_{1}​+(1−λ)w_{2}​∥​≤∥λw_{1}​∥+∥(1−λ)w_{2}​∥$$

Which is exactly the convexity inequality, so the ***objective function is convex***.

Checking if constraint is a **convex set**

Each constraint $y_{i}​(w⋅x_{i}​−b)≥1$ can be rewritten as:

$$1−y_{i}​(w⋅x_{i}​−b)≤0$$

The left-hand side is actually an **affine function**, as it can be rewritten as $(y_{i}​x_{i}​)⋅w−y_{i}​b$ and affine functions are both **convex and concave**. The intersection of convex is convex (for all N inequalities), so the constraint is a **convex set**.

So we have a convex optimization problem.

### Lagrange Multipliers

We can solve this problem:

$$\text{Min: } \Vert w \Vert$$

as this equal problem:

$$\text{Min: } f(w)=\frac{1}{2}\Vert w \Vert^2$$

$$\text{S.T :} \;1 - y_{i}(wx_{i}-b) \leq 0\; \forall i = 1, ..., N$$

Through Lagrange Multipliers method we introduce a Lagrange multiplier $\alpha_i \geq 0$  for each constraint.

The Lagrangian is:

$$L(w, b,\alpha)=\frac{1}{2}\Vert w \Vert^2+\sum_{i=1}^{n}\alpha_{i} \:[1-y_{i}(w^\top x_{i}-b)]$$

### Karush-Kuhn-Tucker (KKT) Conditions

We use KKT conditions to find the minimum. Partial derivatives of L with respect to primal variables $w,b$ and set them to zero:
* With $w$ variable:

  $$\nabla_{w}L=w  - \sum_{i=1}^{n} \alpha_i y_i x_i = 0 \Rightarrow w = \sum_{i=1}^{n} \alpha_i y_i x_i $$
  Which shows that the optimal weight vector is a linear combination of the training examples.

* With $b$ variable:

  $$\frac{\partial L}{\partial b} = - \sum_{i=1}^{n}\alpha_i y_i = 0 \Rightarrow \sum_{i=1}^{n}\alpha_i y_i = 0$$

### Dual problem
1.  Substitute $w = \sum \alpha_i y_i x_i$ into $\frac{1}{2}\|w\|^2$:

    $$\frac{1}{2} \left( \sum_i \alpha_i y_i x_i \right) \cdot \left( \sum_j \alpha_j y_j x_j \right) = \frac{1}{2} \sum_i \sum_j \alpha_i \alpha_j y_i y_j (x_i \cdot x_j)$$

2.  Substitute into the constraint term:

    $$\sum_i \alpha_i - \sum_i \alpha_i y_i (w^T x_i + b) = \sum_i \alpha_i - \sum_i \sum_j \alpha_i \alpha_j y_i y_j (x_i \cdot x_j) - b \sum_i \alpha_i y_i$$

Since $\sum \alpha_i y_i = 0$. Resulting **Dual Objective Function** $Q(\alpha)$ is:

$$Q(\alpha) = \sum_{i=1}^{N} \alpha_i - \frac{1}{2} \sum_{i=1}^{N} \sum_{j=1}^{N} \alpha_i \alpha_j y_i y_j (x_i^T x_j)$$

### Quadratic Programming (QP)
Instead of minimizing over $w$, we **maximize** the dual function $Q(\alpha)$ subject to:
1.  $\sum_{i=1}^{N} \alpha_i y_i = 0$
2.  $\alpha_i \geq 0$ for all $i = 1, \dots, N$

This is a **Quadratic Programming (QP)** problem. Often solved using algorithms like **Sequential Minimal Optimization (SMO)**.