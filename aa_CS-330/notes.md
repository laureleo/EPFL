# TODO
Group
Notes
Exercises

# Lecture 1 Greediness
## Greedy algorithms
Algorithms that take the option that currently seem the best and then moving on.

If a problem can be stated as a matroid it can be optimally solved by a greedy algorithm.
## Graph theory basics
Given an acyclic graph G={V,E}, several properties hold.
1. A subset of acyclic edges is itself acyclic.
2. For two acyclic edge sets A, B on the same vertex set V, |A| > |B| ==> There exists an e belonging to A\B such that B + e is acyclic.
3. The tree consists of |V| - 1 edges

A minimum spanning tree is a set {E2} of edges such that their collective weight is the lowest possible. Two algorithms for creating a minimal spanning trees are Prims algorithm and Kruskals algorithm

### Prims algorithm
A greedy algorithm applied to the minimal/maximal weighed tree problem.

* Starting from a vertex, go to the edge with the highest weight.
* From all currently available edges, pick the one with highest weight (as long as no cycles are created)
* Continue unil no more edges can be added.

Easy to understand. Not optimal. Does not generalize well to other problems
### Kruskal's algorithm
A greedy algorithm that can be applied to the minimal/maximal weighed tree problem.
* Sort all edges.
* Select the first (heaviest) edge.
* Continue selecting the heaviest edge you can from the list until done.

**runtime** Theta(Mergesort) = (|E|log|E|), since the sorting of the list dominates since checking for cycles can be done with Union-Find, which runs in Theta(|E|)

#### PROOF OF OPTIMALITY
Theorem: Kruskals algorithm returns a minimal-weight spanning tree on a connected graph.

Lemma: Kruskals algorithm returns a forest F
1. By definition the algorithm starts from a forest F and only adds edges in such a way that no cycles are created. Thus it creates a forest.

Lemma: The resulting forest F is a single spanning tree.
1. Assume that it is not. Then the resulting graph G2 consist of at least two components.
2. Since the original graph was connected there must exist at least one edge e in G not in G2 that connects the two components.
3. Since connecting components does not create cycle, the existence of such an e cannot exist.

Lemma: The single spanning tree F is of minimal weight.
???

## Union-Find
Union-find is a data structure that keeps track of a set of elements partitioned into disjoint sets.

It allows for two operations, Union and Find.
* Union is used to join disjoint set
* Find for checking if elements belong to the same subset.

In the context of this course the most important application is in Kruskals algorithm.

The (possibly incorrect) intuition can be thus:

* For each new edge (u,v).
* Check if u, v is already part of a set (IF (find(u) AND find(v)))
* If true addition of the edge will cause a cycle.

If it comes up again could be worth to check the data structure in more detail.
## Linear Algebra 
**Vector space:** A set of vectors V, for example the set of nx1 column matrices.

**Span:** The set of all possible linear combinations of a set of vectors (Addition and scaling)

**Basis:** A linearly independent set of vectors that span V.

**Dimension** The size of the basis.

## Matroids
A type of mathematical object that can be solved optimally with greedy algorithms.
### Definition
In the context of independent sets the definition is based on the following two axioms:

A matroid is a matematical object M = (S, I) such that:
* S is the ground set, for example the set of edges in a graph or a set of vectors in space
* I is a set of subsets of S satisfying two axioms. I is known as the independent set.

> **Axiom 1** If X ⊆ Y and Y ∈ I then X ∈ I. This is the heridetary property.

> **Axiom 2** If X and Y ∈ I and |Y| > |X|, then ∃e ∈ Y \ X : X ∪ {e} ∈ I. This is the exchange property.

### Examples
Define I = {T⊆ E : T is acyclic}.
* It satisfies axiom 1 since a subset of a an acyclic set of edges is also acyclic.
* It satisfies axiom 2 since a tree with k edges has n-k components.

## Terminology
* Independent set: A nonempty set of subsets where all subsets recursively fulfill the same property.
* Extension: An element that you can add to an independent set without violating its independency property
* Maximal: A independent set that has no extensions/Isn't a subset of another independent set
* Base: A base for a matroid is a maximum cardinality set.

# Lecture 2 Matroid Intersection and Bipartite Matchings
When the matroid works and when it does not

## Axioms
A matroid is a structure M = (E, I) where the following two examples hold true
1. If X is a subset of Y and Y belongs to I, then X belongs to I as well.
2. If X, Y ∈ I AND |X| > |Y| then there exist an  e ∈ X\Y such that e ∪ Y belongs to I

## Matroid Algorithm
Given a matroid M = (S, I)

The process of solving the matroid is as follows:
0. Solution = ∅ 
1. Sort all edges according to weight.
2. For each element s in S, taken in decreasing order of weight:
3.  If Solution ∪ s ∈ I, keep it, else continue
4. Return Solution

## Correctness of Algorithm
### Lemma: The algorithm preserves the independence property
The final set will be an independent set.

1. The emtpy set is independent.
2. Each iteration preserves the independency of the current set
3. By induction the final solution is an independent set.

### Lemma: Matroids exhibit the greedy-choice property
If the algorithm selects an x, that x is part of the optimal independent set.

1. Let A be the set formed by adding x to the empty set.
2. Let B be a hypothetical optimal set which DOES NOT contain x
> Proving that weight(A) >= weight(B) is the key to proving this property, that x is indeed optimal.
3. If so then weight(x) is bigger than any weight(y) belonging to B.
> This is because of the first axiom. Any subset of B is a independent subset of B.
> Thus any y in B is a independent element which the algorithm would have considered when it selected x.
> Thus weight(x) must be >= weight(y), otherwise that element would have been selected by the algorithm.
4. The rest of the elements can simply be taken from B
> This is because of the second axiom. since A, B belong to I, |B| > |A| we know that there exist an element in B which can be added to A such that A is still a solution.
> This process can be repeated until A and B are of the same cardinality
5. Since A and B contain exactly the same elements apart from x and y, A is an optimal solution.
> More concretly, weight(A) = weight(B) - weight(y) + weight(x).
> weight(x) >= weight(y)
6. In conclusion, the matroid algorithm selects an optimal element when it is run.

### Lemma: Matroids exhibit the optimal sub-structure property (Check book)

## Proof of failure when no Downward closure
## Proof of failure when no Heredity
## Matroid intersection
Any problem that can be described as the intersection of two matroids have an efficient solution (polynomial)

Given two matroids M1, M2 defined on the same ground set E, the intersection of the two matroids is defined as M1 ∩ M2 = (E, I1 ∩ I2)

For the classic example of matroid intersection, bipartite matching, you can define a matroid for both partition A and B.

I1 will contain all possible matchings for A, I2 will contain all possible matchings for B.

F belonging to the intersection of I1 and I2 will be the set of all solutions that are full matchings, and thus solutions.
### THEOREM Edmond
There is an efficient (polynomial) algorithm for finding a max-weight independent set in the intersection of two matroids.

What efficient means in this time is that any subset can be checked for beloning to the independent set in polynomial time.

This is important because while matroids can be solved optimally by greedy, this does not take into account the time required to check for independency.

## Examples of matroids
### Truncated matroid
Given an original Matroid
* M = (E, I)
A Truncated matroid is defined as 
* M2 = (E, I2)
* I2 = {X : X is a subset of I, |X| <= k for some k}
Nice. Now let's check the axioms

1. Downward closure: Does a subset B of A also belong to I?
> Yes. If |A| <= k and |B| <= |A|, |B| <= k
2. Extension:
> Yes. Remember that sets belonging to I in the original matroid all exhibited the property that |A| > |B| => exists e in A\B that can be added to B without violating the inclusion to I. The new matroid is defined so that all sets in I2 belong to I. Thus the statement goes for E2 as well.

This proves that the matroid is optimal for subproblems as well, so it's worth to take a stricter look on this proof.

### Partition matroid
* M = (E, I)
* E = A set of disjoint sets
* I = {X| X is a subset of E such that |X intersect Ei | <= k for k1, k2...kl}

* Property 1:
> True. Any subset of X does also belong to I. Proof, assume that it is not true. Then there is at least one disjoint set Ek such that |A intersect Ei| > k.
Yet A is a subset of X, meaning that it contains the exact same set or less elements than X. The removal of elements can never cause the intersection to increase, thus the assumption is false.

* Property 2: If |A| > |B| then that means that for at least some partition Ek we have that |A intersect E| > |B intersect E|. And that basically proves it. Think about it.
Do take not that this only works if the sets are disjoint.


### Graphic matroid
G = (V, E) is an undirected graph. Let
* M = (E, I)
* E = edges in an graph
* I = {S: S ⊆ E such that S is an acyclic graph}

Property 1 holds since any subset of an acyclic graph S is also an acyclic graph

Property 2 holds since |X| > |Y| implies that X contains one more component, which means it contains one edge connecting two components in A. Adding this edge to Y will still result in an acyclic graph since we are only connecting separate components, and the property holds.
### Transforming a min-cost spanning tree into a weighed matroid and solving it.
G = (V, E) is an undirected connected graph where each edge has a cost. We want to find a spanning tree with minimal cost.

We transform this problem to a matroid by tranforming the edgecosts in the original graph to edgeweights in the matroid according to: weight(e) = MAXCOST - cost(e)
> This tranformation causes the edges with the lowest cost to have the highest weight. We do this because matroids work easier when considering maximization (??)

With 

* M = (E, I)
* E = edges in an graph
* I = {S: S ⊆ E such that S is an acyclic graph}

We have now transformed the problem of finding a maximal spanning tree with minimal cost into finding a maximum independent set with max weight


Property 1 holds since any subset of an acyclic graph S is also an acyclic graph

Property 2 holds since |X| > |Y| implies that X contains one more component, which means it contains one edge connecting two components in A. Adding this edge to Y will still result in an acyclic graph since we are only connecting separate components, and the property holds.
### Counterexample, bipartite graph
### Arborescences (Intersection)
### Netflix (Intersection)

# Exercise set 1
## 1
Prove that GREEDY returns the base of a metroid
* Greedy adds independent elements as long as they can be added.
* Let A be the solution returned by GREEDY and assume that it is not a base. Let B be a base.
* Then |B| > |A| and per the second axiom there is an independent element e in B which could be added to A.
* This causes a contradiction since our algorithm never added e to A, despite it being possible.
## 2
Prove that GREEDY is optimal for subsets of the problem as well.
* Greedy is optimal for matroids.
* Any matroid can be tranformed into a truncated matroid with a base of lower cardinality.
* Since the truncated matroid is itself a matroid, GREEDY will perform optimally on it.
* Thus GREEDY will be optimal for any subset of the original problem

## 3
Prove that the partion matroid is a matroid.
* 

## 4
## 5
## 6
## 7

# Lecture 3: Linear 
## Recap
Greedy is optial for max-weight independent set.
Greedy is polynomial for max-weight independent set of matroid intersection

## Bipartite matching
* Matching: Every vertex has at most degree 1.
* Path: Sequences of vertices such that all vertices is unique and there is an edge between all consecutive vertices. 
* Alternating path: For a matching M, a path P is alternating if the edges alternate between M and E\M. Alternating path is needed to maintain a matching
* Augmenting path: For a matching M, an alternating path is a path that starts and ends with unmatched vertices. 

## Augmenting path algortihm
1. M = {}, no match
2. WHILE EXISTS augmenting path P
3. M = (M\MAP) UNION (P\M)
> M symmetric differene P, remove the intersection
4. Return M

Augmenting path algorithm works in linear time for bipartite graphs. Not quite as good for general graphs.

**Runtime** (|V| + |E|)(|V|)
> Every time an augmenting path is found, Matching is increased by 1. Maximum matching is of size |V|. Algorithm runs at most |V| times.

### Proof of optimal matching
**Lemma:** A matching M is of maximum cardinality IFF there is no augmenting path

**Prove:** OPT M => No augmenting path
1. Suppose there exist an augmenting path P. But then  M symmetric matching P is a larger matching than M, contradicting the optimality of M.

**Prove:** No augmenting path => OPT M <=> If matching M is not optimal then there is an augmenting path.
1. Let M2 be the optimal solution, M be our solution |M2| > |M| 
2. M2 SYMDIFF M 
3. Every vertex has degree of most 2 =>
4. Each component  is either a path or a cycle
5. If you start with a degree one vertex you get a path
6. If you start with degree 2 you get a cycle. 
7. If it is a cycle then it is alternating by M2 and M and we have the same amount of edges from each set.
8. Remove the cycles from M2 and M
9. Then |M2| is still bigger than |M|
10. Then we either start and end on white edges, red and white, red and red.
11. We know that we have more red edges than white edges
12. Thus at least one of the paths start and end with red, and that is an augmenting path.
13. Thus, if M is not matching then there is an augmenting path.

## Linear programming
Optimize linear functions subject to linear inequalites

You are not allowed to force values to take either-or values. You are allowed to define ranges however.

### Linear programming as max weight bipartite matching
The variables should correspond the decision you have to make

For each edge e decide whether to take take e or not.
> Thus we have one variable for each edge. e = 1 if e is taken, 0 otherwise

We want to maximizesum xw(x)

For all vertices: sum of edges incident to v x <= 1

THm: An optimal solution to LP can be taken such that xe belongs to {0,1} for all edges if graph is bipartite

# SYMBOLS
∈   BELONGS TO
∪   UNION
∩   INTERSECT
^	AND
∨	OR
¬	NEGATION
⊕	XOR
⇒	IMPLIES
⇔	IFF
∀	FOR ALL
∃	EXIST
∴	THEREFORE
∵   BECAUSE
⊆
⊂
∅
