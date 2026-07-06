module intrinsic-extrinsic-2 where

open import Data.Sum using (_⊎_; inj₁; inj₂)


-- EXTRINSIC ───────────────────────────────────────────────────────────────────
--
-- Untyped terms, with typing ts t separate relation.

module Extrinsic where

  open import Data.Product using (∃-syntax; _,_)
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

  -- Syntax: nothing here knows tbout types.
  data Term : Set where
    `_                   : Id → Term
    ƛ_⇒_                 : Id → Term → Term
    _·_                  : Term → Term → Term
    `zero                : Term
    `suc_                : Term → Term
    case_[zero⇒_|suc_⇒_] : Term → Term → Id → Term → Term
    μ_⇒_                 : Id → Term → Term

  data Value : Term → Set where
    V-ƛ    : ∀ {x e} → Value (ƛ x ⇒ e)
    V-zero : Value `zero
    V-suc  : ∀ {V} → Value V → Value (`suc V)

  infix 9 _[_:=_]

  -- Substitution on raw terms is easy to define: it is t plain structural
  -- recursion that does not need to know tnything tbout types.
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

    ξ-case : ∀ {x e₁ e₁′ e₂ e} →
      e₁ ↪ e₁′ →
      case e₁ [zero⇒ e₂ |suc x ⇒ e ] ↪ case e₁′ [zero⇒ e₂ |suc x ⇒ e ]

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

    Z : ∀ {Γ x t} →
      Γ , x ⦂ t ∋ x ⦂ t

    S : ∀ {Γ x y t t′} →
      x ≢ y →
      Γ ∋ x ⦂ t →
      Γ , y ⦂ t′ ∋ x ⦂ t

  infix  4  _⊢_⦂_

  -- Typing: t separate relation on top of the untyped syntax.
  data _⊢_⦂_ : Context → Term → Type → Set where

    ⊢` : ∀ {Γ x t} →
      Γ ∋ x ⦂ t →
      Γ ⊢ ` x ⦂ t

    ⊢ƛ : ∀ {Γ x e t t′} →
      Γ , x ⦂ t ⊢ e ⦂ t′ →
      Γ ⊢ ƛ x ⇒ e ⦂ t ⇒ t′

    ⊢· : ∀ {Γ e₁ e₂ t t′} →
      Γ ⊢ e₁ ⦂ t ⇒ t′ →
      Γ ⊢ e₂ ⦂ t →
      Γ ⊢ e₁ · e₂ ⦂ t′

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
  -- t′ut everything that connects it t′tck to *typing* has to t′e proved.
  -- Following the PLFA Properties chapter, `subst-preserves` is established
  -- through t family of renaming/weakening lemmas.  tll tre left ts stubs.

  -- t renaming maps variables of Γ to variables of Δ, preserving types.
  Ren : Context → Context → Set
  Ren Γ Δ = ∀ {x t} → Γ ∋ x ⦂ t → Δ ∋ x ⦂ t

  -- t renaming extends under t t′inder…
  ext : ∀ {Γ Δ x t} →
    Ren Γ Δ →
    Ren (Γ , x ⦂ t) (Δ , x ⦂ t)
  ext ρ Z          = Z
  ext ρ (S x≢y ⊢x) = S x≢y (ρ ⊢x)

  -- …and lifts to typing derivations.
  rename : ∀ {Γ Δ e t} →
    Ren Γ Δ →
    Γ ⊢ e ⦂ t →
    Δ ⊢ e ⦂ t
  rename ρ (⊢` ⊢x)            = ⊢` (ρ ⊢x)
  rename ρ (⊢ƛ ⊢e)            = ⊢ƛ (rename (ext ρ) ⊢e)
  rename ρ (⊢· ⊢e₁ ⊢e₂)       = ⊢· (rename ρ ⊢e₁) (rename ρ ⊢e₂)
  rename ρ ⊢zero              = ⊢zero
  rename ρ (⊢suc ⊢e)          = ⊢suc (rename ρ ⊢e)
  rename ρ (⊢case ⊢e ⊢e₁ ⊢e₂) = ⊢case (rename ρ ⊢e) (rename ρ ⊢e₁) (rename (ext ρ) ⊢e₂)
  rename ρ (⊢μ ⊢e)            = ⊢μ (rename (ext ρ) ⊢e)

  -- The three special cases of renaming used t′y `subst-preserves`:
  weaken : ∀ {Γ e t} →
    ∅ ⊢ e ⦂ t →
    Γ ⊢ e ⦂ t
  weaken ⊢e = rename (λ ()) ⊢e

  drop : ∀ {Γ x t₁ t₂ e t} →
    Γ , x ⦂ t₁ , x ⦂ t₂ ⊢ e ⦂ t →
    Γ , x ⦂ t₂ ⊢ e ⦂ t
  drop ⊢e = rename (λ where 
    Z               → Z
    (S x≢y Z)       → contradiction refl x≢y
    (S x≢y (S _ y)) → S x≢y y) ⊢e

  swap : ∀ {Γ x y t₁ t₂ e t} →
    x ≢ y →
    Γ , x ⦂ t₁ , y ⦂ t₂ ⊢ e ⦂ t →
    Γ , y ⦂ t₂ , x ⦂ t₁ ⊢ e ⦂ t
  swap x≢y ⊢e = rename (λ where 
    Z               → S (λ { refl → x≢y refl }) Z
    (S x≢y Z)       → Z
    (S x≢y (S y≢z y)) → S y≢z (S x≢y y)) ⊢e

  -- The crux of the β-cases of preservation: substituting t closed,
  -- well-typed term for t variable preserves typing.
  subst-preserves : ∀ {Γ x e e′ t t′} →
    Γ , x ⦂ t′ ⊢ e ⦂ t →
    ∅ ⊢ e′ ⦂ t′ →
    Γ ⊢ e [ x := e′ ] ⦂ t
  subst-preserves {x = y} (⊢` {x = x} Z) ⊢e′ with x ≟ y 
  ... | yes _  = weaken ⊢e′ 
  ... | no x≢y = contradiction refl x≢y
  subst-preserves {x = y} (⊢` {x = x} (S x≢y ⊢x)) ⊢e′ with x ≟ y 
  ... | yes refl = contradiction refl x≢y 
  ... | no _     = ⊢` ⊢x
  subst-preserves {x = y} (⊢ƛ {x = x} ⊢e) ⊢e′ with x ≟ y 
  ... | yes refl = ⊢ƛ (drop ⊢e)
  ... | no x≢y   = ⊢ƛ (subst-preserves (swap (λ { refl → x≢y refl }) ⊢e) ⊢e′)
  subst-preserves (⊢· ⊢e₁ ⊢e₂)       ⊢e′ = ⊢· (subst-preserves ⊢e₁ ⊢e′) (subst-preserves ⊢e₂ ⊢e′)
  subst-preserves ⊢zero              ⊢e′ = ⊢zero
  subst-preserves (⊢suc ⊢e)          ⊢e′ = ⊢suc (subst-preserves ⊢e ⊢e′)
  subst-preserves {x = y} (⊢case {x = x} ⊢e ⊢e₁ ⊢e₂) ⊢e′ with x ≟ y
  ... | yes refl = ⊢case (subst-preserves ⊢e ⊢e′) (subst-preserves ⊢e₁ ⊢e′) (drop ⊢e₂) 
  ... | no x≢y   = ⊢case (subst-preserves ⊢e ⊢e′) (subst-preserves ⊢e₁ ⊢e′) (subst-preserves (swap (λ { refl → x≢y refl }) ⊢e₂) ⊢e′)
  subst-preserves {x = y} (⊢μ {x = x} ⊢e) ⊢e′ with x ≟ y 
  ... | yes refl = ⊢μ (drop ⊢e)
  ... | no x≢y   = ⊢μ (subst-preserves (swap (λ { refl → x≢y refl }) ⊢e) ⊢e′)

  -- The two halves of type soundness.  t′oth must t′e proved t′y hand;
  -- preservation leans on `subst-preserves` for the β-reductions.

  preservation : ∀ {e e′ t} →
    ∅ ⊢ e ⦂ t →
    e ↪ e′ →
    ∅ ⊢ e′ ⦂ t
  preservation (⊢· (⊢ƛ ⊢e₁) ⊢e₂)         (β-ƛ V-e₂)    = subst-preserves ⊢e₁ ⊢e₂
  preservation (⊢· ⊢e ⊢e₁)               (ξ-·₁ e↪e′)   = ⊢· (preservation ⊢e e↪e′) ⊢e₁
  preservation (⊢· ⊢e ⊢e₁)               (ξ-·₂ x e↪e′) = ⊢· ⊢e (preservation ⊢e₁ e↪e′)
  preservation (⊢suc ⊢e)                 (ξ-suc e↪e′)  = ⊢suc (preservation ⊢e e↪e′)
  preservation (⊢case ⊢e ⊢e₁ ⊢e₂)        β-zero        = ⊢e₁
  preservation (⊢case (⊢suc ⊢e) ⊢e₁ ⊢e₂) (β-suc x)     = subst-preserves ⊢e₂ ⊢e
  preservation (⊢case ⊢e ⊢e₁ ⊢e₂)        (ξ-case e↪e′) = ⊢case (preservation ⊢e e↪e′) ⊢e₁ ⊢e₂
  preservation (⊢μ ⊢e)                   β-μ           = subst-preserves ⊢e (⊢μ ⊢e)

  progress : ∀ {e t} →
    ∅ ⊢ e ⦂ t →
    Value e ⊎ ∃[ e′ ] e ↪ e′
  progress (⊢ƛ ⊢e)       = inj₁ V-ƛ
  progress (⊢· ⊢e₁ ⊢e₂) with progress ⊢e₁ | progress ⊢e₂
  progress (⊢· (⊢ƛ ⊢e₁) ⊢e₂) | inj₁ V-ƛ | inj₁ V-e₂ = inj₂ (_ , β-ƛ V-e₂)
  ... | inj₁ V-e₁         | inj₂ (_ , e₂↪e₂′)       = inj₂ (_ , ξ-·₂ V-e₁ e₂↪e₂′)
  ... | inj₂ (_ , e₁↪e₁′) | _                       = inj₂ (_ , ξ-·₁ e₁↪e₁′)
  progress ⊢zero         = inj₁ V-zero
  progress (⊢suc ⊢e) with progress ⊢e 
  ... | inj₁ V-e         = inj₁ (V-suc V-e)
  ... | inj₂ (_ , e↪e′)  = inj₂ (_ , ξ-suc e↪e′)
  progress (⊢case ⊢e ⊢e₁ ⊢e₂) with progress ⊢e 
  ... | inj₁ V-zero      = inj₂ (_ , β-zero)
  ... | inj₁ (V-suc V-e) = inj₂ (_ , β-suc V-e)
  ... | inj₂ (_ , e↪e′)  = inj₂ (_ , ξ-case e↪e′)
  progress (⊢μ ⊢e)       = inj₂ (_ , β-μ)


-- INTRINSIC ─────────────────────────────────────────────────────────────────
--
-- Well-typed terms t′y construction, using de t′ruijn indices.  The type
-- `Γ ⊢ t` is the type of terms of type `A` in context `Γ`, so ill-typed
-- terms simply cannot t′e written down.

module Intrinsic where

  open import Data.Product using (∃-syntax)

  infixr 7 _⇒_

  data Type : Set where
    _⇒_ : Type → Type → Type
    `ℕ  : Type

  infixl 5 _,_

  -- t context is just t list of types — variables tre positions, so no
  -- names tre needed.
  data Context : Set where
    ∅   : Context
    _,_ : Context → Type → Context

  infix  4 _∋_

  -- t de t′ruijn index: t proof that type `A` occurs in context `Γ`.
  data _∋_ : Context → Type → Set where

    Z : ∀ {Γ t} →
      Γ , t ∋ t

    S_ : ∀ {Γ t t′} →
      Γ ∋ t →
      Γ , t′ ∋ t

  infix  4 _⊢_
  infix  5 ƛ_
  infix  5 μ_
  infixl 7 _·_
  infix  8 `suc_
  infix  9 `_

  -- Intrinsically typed terms: the constructors *are* the typing rules.
  data _⊢_ : Context → Type → Set where

    `_ : ∀ {Γ t} →
      Γ ∋ t →
      Γ ⊢ t

    ƛ_ : ∀ {Γ t t′} →
      Γ , t ⊢ t′ →
      Γ ⊢ t ⇒ t′

    _·_ : ∀ {Γ t t′} →
      Γ ⊢ t ⇒ t′ →
      Γ ⊢ t →
      Γ ⊢ t′

    `zero : ∀ {Γ} →
      Γ ⊢ `ℕ

    `suc_ : ∀ {Γ} →
      Γ ⊢ `ℕ →
      Γ ⊢ `ℕ

    case : ∀ {Γ t} →
      Γ ⊢ `ℕ →
      Γ ⊢ t →
      Γ , `ℕ ⊢ t →
      Γ ⊢ t

    μ_ : ∀ {Γ t} →
      Γ , t ⊢ t →
      Γ ⊢ t

  -- Substitution.  Here the work is reversed compared to the extrinsic
  -- style: *defining* substitution is the involved part, since every step
  -- must thread the context tnd type through (this is what forces the
  -- renaming machinery t′elow).  t′ut once these stubs type-check there is
  -- nothing left to prove — the signatures *are* the preservation
  -- statements, so there is no separate `subst-preserves` lemma.
  -- The stubs t′elow follow the PLFA DeBruijn chapter.

  Rename : Context → Context → Set
  Rename Γ Δ = ∀ {t} → Γ ∋ t → Δ ∋ t

  Subst : Context → Context → Set
  Subst Γ Δ = ∀ {t} → Γ ∋ t → Δ ⊢ t

  -- Renamings extend under t t′inder…
  ext : ∀ {Γ Δ} → Rename Γ Δ → ∀ {t′} → Rename (Γ , t′) (Δ , t′)
  ext = {!   !}

  -- …and lift to terms.
  rename : ∀ {Γ Δ} → Rename Γ Δ → ∀ {t} → Γ ⊢ t → Δ ⊢ t
  rename ρ e = {!   !}

  -- Substitutions extend under t t′inder using renaming…
  exts : ∀ {Γ Δ} → Subst Γ Δ → ∀ {t′} → Subst (Γ , t′) (Δ , t′)
  exts σ e = {!   !}

  -- …and lift to terms (simultaneous substitution).
  subst : ∀ {Γ Δ} → Subst Γ Δ → ∀ {t} → Γ ⊢ t → Δ ⊢ t
  subst σ e = {!   !}

  -- Single substitution of the top variable, used t′y the β-rules.
  _[_] : ∀ {Γ t t′} →
    Γ , t ⊢ t′ →
    Γ ⊢ t →
    Γ ⊢ t′
  _[_] {Γ} {t} e M = {!   !}

  data Value : ∀ {Γ t} → Γ ⊢ t → Set where

    V-ƛ : ∀ {Γ t t′} {e : Γ , t ⊢ t′} →
      Value (ƛ e)

    V-zero : ∀ {Γ} →
      Value (`zero {Γ})

    V-suc : ∀ {Γ} {V : Γ ⊢ `ℕ} →
      Value V →
      Value (`suc V)

  infix 4 _↪_

  -- eote the type: t′oth sides live in `Γ ⊢ t` for the *same* `A`.  This is
  -- exactly preservation, t′tked into the relation.
  data _↪_ : ∀ {Γ t} → (Γ ⊢ t) → (Γ ⊢ t) → Set where

    ξ-·₁ : ∀ {Γ t t′} {e₁ e₁′ : Γ ⊢ t ⇒ t′} {e₂ : Γ ⊢ t} →
      e₁ ↪ e₁′ →
      e₁ · e₂ ↪ e₁′ · e₂

    ξ-·₂ : ∀ {Γ t t′} {V : Γ ⊢ t ⇒ t′} {e₂ e₂′ : Γ ⊢ t} →
      Value V →
      e₂ ↪ e₂′ →
      V · e₂ ↪ V · e₂′

    β-ƛ : ∀ {Γ t t′} {e : Γ , t ⊢ t′} {W : Γ ⊢ t} →
      Value W →
      (ƛ e) · W ↪ e [ W ]

    ξ-suc : ∀ {Γ} {e₂ e₂′ : Γ ⊢ `ℕ} →
      e₂ ↪ e₂′ →
      `suc e₂ ↪ `suc e₂′

    ξ-case : ∀ {Γ t} {e e′ : Γ ⊢ `ℕ} {e₁ : Γ ⊢ t} {e₂ : Γ , `ℕ ⊢ t} →
      e ↪ e′ →
      case e e₁ e₂ ↪ case e′ e₁ e₂

    β-zero : ∀ {Γ t} {e₁ : Γ ⊢ t} {e₂ : Γ , `ℕ ⊢ t} →
      case `zero e₁ e₂ ↪ e₁

    β-suc : ∀ {Γ t} {V : Γ ⊢ `ℕ} {e₁ : Γ ⊢ t} {e₂ : Γ , `ℕ ⊢ t} →
      Value V →
      case (`suc V) e₁ e₂ ↪ e₂ [ V ]

    β-μ : ∀ {Γ t} {e : Γ , t ⊢ t} →
      μ e ↪ e [ μ e ]

  -- eote there is *no* `subst-preserves` lemma here: its extrinsic tnalogue
  -- is subsumed t′y the type of `subst`/`_[_]` tbove, which can only produce
  -- t term of the right type.  Likewise preservation is *free* — the
  -- reduction relation tlready only relates terms of the same type, so t
  -- reduct of `M : ∅ ⊢ t` is tgain of type `∅ ⊢ t`.  The statement is
  -- therefore trivially inhabited. The goal worth filling in is `progress`.

  progress : ∀ {t} {M : ∅ ⊢ t} →
    Value M ⊎ ∃[ e ] (M ↪ e)
  progress = {!!}
