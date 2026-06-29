module lambda where

module Overview where
  open import Data.Nat using (ℕ; zero; suc; _+_; _<ᵇ_)
  open import Data.Bool using (Bool; true; false; _∧_)
  open import Data.Sum using (_⊎_; inj₁; inj₂)
  open import Data.Product using (_×_; _,_; proj₁; proj₂; Σ-syntax; ∃-syntax)
  open import Relation.Binary.PropositionalEquality using (_≡_)


  -- THE PLANᵀᴹ
  -- 1) Quick Intro: Extrinsic vs Intrinsic
  -- 2) Preservation for the Mini Language
  -- 3) Substitution and Type Safety for the Lec Lang!


  -- Extrinsic (named) : 
     -- Expr : Set,
     -- _⊢_⦂_ : Context → Expr → Type → Set 
     -- _[_:=_] : Term → Id → Term → Term
     -- subst-preserves : ∀ {Γ x e e' t t'} →
     --   Γ , x ⦂ t' ⊢ e ⦂ t →
     --   ∅ ⊢ e' ⦂ t' →
     --   Γ ⊢ e [ x := e' ] ⦂ t

  -- Intrinsic (de Bruijn): 
     -- Expr : Context → Type → Set
     -- subst : ∀ {Γ Δ} → Subst Γ Δ → ∀ {A} → Γ ⊢ A → Δ ⊢ A

  -- Typed programming languages are formally specified by giving a
  -- syntax, semantics, and typing relation.

  -- The syntax describes the structure of programs, e.g.
  data Expr : Set where
    nat  : ℕ → Expr 
    bool : Bool → Expr 
    _`+_ : Expr → Expr → Expr
    _`<_ : Expr → Expr → Expr
    _`∧_ : Expr → Expr → Expr

  -- For example, the abstract syntax tree for the expression `2 + 3 < 6` is
  example : Expr
  example = (nat 2 `+ nat 3) `< nat 6


  -- The semantics describes the meaning of programs, i.e. how they are
  -- evaluated. A small-step operational semantics is a binary relation
  -- on expressions, _↪_, that describes the evaluation of a program
  -- as a sequence of reduction steps, e.g.

  data _↪_ : Expr → Expr → Set where
    -- contraction rules: compute the primitive once both operands are constants.
    -- We "cheat" by reusing Agda's own _+_, _<ᵇ_ and _∧_ to produce the result.
    β-+  : ∀ {n m}   → (nat n `+ nat m)     ↪ nat (n + m)
    β-<  : ∀ {n m}   → (nat n `< nat m)     ↪ bool (n <ᵇ m)
    β-∧  : ∀ {b₁ b₂} → (bool b₁ `∧ bool b₂) ↪ bool (b₁ ∧ b₂)
    -- congruence rules: reduce somewhere inside a subexpression
    ξ-+₁ : ∀ {e₁ e₁′ e₂} → e₁ ↪ e₁′ → (e₁ `+ e₂) ↪ (e₁′ `+ e₂)
    ξ-+₂ : ∀ {e₁ e₂ e₂′} → e₂ ↪ e₂′ → (e₁ `+ e₂) ↪ (e₁ `+ e₂′)
    ξ-<₁ : ∀ {e₁ e₁′ e₂} → e₁ ↪ e₁′ → (e₁ `< e₂) ↪ (e₁′ `< e₂)
    ξ-<₂ : ∀ {e₁ e₂ e₂′} → e₂ ↪ e₂′ → (e₁ `< e₂) ↪ (e₁ `< e₂′)
    ξ-∧₁ : ∀ {e₁ e₁′ e₂} → e₁ ↪ e₁′ → (e₁ `∧ e₂) ↪ (e₁′ `∧ e₂)
    ξ-∧₂ : ∀ {e₁ e₂ e₂′} → e₂ ↪ e₂′ → (e₁ `∧ e₂) ↪ (e₁ `∧ e₂′)

  -- Here we would define the relation, such that for example
  --
  --   (nat 2 `+ nat 3) `< nat 6  ↪  nat 5 `< nat 6  ↪  bool true
  --
  -- When it is not possible to apply the relation any more, this can mean
  -- one of two things:
  --
  -- 1.  The evaluation terminated successfully, e.g. `bool true`.
  --
  -- 2.  The evaluation got stuck (runtime error), e.g. `nat 5 `< true`.
  --
  -- To distinguish these cases, a value-predicate is defined, which
  -- distinguishes successfully evaluated programs from runtime errors.
  -- For example, `Value (bool true)` but not `Value (nat 5 `< true)`.

  data Value : Expr → Set where
    v-nat  : ∀ {n} → Value (nat n)
    v-bool : ∀ {b} → Value (bool b)

  --
  -- The typing relation, _⦂_, relates expressions with types.
  -- For the above example language that could be:

  data Type : Set where
    `Nat  : Type
    `Bool : Type

  data _⦂_ : Expr → Type → Set where
    t-nat  : ∀ {n} →
      nat n ⦂ `Nat
    t-bool : ∀ {b} →
      bool b ⦂ `Bool
    t-+  : ∀ {e₁ e₂} →
      e₁ ⦂ `Nat →
      e₂ ⦂ `Nat →
      (e₁ `+ e₂) ⦂ `Nat
    t-<  : ∀ {e₁ e₂} →
      e₁ ⦂ `Nat →
      e₂ ⦂ `Nat →
      (e₁ `< e₂) ⦂ `Bool
    t-∧  : ∀ {e₁ e₂} →
      e₁ ⦂ `Bool →
      e₂ ⦂ `Bool →
      (e₁ `∧ e₂) ⦂ `Bool

  -- To prove that the typing relation actually prevents runtime errors,
  -- we need to establish a relation between the typing and semantics,
  -- which is called *type soundness* or *type safety*.
  -- Type soundness states that if an expression `e` has some type
  -- `t`, i.e. `e ⦂ t`, then either
  --
  -- - it is possible to apply a finite amount of reduction steps
  --   to `e` such that it reduces to a value of type `t`, i.e.
  --
  --     e ↪ e₁ ↪ e₂ ↪ ... ↪ eₙ   ∧   Value eₙ   ∧   eₙ ⦂ t
  --
  -- - or the expression is non-terminating, i.e. it will
  --   always be possible to apply another reduction step.
  
  -- type soundness is usually proved by the following two theorems:

  preservation : ∀ {e e' t} →
    e ⦂ t →
    e ↪ e' →
    e' ⦂ t
  preservation (t-+ e⦂t e⦂t₁)    β-+           = t-nat
  preservation (t-+ e₁⦂t₁ e₂⦂t₂) (ξ-+₁ e₁↪e₁') = t-+ (preservation e₁⦂t₁ e₁↪e₁') e₂⦂t₂
  preservation (t-+ e₁⦂t₁ e₂⦂t₂) (ξ-+₂ e₂↪e₂') = t-+ e₁⦂t₁ (preservation e₂⦂t₂ e₂↪e₂')
  preservation (t-< e⦂t e⦂t₁) β-< = t-bool
  preservation (t-< e⦂t e⦂t₁) (ξ-<₁ e↪e') = t-< (preservation e⦂t e↪e') e⦂t₁
  preservation (t-< e⦂t e⦂t₁) (ξ-<₂ e↪e') = t-< e⦂t (preservation e⦂t₁ e↪e')
  preservation (t-∧ e⦂t e⦂t₁) β-∧ = t-bool
  preservation (t-∧ e⦂t e⦂t₁) (ξ-∧₁ e↪e') = t-∧ (preservation e⦂t e↪e') e⦂t₁
  preservation (t-∧ e⦂t e⦂t₁) (ξ-∧₂ e↪e') = t-∧ e⦂t (preservation e⦂t₁ e↪e')

  progress : ∀ {e t} →
    e ⦂ t →
    Value e ⊎ ∃[ e' ] e ↪ e'
  progress t-nat         = inj₁ v-nat
  progress t-bool        = inj₁ v-bool
  progress (t-+ e₁⦂t₁ e₂⦂t₂) with progress e₁⦂t₁ | progress e₂⦂t₂ 
  ... | inj₁ v-nat        | inj₁ v-nat        = inj₂ (_ , β-+)
  ... | _                 | inj₂ (_ , e₂↪e₂') = inj₂ (_ , ξ-+₂ e₂↪e₂')
  ... | inj₂ (_ , e₁↪e₁') | _                 = inj₂ (_ , ξ-+₁ e₁↪e₁')
  progress (t-< e₁⦂t₁ e₂⦂t₂) with progress e₁⦂t₁ | progress e₂⦂t₂  
  ... | inj₁ v-nat        | inj₁ v-nat        = inj₂ (_ , β-<)
  ... | _                 | inj₂ (_ , e₂↪e₂') = inj₂ (_ , ξ-<₂ e₂↪e₂')
  ... | inj₂ (_ , e₁↪e₁') | _                 = inj₂ (_ , ξ-<₁ e₁↪e₁')
  progress (t-∧ e₁⦂t₁ e₂⦂t₂) with progress e₁⦂t₁ | progress e₂⦂t₂  
  ... | inj₁ v-bool       | inj₁ v-bool       = inj₂ (_ , β-∧)
  ... | _                 | inj₂ (_ , e₂↪e₂') = inj₂ (_ , ξ-∧₂ e₂↪e₂')
  ... | inj₂ (_ , e₁↪e₁') | _                 = inj₂ (_ , ξ-∧₁ e₁↪e₁')

open import Data.Bool.Base using (Bool; true; false; T; not)
open import Data.List.Base using (List; _∷_; [])
open import Data.Nat.Base using (ℕ; zero; suc)
open import Data.Product.Base using (∃-syntax; _×_)
open import Data.String using (String; _≟_)
open import Data.Unit.Base using (tt)
open import Relation.Nullary.Negation using (¬_; contradiction)
open import Relation.Nullary.Decidable using (Dec; yes; no; False; toWitnessFalse; ¬?)
open import Relation.Binary.PropositionalEquality using (_≡_; _≢_; refl)

Id : Set
Id = String

infix  5  ƛ_⇒_  μ_⇒_
infixl 7  _·_
infix  8  `suc_
infix  9  `_

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

module HowTheBookDoesIt where
  infix  2 _↪*_
  infix  1 begin_
  infixr 2 _↪⟨_⟩_
  infix  3 _∎

  data _↪*_ : Term → Term → Set where
    _∎ : ∀ M
        ---------
      → M ↪* M

    step↪ : ∀ L {M N}
      → M ↪* N
      → L ↪ M
        ---------
      → M ↪* N

  pattern _↪⟨_⟩_ L L↪M N↪*M = step↪ L N↪*M L↪M

  begin_ : ∀ {M N}
    → M ↪* N
      ------
    → M ↪* N
  begin M↪*N = M↪*N

module HowItShouldBeDone where
  infix  2 _↪*_

  data _↪*_ : Term → Term → Set where
    refl : ∀ {e} → e ↪* e
    step : ∀ {e₁ e₂ e₃} → e₁ ↪ e₂ → e₂ ↪* e₃ → e₁ ↪* e₃

  trans : ∀ {e₁ e₂ e₃} → e₁ ↪* e₂ → e₂ ↪* e₃ → e₁ ↪* e₃
  trans refl q = q
  trans (step x p) q = step x (trans p q)

  module ↪*-Reasoning where
    infix  1 begin_
    infixr 2 _↪⟨_⟩_  _≡⟨_⟩_
    infix  3 _∎

    begin_ : ∀ {e₁ e₂} → e₁ ↪* e₂ → e₁ ↪* e₂
    begin e₂↪*N = e₂↪*N

    _↪⟨_⟩_ : ∀ e₁ {e₂ e₃} → e₁ ↪ e₂ → e₂ ↪* e₃ → e₁ ↪* e₃
    e₁ ↪⟨ e₁↪e₂ ⟩ e₂↪*e₃ = step e₁↪e₂ e₂↪*e₃ 

    _≡⟨_⟩_ : ∀ e₁ {e₂ e₃} → e₁ ≡ e₂ → e₂ ↪* e₃ → e₁ ↪* e₃
    e₁ ≡⟨ refl ⟩ e₂↪*e₃ = e₂↪*e₃

    _∎ : ∀ e → e ↪* e
    e₂ ∎ = refl

open HowItShouldBeDone

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

data _⊢_⦂_ : Context → Term → Type → Set where

  -- Axiom
  ⊢` : ∀ {Γ x A} →
    Γ ∋ x ⦂ A →
    Γ ⊢ ` x ⦂ A

  -- ⇒-I
  ⊢ƛ : ∀ {Γ x N A B} →
    Γ , x ⦂ A ⊢ N ⦂ B →
    -------------------
    Γ ⊢ ƛ x ⇒ N ⦂ A ⇒ B

  -- ⇒-E
  _·_ : ∀ {Γ e₁ e₂ A B} →
    Γ ⊢ e₁ ⦂ A ⇒ B →
    Γ ⊢ e₂ ⦂ A →
    -------------
    Γ ⊢ e₁ · e₂ ⦂ B

  -- ℕ-I₁
  ⊢zero : ∀ {Γ} →
    --------------
    Γ ⊢ `zero ⦂ `ℕ

  -- ℕ-I₂
  ⊢suc : ∀ {Γ e₂} →
    Γ ⊢ e₂ ⦂ `ℕ →
    ----------------
    Γ ⊢ `suc e₂ ⦂ `ℕ

  -- ℕ-E
  ⊢case : ∀ {Γ e₁ e₂ x N A} →
    Γ ⊢ e₁ ⦂ `ℕ →
    Γ ⊢ e₂ ⦂ A →
    Γ , x ⦂ `ℕ ⊢ N ⦂ A →
    -------------------------------------
    Γ ⊢ case e₁ [zero⇒ e₂ |suc x ⇒ N ] ⦂ A

  ⊢μ : ∀ {Γ x e₂ A} →
    Γ , x ⦂ A ⊢ e₂ ⦂ A →
    -----------------
    Γ ⊢ μ x ⇒ e₂ ⦂ A

-- Type derivations correspond to trees. In informal notation, 
-- here is a type derivation for the Church numeral two,
-- 
--                         ∋s                     ∋z
--                         ------------------ ⊢`  -------------- ⊢`
-- ∋s                      Γ₂ ⊢ ` "s" ⦂ A ⇒ A     Γ₂ ⊢ ` "z" ⦂ A
-- ------------------ ⊢`   ------------------------------------- _·_
-- Γ₂ ⊢ ` "s" ⦂ A ⇒ A      Γ₂ ⊢ ` "s" · ` "z" ⦂ A
-- ---------------------------------------------- _·_
-- Γ₂ ⊢ ` "s" · (` "s" · ` "z") ⦂ A
-- -------------------------------------------- ⊢ƛ
-- Γ₁ ⊢ ƛ "z" ⇒ ` "s" · (` "s" · ` "z") ⦂ A ⇒ A
-- ------------------------------------------------------------- ⊢ƛ
-- Γ ⊢ ƛ "s" ⇒ ƛ "z" ⇒ ` "s" · (` "s" · ` "z") ⦂ (A ⇒ A) ⇒ A ⇒ A
-- 
-- where ∋s and ∋z abbreviate the two derivations,
-- 
--              ---------------- Z
-- "s" ≢ "z"    Γ₁ ∋ "s" ⦂ A ⇒ A
-- ----------------------------- S       ------------- Z
-- Γ₂ ∋ "s" ⦂ A ⇒ A                       Γ₂ ∋ "z" ⦂ A