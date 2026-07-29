## Hypothesis set of KNN & training algorithm
This ML algorithm is particular because it doesn't build a model from the data, instead it stores all the data in order to compare the existing information with new entering information. 

## Hypothesis set
This set includes all the functions that assign a label to each data point based on the $k$ training samples closest to the point being labeled, using a distance metric.
### Classification
This is the form a hypothesis takes. So, we have
```math
h_{D}=mode\{y_{i} | x_{i} \in N_{k}(x)\}
```
where 
* $D$:=set of the training data
* $N_{k}(x)$:=set of the $k$ nearest neighbours to x
* $mode$:=classifies the data using the most frequent labels among its neighbors

Then, hypothesis set for classification problems is:
```math
H=\{h_{D} | h_{D}=mode\{y_{i} | x_{i} \in N_{k}(x)\}\}
```

## Learning algorithm
We can divide the algorithm's construction into two parts:
1. **Training phase**
    * The number of k-neighbors must be determined
    * A distance metric must be established to provide a standard measurement for all data
    * All training data must be stored

 2. **Prediction phase**
    * The distance between the new data point and all previously stored data points is calculated
    * the k nearest data points are selected
    * The new data point is classified; if it is a classification problem, the majority class is chosen, whereas if it is a regression problem, the average of the neighbors' values ​​is calculated

This homework provides a good explanation of the most basic instance-based algorithm.