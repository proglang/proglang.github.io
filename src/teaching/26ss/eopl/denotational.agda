module denotational where

open import Data.Empty using (⊥)
open import Data.Maybe using (Maybe; just; nothing)
open import Data.Nat using (ℕ; zero; suc)
open import Data.Product using (_×_; proj₁; proj₂; ∃-syntax) renaming (_,_ to ⟨_,_⟩)
open import Data.Sum using (_⊎_; inj₁; inj₂)
open import Data.String using (String; _≟_)
open import Data.Unit using (⊤; tt)
open import Function using (_∘_)
open import Relation.Binary.PropositionalEquality using (_≡_; _≢_; refl; cong; sym; trans)
open import Relation.Nullary using (¬_; contradiction)
open import Relation.Nullary.Decidable using (Dec; yes; no; False; toWitnessFalse; ¬?)

-- Operators -------------------------------------------------------------------

infix  4 _⊢_
infix  4 _∋_
infixl 5 _,_

infixr 7 _⇒_

infix  5 ƛ_
infixl 7 _·_
infix  8 `suc_
infix  9 `_
infix  9 S_

-- Syntax ----------------------------------------------------------------------

data Type : Set where
  _⇒_ : Type → Type → Type
  `ℕ : Type

data Context : Set where
  ∅   : Context
  _,_ : Context → Type → Context

variable
  A B C : Type
  Γ Δ : Context

-- Variable lookup (as before)
data _∋_ : Context → Type → Set where
  Z : ∀ {Γ} → Γ , A ∋ A
  S_ : ∀ {Γ} → Γ ∋ A → Γ , B ∋ A

-- Terms and typing
-- Same as before, except that we remove `μ` and replace `case` by `recnat`.
data _⊢_ : Context → Type → Set where
  `_ : ∀ {Γ A}
    → Γ ∋ A
    → Γ ⊢ A
  ƛ_  : ∀ {Γ A B}
    → Γ , A ⊢ B
    → Γ ⊢ A ⇒ B
  _·_ : ∀ {Γ A B}
    → Γ ⊢ A ⇒ B
    → Γ ⊢ A
    → Γ ⊢ B
  `zero : ∀ {Γ}
    → Γ ⊢ `ℕ
  `suc_ : ∀ {Γ}
    → Γ ⊢ `ℕ
    → Γ ⊢ `ℕ
  recnat : ∀ {Γ A}
    → Γ ⊢ `ℕ
    → Γ ⊢ A
    → Γ ⊢ `ℕ ⇒ A ⇒ A
    → Γ ⊢ A

-- Denotational Semantics ------------------------------------------------------

𝓣⟦_⟧ : Type → Set
𝓣⟦ A ⇒ B ⟧ = 𝓣⟦ A ⟧ → 𝓣⟦ B ⟧
𝓣⟦ `ℕ ⟧ = ℕ

𝓒⟦_⟧ : Context → Set
𝓒⟦ Γ ⟧ = ∀ A → Γ ∋ A → 𝓣⟦ A ⟧

extc : 𝓒⟦ Γ ⟧ → 𝓣⟦ A ⟧ → 𝓒⟦ Γ , A ⟧
extc γ a _ Z = a
extc γ a _ (S x) = γ _ x

recnat′ : ∀ {X : Set} → ℕ → (x₀ : X) → (sₛ : ℕ → X → X) → X
recnat′ zero x₀ xₛ = x₀
recnat′ (suc n) x₀ xₛ = xₛ n (recnat′ n x₀ xₛ)

𝓔⟦_⟧ : Γ ⊢ A → (𝓒⟦ Γ ⟧ → 𝓣⟦ A ⟧)
𝓔⟦ e ⟧ γ = {!   !}

-- Small-Step Semantics --------------------------------------------------------

-- Renamings

Ren : Context → Context → Set
Ren Γ Δ = ∀ {A} → Γ ∋ A → Δ ∋ A

extr : Ren Γ Δ → Ren (Γ , A) (Δ , A)
extr ρ Z = Z
extr ρ (S x) = S (ρ x)

rename : ∀ {Γ Δ} → Ren Γ Δ → Γ ⊢ A → Δ ⊢ A
rename ρ (` x) = ` (ρ x)
rename ρ (ƛ ⊢A) = ƛ rename (extr ρ) ⊢A
rename ρ (⊢A · ⊢A₁) = (rename ρ ⊢A) · (rename ρ ⊢A₁)
rename ρ `zero = `zero
rename ρ (`suc ⊢A) = `suc (rename ρ ⊢A)
rename ρ (recnat ⊢A ⊢A₁ ⊢A₂) = recnat (rename ρ ⊢A) (rename ρ ⊢A₁) (rename ρ ⊢A₂)

-- Substitutions

Sub : Context → Context → Set
Sub Γ Δ  = ∀ {A} → Γ ∋ A → Δ ⊢ A

exts : Sub Γ Δ → Sub (Γ , A) (Δ , A)
exts σ Z = ` Z
exts σ (S x) = rename S_ (σ x)

subst : ∀ {Γ Δ} → Sub Γ Δ → Γ ⊢ A → Δ ⊢ A
subst σ (` x) = σ x
subst σ (ƛ ⊢A) = ƛ subst (exts σ) ⊢A
subst σ (⊢A · ⊢A₁) = (subst σ ⊢A) · (subst σ ⊢A₁)
subst σ `zero = `zero
subst σ (`suc ⊢A) = `suc (subst σ ⊢A)
subst σ (recnat ⊢A ⊢A₁ ⊢A₂) = recnat (subst σ ⊢A) (subst σ ⊢A₁) (subst σ ⊢A₂)

-- Singleton Substitution

σ₀ : (M : Γ ⊢ B) → Sub (Γ , B) Γ
σ₀ M Z     = M
σ₀ M (S x) = ` x

_[_] : ∀ {Γ A B} → Γ , B ⊢ A → Γ ⊢ B → Γ ⊢ A
_[_] {Γ} {A} {B} N M = subst (σ₀ M) N

-- Values

data Value  {Γ} : ∀ {A} → Γ ⊢ A → Set where
  ƛ_    : (N : Γ , A ⊢ B) → Value (ƛ N)
  `zero : Value `zero
  `suc_ : ∀ {V : Γ ⊢ `ℕ} → Value V → Value (`suc V)

-- Reduction Relation

infix 2 _⟶_

data _⟶_ : ∀ {Γ A} → (Γ ⊢ A) → (Γ ⊢ A) → Set where
  ξ-·₁ : ∀ {Γ A B} {L L′ : Γ ⊢ A ⇒ B} {M : Γ ⊢ A}
    → L ⟶ L′
    → L · M ⟶ L′ · M
  ξ-·₂ : ∀ {Γ A B} {V : Γ ⊢ A ⇒ B} {M M′ : Γ ⊢ A}
    → Value V
    → M ⟶ M′
    → V · M ⟶ V · M′
  β-ƛ : ∀ {Γ A B} {N : Γ , A ⊢ B} {W : Γ ⊢ A}
    → Value W
    → (ƛ N) · W ⟶ N [ W ]
  ξ-suc : ∀ {Γ} {M M′ : Γ ⊢ `ℕ}
    → M ⟶ M′
    → `suc M ⟶ `suc M′
  ξ-recnat : ∀ {Γ A} {L L′ : Γ ⊢ `ℕ} {M : Γ ⊢ A} {N : Γ  ⊢ `ℕ ⇒ A ⇒ A}
    → L ⟶ L′
    → recnat L M N ⟶ recnat L′ M N
  β-zero :  ∀ {Γ A} {M : Γ ⊢ A} {N : Γ ⊢ `ℕ ⇒ A ⇒ A}
    → recnat `zero M N ⟶ M
  β-suc : ∀ {Γ A} {V : Γ ⊢ `ℕ} {M : Γ ⊢ A} {N : Γ ⊢ `ℕ ⇒ A ⇒ A}
    → Value V
    → recnat (`suc V) M N ⟶ N · V · recnat V M N

-- Relation between small-step and denotational semantics -------------------------

postulate
  ext : ∀ {A : Set}{B : A → Set} {f g : (a : A) → B a} → (∀ x → f x ≡ g x) → f ≡ g

𝓡⟦_⟧ : Ren Γ Δ → 𝓒⟦ Δ ⟧ → 𝓒⟦ Γ ⟧
𝓡⟦ ρ ⟧ δ _ x = δ _ (ρ x)

extc-ρ : ∀ {v : 𝓣⟦ A ⟧} (δ : 𝓒⟦ Δ ⟧) (ρ : Ren Γ Δ)
  → extc (𝓡⟦ ρ ⟧ δ) v ≡ 𝓡⟦ extr ρ ⟧ (extc δ v)
extc-ρ δ ρ = {!   !}

sound-ren : ∀ (M : Γ ⊢ A) (δ : 𝓒⟦ Δ ⟧) (ρ : Ren Γ Δ)
  → 𝓔⟦ M ⟧ (𝓡⟦ ρ ⟧ δ) ≡ 𝓔⟦ rename ρ M ⟧ δ
sound-ren e δ ρ = {!   !}

--      Sub Γ Δ → Sub Δ ∅ → Sub Γ ∅
𝓢⟦_⟧ : Sub Γ Δ → 𝓒⟦ Δ ⟧ → 𝓒⟦ Γ ⟧
𝓢⟦ σ ⟧ δ _ x = 𝓔⟦ σ x ⟧ δ

extc-exts : ∀ {v : 𝓣⟦ A ⟧} → (σ : Sub Γ Δ) (δ : 𝓒⟦ Δ ⟧)
  → extc {A = A} (𝓢⟦ σ ⟧ δ) v ≡ 𝓢⟦ exts σ ⟧ (extc {A = A} δ v)
extc-exts {v = v} σ δ = {!   !}

sound-sub : (M : Γ ⊢ A) (σ : Sub Γ Δ) (δ : 𝓒⟦ Δ ⟧)
  → 𝓔⟦ M ⟧ (𝓢⟦ σ ⟧ δ) ≡ 𝓔⟦ subst σ M ⟧ δ
sound-sub e σ δ = {!   !}

extc-σ₀ : (γ  : 𝓒⟦ Γ ⟧) (W  : Γ ⊢ A) → extc γ (𝓔⟦ W ⟧ γ) ≡ 𝓢⟦ σ₀ W ⟧ γ
extc-σ₀ γ W = {!   !}

sound⟶ : ∀ {M N : Γ ⊢ A} → M ⟶ N → (γ : 𝓒⟦ Γ ⟧) → 𝓔⟦ M ⟧ γ ≡ 𝓔⟦ N ⟧ γ
sound⟶ M⟶N γ = {!   !}