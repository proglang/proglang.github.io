# Available Projects & Theses

## General Information

If you are interested in one of the topics below or you have thought of a topic yourself, 
please write an email to [Prof. Dr. Thiemann](team/thiemann.md) with all required details.

Also, if you cannot find a suitable topic here, you may still want to write an email to 
[Prof. Dr. Thiemann](team/thiemann.md).

## Overview

### Bachelorprojekt

<!-- #### Reusable Library for checking correctness + exhaustiveness of nested pattern matching
* Define set of ADTs with constructors and field types
* Receives type of initial expression + set of branches (ie. patterns) as inputs
* If exhaustive + correct: return which variables of which type are bound in branch #1, #2, etc.
* Failure cases: type mismatch, not exhaustive, unreachable branches
* Possible extension points
    * more complicated patterns (eg. or patterns, `Some(Pair(suc x, _) | Pair(_, suc x))`)
    * reasonable representation/printing of non-exhaustive patterns
    * lazy pattern matching
* [Luc Maranget: Warnings for pattern matching](https://cambium.inria.fr/~maranget/papers/warn/warn.pdf)
* [Luc Maranget: Compiling Pattern Matching to Good Decision Trees](http://moscova.inria.fr/~maranget/papers/ml05e-maranget.pdf)
 -->

#### Extensions to the compiler construction lecture compiler
* Arrays
* Strings / Chars
* Match
* …?

#### Extending Lambda Pi Paper with Universe Polymorphism 
* Addition of universe levels and polymorphism to the existing implementation
* The type checker would use the subtype approach suggested here: https://github.com/agda/agda/issues/5810, where `Set l` < `Setω` for all `l`.
* as project: implementation
* follow up with thesis: proof, maybe explore alternatives, build upon Hannes' dependent types formalization

### Bachelorarbeit

### Master Lab Course

<!-- 
### Lecture compiler in Rust
* different internal structure based on [Appel](https://api.pageplace.de/preview/DT0400.9781107266391_A23693450/preview-9781107266391_A23693450.pdf) 
-->

## Master Project

#### Extensions to the compiler construction lecture compiler
* `call/cc`
* `shift`/`reset`
* generators

#### Register Allocation using SAT Solving
* Usage of the compiler from the lecture
* Translation of the graph coloring problem to SAT
* Interfacing with an existing SAT solver (e.g. KISSAT, CaDiCaL)
* (Fuzzer based) Generation of large program instances to produce reasonable benchmarks for both runtime and compilation speed

#### Use agda-hs for program extraction of existing correct algorithm 
* students must be comfortable adjusting the Agda code to fit the custom agda-hs prelude

#### Reproduce Agda proofs in Lean
* SystemF or Logical Rel.
* Possible research questions: 
    * What is a good representation for syntax (extrinsic; scoped; intrinsic)?
    * How do we represent substitutions?  
    * What can Lean solve automatically, what Agda cannot?
    * What libraries exist to formalize PLs in Lean?

#### effect-calculus denotational semantics in Agda 
* [Bauer & Pretnar: An effect system for algebraic effects and handlers](https://lmcs.episciences.org/1153/pdf)

### Master Thesis

#### Implement dependent pattern matching in Rust
* [Jesper Cockx, Andreas Abel: Elaborating dependent (co)pattern matching](https://dl.acm.org/doi/epdf/10.1145/3236770)