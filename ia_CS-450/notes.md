# TODO
Notes
Python

# Lecture 1 Introduction
## qu'est-ce que l'intelligence?
Aucune définition fait d'unamite, mais la capacite d'abstraction et d'explication fondée sur grande base de connaissances

## Comment creer l'intelligence?
* Programmation: Definier les lois qui controlent le comportement.
* Incertitude: Utiliser le calcul probabiliste
* Apprentissage: Donner des examples a suivre
* Optimisation: Comportement emergent

## Logique des predicats
Il existe des choses
* Symboles: Des objets et des parametres. Victor. 18 ans.
* Prédicats: Des relations et proprietes. OlderThan(Victor, 18ans)

## Propositions
Expressions logiques qui peut-etre vrai ou fausse. Il fait beau. C'est claire.

## Regles d'inference logique
A partir d'une ensemble de propositons qui sont vraies (les premisses) on trouve un nouvelle propositon x tel que x is vrai, ainsi que les propostions precedant.

### Lois d'inference
#### Les lois de Morgan
* ¬(A AND B) <=> ¬A OR ¬B
> If it is false that both are true, then it is true that one of them is false
* ¬(A OR B) => ¬A OR ¬B
> If it is false that either of them is true,  then both are false.
#### Les lois Distributives
* A AND (B OR C) = (A AND B) OR (A AND C)
* A OR (B AND C) = (A OR B) AND (A OR C)
#### Les lois Associatives 
* (A AND B) AND C = A AND (B AND C)
* (A OR B) OR C = A OR (B OR C)
#### Les lois Commutatives
* A AND B = B AND A
* A OR B = B OR A
#### Le loi de la Contraposeé
* A => B <=> NOT B => NOT A
#### modus ponens:
(p ⇒ q), p ⇒ q
#### introduction:
p, q ⇒ p ∧ q
#### elimination 
p ∧ q ⇒ p, q

### Modes d'inference
The three modes of inference.
* You observe a conclusion and infer a premise using abduction.
* You infer a rule for the relation between the cause and conclusion using induction.
* You use your rules and premises to infer new conclusions via deduction.
#### Deduction
Given premises and rules, infer conclusions
#### Induction
Given premises and conclusion, infer rules
#### Abduction
Given rules and conclusion, infer premises.

# Lecture 2 Inference
## Inference sans variables
### Inference par resolution
#### Transformation en forme conjugative normale
### Inference par chainage
### Chainage avant.
## Inference avec variables
### Quantification
#### Les fonctions de Skolem
#### Resolution avec variables (L'unification)
### Filtrage et unification

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
