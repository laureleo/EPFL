# TODO
Review first lecture

# Lecture 1 Greediness
## Greedy algorithms
Algorithms that take the option that currently seem the best and then moving on.

If a problem can be stated as a matroid it can be optimally solved by a greedy algorithm.
## Graph theory basics
Given an undirected graph G={V,E}

A spanning tree consist of |V|-1 edges

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

**PROOF OF CORRECTNESS**
Lemma: An acyclic graph G=(V,E) consist of |V|-|E| components
> With 0 edges we have |V| components. For every edge added one component is absorbed into a bigger one.
Lemma: A subset of a spanning tree is itself a spanning tree.


Lemma: Kruskals algo returns a max-weight spanning tree



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
## Matroids
### Use
### Definition
### Axioms
### Examples
## Misc
### Union Find

