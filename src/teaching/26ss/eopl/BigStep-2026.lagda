---
title     : "BigStep: Big-step semantics"
permalink : /BigStep/
---

\begin{code}
module plfa.part2.BigStep-2026 where
\end{code}

# Introduction

The preceding chapter defines an intrinsically-typed lambda calculus
using de Bruijn indices.  It also gives a small-step operational
semantics, written `M —→ N`, where each step performs one local
computation.  In this chapter we introduce a second presentation of
evaluation.

A _big-step semantics_ relates a closed term directly to the value it
computes.  We write this relation as `M ⇓ V`: the term `M` evaluates
to the value `V`.  Compared with small-step reduction, big-step
evaluation hides the intermediate states and focuses on the final
answer.  This makes it a convenient specification of interpreters and
evaluators, while small-step reduction remains useful for reasoning
about individual computation steps.

# Imports

\begin{code}
import Relation.Binary.PropositionalEquality as Eq
open Eq using (_≡_; refl; cong)
open import Data.Nat using (ℕ; zero; suc; _<_; z<s; s<s; _≤_; z≤n; s≤s; _≤?_)
open import Relation.Nullary.Negation using (¬_)
open import Data.Product using (∃-syntax; proj₁; proj₂) renaming (_,_ to ⟨_,_⟩)
open import Relation.Nullary.Decidable using (True; toWitness)

open import plfa.part2.DeBruijn-2026
\end{code}

# Big-step evaluation

The big-step relation is indexed by the type of the input and output
terms.  Since both terms are closed, the context is always `∅`.
The intended reading of `M ⇓ V` is that evaluation of `M` terminates
with the value `V`.

\begin{code}
data _⇓_ : ∀ {A} → ∅ ⊢ A → ∅ ⊢ A → Set where

  ⇓-ƛ : ∀ {A}{B}{M : ∅ , A ⊢ B}
    → (ƛ M) ⇓ (ƛ M)

  ⇓-· : ∀ {A}{B}{L : ∅ ⊢ A ⇒ B}{L′ : ∅ , A ⊢ B}{M V : ∅ ⊢ A}{W}
    → L ⇓ (ƛ L′)
    → M ⇓ V
    → (L′ [ V ]) ⇓ W
    → (L · M) ⇓ W

  ⇓-zero : `zero ⇓ `zero

  ⇓-suc : ∀ {M}{V}
    → M ⇓ V
    → (`suc M) ⇓ (`suc V)

  ⇓-case-zero : ∀ {A}{L}{M : ∅ ⊢ A}{N}{V}
    → L ⇓ `zero
    → M ⇓ V
    → case L M N ⇓ V

  ⇓-case-suc :  ∀ {A}{L}{M : ∅ ⊢ A}{N}{V}{W}
    → L ⇓ (`suc W)
    → (N [ W ]) ⇓ V
    → case L M N ⇓ V

  ⇓-μ : ∀ {A}{M : ∅ , A ⊢ A}{V}
    → (M [ μ M ]) ⇓ V
    → (μ M) ⇓ V
\end{code}

The rules mirror the constructs of the language.
Lambda abstractions and zero are already values.  To evaluate an
application, first evaluate the operator to a lambda abstraction,
then evaluate the argument, and finally evaluate the body after
substituting the argument value for the bound variable.  Successor and
case evaluate their natural-number subterms, and recursion unfolds one
step before continuing.

# Evaluation returns values

The result of big-step evaluation should not be an arbitrary term: it
should be a syntactic value.  The following lemma records that fact.
It proceeds by induction over the big-step derivation.

\begin{code}
⇓-returns-V : ∀ {A}{M V : ∅ ⊢ A} → M ⇓ V → Value V
⇓-returns-V ⇓-ƛ = V-ƛ
⇓-returns-V (⇓-· L⇓ƛL′ M⇓V L′[V]⇓W)
  with ⇓-returns-V L⇓ƛL′
... | V-ƛ
  with ⇓-returns-V M⇓V
... | ih-M = ⇓-returns-V L′[V]⇓W
⇓-returns-V ⇓-zero = V-zero
⇓-returns-V (⇓-suc M⇓V) = V-suc (⇓-returns-V M⇓V)
⇓-returns-V (⇓-case-zero L⇓zero M⇓V)
  with ⇓-returns-V L⇓zero
... | V-zero = ⇓-returns-V M⇓V
⇓-returns-V (⇓-case-suc L⇓sucW N[W]⇓V)
  with ⇓-returns-V L⇓sucW
... | V-suc ih =  ⇓-returns-V N[W]⇓V
⇓-returns-V (⇓-μ M⇓V) = ⇓-returns-V M⇓V
\end{code}

# Relating big-step and small-step semantics

We next connect the big-step relation to the small-step reduction
relation from the previous chapter.  The desired theorem has two
directions:

  * _soundness_: if `M ⇓ V`, then `M —↠ V`;
  * _completeness_: if `M —↠ V` and `V` is a value, then `M ⇓ V`.

Before proving these statements, we collect a few standard lemmas
about multi-step reduction.

## Lifting reductions through contexts

If a single-step reduction can be lifted through some term context
`F`, then a multi-step reduction can be lifted through the same
context.  We use this generic lemma for successor and case terms.

\begin{code}
ξ-lift : ∀ {A B} {M N : ∅ ⊢ A}{F : ∅ ⊢ A → ∅ ⊢ B}
  → (ξ : ∀ {M}{N} → M —→ N → F M  —→ F N)
  → M —↠ N
  → F M —↠ F N
ξ-lift {F = F} ξ (M ∎) = F M ∎
ξ-lift ξ (L —→⟨ L—→M ⟩ M—↠N) = _ —→⟨ ξ L—→M ⟩ ξ-lift ξ M—↠N

ξ-suc-lift : ∀ {M N : ∅ ⊢ `ℕ}
  → M —↠ N →  `suc M —↠ `suc N
ξ-suc-lift = ξ-lift ξ-suc

ξ-case-lift : ∀ {A} {L L′ : ∅ ⊢ `ℕ}{M : ∅ ⊢ A} {N}
  → L —↠ L′ →  case L M N —↠ case L′ M N
ξ-case-lift = ξ-lift ξ-case
\end{code}

## Transitivity

Multi-step reduction is transitive.  The proof is structurally the
same as append for lists: append the first reduction sequence to the
front of the second one.

\begin{code}
—↠-trans : ∀ {A}{L M N : ∅ ⊢ A} → L —↠ M → M —↠ N → L —↠ N
—↠-trans (M ∎) M—↠N = M—↠N
—↠-trans (L —→⟨ x ⟩ L—↠M) M—↠N = L —→⟨ x ⟩ —↠-trans L—↠M M—↠N
\end{code}

# Completeness

Completeness says that if small-step reduction reaches a value, then
big-step evaluation reaches the same value.  The proof is split in
two.  First, a single small-step reduction preserves the result of
big-step evaluation.  Second, the argument is extended from one step
to many steps.

\begin{code}
complete-step : ∀ {A} {M N V : ∅ ⊢ A}
  → M —→ N → M ⇓ V → N ⇓ V
complete-step = {!!}

completeness : ∀ {A} {M V : ∅ ⊢ A}
  → M —↠ V → Value V → M ⇓ V
completeness = {!!}
\end{code}

# Soundness

Soundness goes in the other direction: every big-step derivation can
be expanded into a multi-step reduction from the input term to the
same value.  The proof follows the shape of the big-step derivation.
In the application case, the reductions for the operator and argument
are lifted into the corresponding evaluation contexts before the
β-rule is applied.

\begin{code}
soundness : ∀ {A} {M V : ∅ ⊢ A}
  → M ⇓ V → M —↠ V
soundness (⇓-ƛ {M = M}) = ƛ M ∎
soundness (⇓-· {L′ = L′}{M = M} L⇓ƛL′ M⇓V L′[V]⇓W)
  using red1 ← ξ-lift (ξ-·₁ {M = M}) (soundness L⇓ƛL′)
  using red2 ← ξ-lift (ξ-·₂ {V = ƛ L′} V-ƛ) (soundness M⇓V)
  using red3 ← —↠-trans red1 red2
  = —↠-trans red3 (_ —→⟨ β-ƛ (⇓-returns-V M⇓V) ⟩ soundness L′[V]⇓W)
soundness ⇓-zero = `zero ∎
soundness (⇓-suc M⇓V) = ξ-lift ξ-suc (soundness M⇓V)
soundness (⇓-case-zero {M = M}{N = N} L⇓zero M⇓V)
  using red ← ξ-case-lift{M = M}{N = N} (soundness L⇓zero)
    = —↠-trans red ((case `zero M N) —→⟨ β-zero ⟩ (soundness M⇓V))
soundness (⇓-case-suc {M = M}{N = N} L⇓suc N⇓V)
  using red ← ξ-case-lift{M = M}{N = N} (soundness L⇓suc)
  with ⇓-returns-V L⇓suc
... | V-suc val-W
  = —↠-trans red (case (`suc _) M N —→⟨ β-suc val-W ⟩ soundness N⇓V)
soundness (⇓-μ {M = M} M⇓V) = μ M —→⟨ β-μ ⟩ soundness M⇓V
\end{code}

The proof uses the big-step derivation as its induction structure.
Each constructor of `_⇓_` explains why the source term evaluates, and
the corresponding clause of `soundness` turns that explanation into a
small-step reduction sequence.

For values, no computation is required.  A lambda abstraction reduces
to itself by the empty multi-step sequence `ƛ M ∎`, and zero reduces
to itself by `` `zero ∎ ``.  The successor case is also direct: by the
induction hypothesis, `M` reduces to `V`; applying `ξ-suc` at every
step lifts this sequence to a reduction from `` `suc M `` to
`` `suc V ``.

The application case is the main one.  From the big-step derivation we
know three things: the operator `L` evaluates to a lambda `ƛ L′`, the
argument `M` evaluates to a value `V`, and the substituted body
`L′ [ V ]` evaluates to `W`.  The induction hypotheses give
multi-step reductions for each of these evaluations.  The first
reduction is lifted into the left side of the application with
`ξ-·₁`, producing a reduction from `L · M` to `(ƛ L′) · M`.  The
second reduction is lifted into the right side of the application
with `ξ-·₂`; this rule requires the operator to be a value, supplied
by `V-ƛ`.  After both subterms have been reduced, the β-rule
`β-ƛ` takes the single step from `(ƛ L′) · V` to `L′ [ V ]`.  Finally,
the induction hypothesis for the body evaluation reduces `L′ [ V ]`
to `W`.  The intermediate sequences are joined with `—↠-trans`.

The two case-expression clauses follow the same pattern.  First, the
scrutinee reduction is lifted into the `case` context.  If the
scrutinee evaluates to `zero`, the β-rule `β-zero` selects the zero
branch and the induction hypothesis for that branch finishes the
reduction.  If the scrutinee evaluates to `suc W`, the lemma
`⇓-returns-V` tells us that `W` is a value, which is exactly the
premise required by `β-suc`; after this step, the induction hypothesis
for the substituted successor branch completes the proof.

The recursion case is the smallest computational case.  The small-step
semantics unfolds `μ M` by one `β-μ` step to `M [ μ M ]`, and the
induction hypothesis then reduces that unfolded term to the value
produced by the big-step derivation.

# Big-step evaluation with environments

The first big-step relation uses substitution directly.  A more
implementation-oriented evaluator can instead carry an environment
that maps variables to closed terms.  The following definitions start
that development.

\begin{code}
Env : Context → Set
Env Γ = Sub Γ ∅
\end{code}

An environment is just a substitution from the current context to the
empty context.  Thus an entry for a variable is a closed term of the
appropriate type.

\begin{code}
data _∣_⇓_ : ∀ {Γ}{A} → Env Γ → Γ ⊢ A → ∅ ⊢ A → Set where

  ⇓-‵ : ∀ {Γ}{A} {σ : Env Γ}{x : Γ ∋ A}
    → σ ∣ ` x ⇓ σ x

  ⇓-ƛ : ∀ {Γ}{A}{B} {σ : Env Γ}{M : Γ , A ⊢ B}
    → σ ∣ (ƛ M) ⇓ {!!}           -- need a closure at this point
\end{code}

The lambda case exposes the limitation of this representation.  A
lambda term with free variables cannot be returned as a closed value
by itself; it must be paired with the environment that gives meanings
to those variables.  That pair is a _closure_, which is the next
structure needed for this development.

\begin{code}
-- closure = pair of σ and M
\end{code}

% Local Variables:
% mode: agda2
% End:
