-- There are two styles for mechanising a *typed* programming language:
--
--   * EXTRINSIC (Curry-style): terms are defined first, without any
--     reference to types.  Typing is a *separate* relation `Γ ⊢ e ⦂ t`
--     layered on top.  An expression like `(ƛ "x" ⇒ ` "x") · `zero` is a
--     perfectly fine `Term`, it just may or may not be well-typed.
--     Type soundness has to be *proved* and splits into two theorems:
--       - preservation: reduction keeps the type, and
--       - progress:     well-typed terms do not get stuck.
--
--   * INTRINSIC (Church-style): only well-typed terms can be written down
--     in the first place.  The datatype of terms `Γ ⊢ A` is *indexed* by
--     a context and a type, so an ill-typed term is not even expressible.
--     Here preservation comes *for free* — the reduction relation relates
--     terms of the *same* type by construction — and progress remains the
--     one theorem worth proving.
--
-- Below we set up both styles for the same simply typed lambda calculus
-- (functions + naturals + recursion).  In each module substitution is
-- left as a hole, and `preservation` / `progress` are the goals.

module intrinsic-vs-extrinsic where

open import Data.Sum using (_⊎_; inj₁; inj₂)


-- EXTRINSIC ───────────────────────────────────────────────────────────────────
--
-- Untyped terms, with typing as a separate relation.

module Extrinsic where

  open import Data.Product using (∃-syntax)
  open import Data.String using (String; _≟_)
  open import Relation.Nullary.Decidable using (yes; no)
  open import Relation.Nullary.Negation using (contradiction)
  open import Relation.Binary.PropositionalEquality using (_≡_; _≢_; refl)

  Id : Set
  Id = String

  infix  5  ƛ_⇒_  μ_⇒_
  infixl 7  _·_
  infix  8  `suc_
  infix  9  `_

  -- Syntax: nothing here knows about types.
  data Term : Set where
    `_                   : Id → Term
    ƛ_⇒_                 : Id → Term → Term
    _·_                  : Term → Term → Term
    `zero                : Term
    `suc_                : Term → Term
    case_[zero⇒_|suc_⇒_] : Term → Term → Id → Term → Term
    μ_⇒_                 : Id → Term → Term

  data Value : Term → Set where
    V-ƛ    : ∀ {x N} → Value (ƛ x ⇒ N)
    V-zero : Value `zero
    V-suc  : ∀ {V} → Value V → Value (`suc V)

  infix 9 _[_:=_]

  -- Substitution on raw terms is easy to define: it is a plain structural
  -- recursion that does not need to know anything about types.
  _[_:=_] : Term → Id → Term → Term
  (` x) [ y := V ] with x ≟ y
  ... | yes _ = V
  ... | no  _ = ` x
  (ƛ x ⇒ e) [ y := V ] with x ≟ y
  ... | yes _ = ƛ x ⇒ e
  ... | no  _ = ƛ x ⇒ e [ y := V ]
  (e₁ · e₂) [ y := V ] = e₁ [ y := V ] · e₂ [ y := V ]
  (`zero) [ y := V ] = `zero
  (`suc e₂) [ y := V ] = `suc e₂ [ y := V ]
  (case e [zero⇒ e₁ |suc x ⇒ e₂ ]) [ y := V ] with x ≟ y
  ... | yes _ = case e [ y := V ] [zero⇒ e₁ [ y := V ] |suc x ⇒ e₂ ]
  ... | no  _ = case e [ y := V ] [zero⇒ e₁ [ y := V ] |suc x ⇒ e₂ [ y := V ] ]
  (μ x ⇒ e) [ y := V ] with x ≟ y
  ... | yes _ = μ x ⇒ e
  ... | no  _ = μ x ⇒ e [ y := V ]

  infix 4 _↪_

  data _↪_ : Term → Term → Set where

    β-ƛ : ∀ {x e₁ e₂} →
      Value e₂ →
      (ƛ x ⇒ e₁) · e₂ ↪ e₁ [ x := e₂ ]

    β-zero : ∀ {x e₁ e₂} →
      case `zero [zero⇒ e₁ |suc x ⇒ e₂ ] ↪ e₁

    β-suc : ∀ {x e e₁ e₂} →
      Value e →
      case `suc e [zero⇒ e₁ |suc x ⇒ e₂ ] ↪ e₂ [ x := e ]

    β-μ : ∀ {x e₂} →
      μ x ⇒ e₂ ↪ e₂ [ x := μ x ⇒ e₂ ]

    ξ-·₁ : ∀ {e₁ e₁′ e₂} →
      e₁ ↪ e₁′ →
      e₁ · e₂ ↪ e₁′ · e₂

    ξ-·₂ : ∀ {V e₂ e₂′} →
      Value V →
      e₂ ↪ e₂′ →
      V · e₂ ↪ V · e₂′

    ξ-suc : ∀ {e₂ e₂′} →
      e₂ ↪ e₂′ →
      `suc e₂ ↪ `suc e₂′

    ξ-case : ∀ {x e₁ e₁′ e₂ N} →
      e₁ ↪ e₁′ →
      case e₁ [zero⇒ e₂ |suc x ⇒ N ] ↪ case e₁′ [zero⇒ e₂ |suc x ⇒ N ]

  infixr 7 _⇒_

  data Type : Set where
    _⇒_ : Type → Type → Type
    `ℕ  : Type

  infixl 5  _,_⦂_

  data Context : Set where
    ∅     : Context
    _,_⦂_ : Context → Id → Type → Context

  infix  4  _∋_⦂_

  data _∋_⦂_ : Context → Id → Type → Set where

    Z : ∀ {Γ x A} →
      Γ , x ⦂ A ∋ x ⦂ A

    S : ∀ {Γ x y A B} →
      x ≢ y →
      Γ ∋ x ⦂ A →
      Γ , y ⦂ B ∋ x ⦂ A

  infix  4  _⊢_⦂_

  -- Typing: a separate relation on top of the untyped syntax.
  data _⊢_⦂_ : Context → Term → Type → Set where

    ⊢` : ∀ {Γ x A} →
      Γ ∋ x ⦂ A →
      Γ ⊢ ` x ⦂ A

    ⊢ƛ : ∀ {Γ x N A B} →
      Γ , x ⦂ A ⊢ N ⦂ B →
      Γ ⊢ ƛ x ⇒ N ⦂ A ⇒ B

    ⊢· : ∀ {Γ e₁ e₂ A B} →
      Γ ⊢ e₁ ⦂ A ⇒ B →
      Γ ⊢ e₂ ⦂ A →
      Γ ⊢ e₁ · e₂ ⦂ B

    ⊢zero : ∀ {Γ} →
      Γ ⊢ `zero ⦂ `ℕ

    ⊢suc : ∀ {Γ e₂} →
      Γ ⊢ e₂ ⦂ `ℕ →
      Γ ⊢ `suc e₂ ⦂ `ℕ

    ⊢case : ∀ {Γ e e₁ e₂ x t} →
      Γ ⊢ e ⦂ `ℕ →
      Γ ⊢ e₁ ⦂ t →
      Γ , x ⦂ `ℕ ⊢ e₂ ⦂ t →
      Γ ⊢ case e [zero⇒ e₁ |suc x ⇒ e₂ ] ⦂ t

    ⊢μ : ∀ {Γ x e₂ t} →
      Γ , x ⦂ t ⊢ e₂ ⦂ t →
      Γ ⊢ μ x ⇒ e₂ ⦂ t

  -- The price of the extrinsic style: substitution was trivial to define,
  -- but everything that connects it back to *typing* has to be proved.
  -- Following the PLFA Properties chapter, `subst-preserves` is established
  -- through a family of renaming/weakening lemmas.  All are left as stubs.

  -- A renaming maps variables of Γ to variables of Δ, preserving types.
  Ren : Context → Context → Set
  Ren Γ Δ = ∀ {x A} → Γ ∋ x ⦂ A → Δ ∋ x ⦂ A

  -- A renaming extends under a binder…
  ext : ∀ {Γ Δ x A} →
    Ren Γ Δ →
    Ren (Γ , x ⦂ A) (Δ , x ⦂ A)
  ext = {!!}

  -- …and lifts to typing derivations.
  rename : ∀ {Γ Δ e t} →
    Ren Γ Δ →
    Γ ⊢ e ⦂ t →
    Δ ⊢ e ⦂ t
  rename = {!!}

  -- The three special cases of renaming used by `subst-preserves`:
  weaken : ∀ {Γ e t} →
    ∅ ⊢ e ⦂ t →
    Γ ⊢ e ⦂ t
  weaken = {!!}

  drop : ∀ {Γ x t₁ t₂ e t} →
    Γ , x ⦂ t₁ , x ⦂ t₂ ⊢ e ⦂ t →
    Γ , x ⦂ t₂ ⊢ e ⦂ t
  drop = {!!}

  swap : ∀ {Γ x y t₁ t₂ e t} →
    x ≢ y →
    Γ , x ⦂ t₁ , y ⦂ t₂ ⊢ e ⦂ t →
    Γ , y ⦂ t₂ , x ⦂ t₁ ⊢ e ⦂ t
  swap = {!!}

  -- The crux of the β-cases of preservation: substituting a closed,
  -- well-typed term for a variable preserves typing.
  subst-preserves : ∀ {Γ x e e' t t'} →
    Γ , x ⦂ t' ⊢ e ⦂ t →
    ∅ ⊢ e' ⦂ t' →
    Γ ⊢ e [ x := e' ] ⦂ t
  subst-preserves = {!!}

  -- The two halves of type soundness.  Both must be proved by hand;
  -- preservation leans on `subst-preserves` for the β-reductions.

  preservation : ∀ {e e' t} →
    ∅ ⊢ e ⦂ t →
    e ↪ e' →
    ∅ ⊢ e' ⦂ t
  preservation = {!!}

  progress : ∀ {e t} →
    ∅ ⊢ e ⦂ t →
    Value e ⊎ ∃[ e' ] e ↪ e'
  progress = {!!}


-- INTRINSIC ─────────────────────────────────────────────────────────────────
--
-- Well-typed terms by construction, using de Bruijn indices.  The type
-- `Γ ⊢ A` is the type of terms of type `A` in context `Γ`, so ill-typed
-- terms simply cannot be written down.

module Intrinsic where

  open import Data.Product using (∃-syntax)

  infixr 7 _⇒_

  data Type : Set where
    _⇒_ : Type → Type → Type
    `ℕ  : Type

  infixl 5 _,_

  -- A context is just a list of types — variables are positions, so no
  -- names are needed.
  data Context : Set where
    ∅   : Context
    _,_ : Context → Type → Context

  infix  4 _∋_

  -- A de Bruijn index: a proof that type `A` occurs in context `Γ`.
  data _∋_ : Context → Type → Set where

    Z : ∀ {Γ A} →
      Γ , A ∋ A

    S_ : ∀ {Γ A B} →
      Γ ∋ A →
      Γ , B ∋ A

  infix  4 _⊢_
  infix  5 ƛ_
  infix  5 μ_
  infixl 7 _·_
  infix  8 `suc_
  infix  9 `_

  -- Intrinsically typed terms: the constructors *are* the typing rules.
  data _⊢_ : Context → Type → Set where

    `_ : ∀ {Γ A} →
      Γ ∋ A →
      Γ ⊢ A

    ƛ_ : ∀ {Γ A B} →
      Γ , A ⊢ B →
      Γ ⊢ A ⇒ B

    _·_ : ∀ {Γ A B} →
      Γ ⊢ A ⇒ B →
      Γ ⊢ A →
      Γ ⊢ B

    `zero : ∀ {Γ} →
      Γ ⊢ `ℕ

    `suc_ : ∀ {Γ} →
      Γ ⊢ `ℕ →
      Γ ⊢ `ℕ

    case : ∀ {Γ A} →
      Γ ⊢ `ℕ →
      Γ ⊢ A →
      Γ , `ℕ ⊢ A →
      Γ ⊢ A

    μ_ : ∀ {Γ A} →
      Γ , A ⊢ A →
      Γ ⊢ A

  -- Substitution.  Here the work is reversed compared to the extrinsic
  -- style: *defining* substitution is the involved part, since every step
  -- must thread the context and type through (this is what forces the
  -- renaming machinery below).  But once these stubs type-check there is
  -- nothing left to prove — the signatures *are* the preservation
  -- statements, so there is no separate `subst-preserves` lemma.
  -- The stubs below follow the PLFA DeBruijn chapter.

  Rename : Context → Context → Set
  Rename Γ Δ = ∀ {A} → Γ ∋ A → Δ ∋ A

  Subst : Context → Context → Set
  Subst Γ Δ = ∀ {A} → Γ ∋ A → Δ ⊢ A

  -- Renamings extend under a binder…
  ext : ∀ {Γ Δ} → Rename Γ Δ → ∀ {B} → Rename (Γ , B) (Δ , B)
  ext = {!   !}

  -- …and lift to terms.
  rename : ∀ {Γ Δ} → Rename Γ Δ → ∀ {A} → Γ ⊢ A → Δ ⊢ A
  rename ρ N = {!   !}

  -- Substitutions extend under a binder using renaming…
  exts : ∀ {Γ Δ} → Subst Γ Δ → ∀ {B} → Subst (Γ , B) (Δ , B)
  exts σ N = {!   !}

  -- …and lift to terms (simultaneous substitution).
  subst : ∀ {Γ Δ} → Subst Γ Δ → ∀ {A} → Γ ⊢ A → Δ ⊢ A
  subst σ N = {!   !}

  -- Single substitution of the top variable, used by the β-rules.
  _[_] : ∀ {Γ A B} →
    Γ , A ⊢ B →
    Γ ⊢ A →
    Γ ⊢ B
  _[_] {Γ} {A} N M = {!   !}

  data Value : ∀ {Γ A} → Γ ⊢ A → Set where

    V-ƛ : ∀ {Γ A B} {N : Γ , A ⊢ B} →
      Value (ƛ N)

    V-zero : ∀ {Γ} →
      Value (`zero {Γ})

    V-suc : ∀ {Γ} {V : Γ ⊢ `ℕ} →
      Value V →
      Value (`suc V)

  infix 4 _↪_

  -- Note the type: both sides live in `Γ ⊢ A` for the *same* `A`.  This is
  -- exactly preservation, baked into the relation.
  data _↪_ : ∀ {Γ A} → (Γ ⊢ A) → (Γ ⊢ A) → Set where

    ξ-·₁ : ∀ {Γ A B} {e₁ e₁′ : Γ ⊢ A ⇒ B} {e₂ : Γ ⊢ A} →
      e₁ ↪ e₁′ →
      e₁ · e₂ ↪ e₁′ · e₂

    ξ-·₂ : ∀ {Γ A B} {V : Γ ⊢ A ⇒ B} {e₂ e₂′ : Γ ⊢ A} →
      Value V →
      e₂ ↪ e₂′ →
      V · e₂ ↪ V · e₂′

    β-ƛ : ∀ {Γ A B} {N : Γ , A ⊢ B} {W : Γ ⊢ A} →
      Value W →
      (ƛ N) · W ↪ N [ W ]

    ξ-suc : ∀ {Γ} {e₂ e₂′ : Γ ⊢ `ℕ} →
      e₂ ↪ e₂′ →
      `suc e₂ ↪ `suc e₂′

    ξ-case : ∀ {Γ A} {e e′ : Γ ⊢ `ℕ} {e₁ : Γ ⊢ A} {e₂ : Γ , `ℕ ⊢ A} →
      e ↪ e′ →
      case e e₁ e₂ ↪ case e′ e₁ e₂

    β-zero : ∀ {Γ A} {e₁ : Γ ⊢ A} {e₂ : Γ , `ℕ ⊢ A} →
      case `zero e₁ e₂ ↪ e₁

    β-suc : ∀ {Γ A} {V : Γ ⊢ `ℕ} {e₁ : Γ ⊢ A} {e₂ : Γ , `ℕ ⊢ A} →
      Value V →
      case (`suc V) e₁ e₂ ↪ e₂ [ V ]

    β-μ : ∀ {Γ A} {N : Γ , A ⊢ A} →
      μ N ↪ N [ μ N ]

  -- Note there is *no* `subst-preserves` lemma here: its extrinsic analogue
  -- is subsumed by the type of `subst`/`_[_]` above, which can only produce
  -- a term of the right type.  Likewise preservation is *free* — the
  -- reduction relation already only relates terms of the same type, so a
  -- reduct of `M : ∅ ⊢ A` is again of type `∅ ⊢ A`.  The statement is
  -- therefore trivially inhabited. The goal worth filling in is `progress`.

  progress : ∀ {A} {M : ∅ ⊢ A} →
    Value M ⊎ ∃[ N ] (M ↪ N)
  progress = {!!}
