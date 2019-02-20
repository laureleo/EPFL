# TODO
Join group
16.4 on weighed matroids

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

> **Axiom 1** If X ∈ Y and Y ⊆ I then X ∈ I. This is the heridetary property.

> **Axiom 2** If X and Y ∈ I and |Y| > |X|, then ∃e ∈ Y \ X : X ∪ {e} ∈ I. This is the exchange property.

### Examples
Define I = {T⊆ E : T is acyclic}.
* It satisfies axiom 1 since a subset of a an acyclic set of edges is also acyclic.
* It satisfies axiom 2 since a tree with k edges has n-k components.

## Terminology
* Independent set: A nonempty set of subsets where all subsets recursively fulfill the same property.
* Extension: An element that you can add to an independent set without violating its independency property
* Maximal: A independent set that has no extensions/Isn't a subset of another independent set

# SYMBOLS
∈   BELONGS TO
∪   UNION
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
