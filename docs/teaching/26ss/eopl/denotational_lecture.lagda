	-*- mode: agda2;-*-

```
module denotational_lecture where
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
```

# Towards denotational semantics

To ensure that we can choose sets (i.e., plain Agda types) as semantics domains,
we remove the fixpoint operator `μ` from the calculus and replace the `case` on
natural numbers with a *recursor* called `recnat`. The recursor implements primitive recursion,
which ensures termination.


```
infix  4 _⊢_
infix  4 _∋_
infixl 5 _,_
infixr 7 _⇒_
infix  5 ƛ_
infixl 7 _·_
infix  8 `suc_
infix  9 `_
infix  9 S_
```

## Syntax

## Simple Types (as before)

```
data Type : Set where
  _⇒_ : Type → Type → Type
  `ℕ : Type

variable
  A B C : Type
```

## Contexts (as before)

```
data Context : Set where
  ∅   : Context
  _,_ : Context → Type → Context

variable
  Γ Δ : Context
```

## Variable lookup (as before)

```
data _∋_ : Context → Type → Set where

  Z : ∀ {Γ}
      ---------
    → Γ , A ∋ A

  S_ : ∀ {Γ}
    → Γ ∋ A
      ---------
    → Γ , B ∋ A
```

## Terms and typing

Same as before, except that we remove `μ` and replace `case` by `recnat`.

```
data _⊢_ : Context → Type → Set where

  `_ : ∀ {Γ A}
    → Γ ∋ A
      -----
    → Γ ⊢ A

  ƛ_  : ∀ {Γ A B}
    → Γ , A ⊢ B
      ---------
    → Γ ⊢ A ⇒ B

  _·_ : ∀ {Γ A B}
    → Γ ⊢ A ⇒ B
    → Γ ⊢ A
      ---------
    → Γ ⊢ B

  `zero : ∀ {Γ}
      ---------
    → Γ ⊢ `ℕ

  `suc_ : ∀ {Γ}
    → Γ ⊢ `ℕ
      ------
    → Γ ⊢ `ℕ

  recnat : ∀ {Γ A}
    → Γ ⊢ `ℕ
    → Γ ⊢ A
    → Γ ⊢ `ℕ ⇒ A ⇒ A
      ---------------
    → Γ ⊢ A
```

We encode `recnat` differently to the prior `case`. The `suc` branch of the `case` assumed
a context extended with the predecessor. Equivalently, we could have asked for he `suc` branch
to be a function of type `ℕ ⇒ A`.
For the `recnat`, we would have to extend the context with two types, one for the predecesssor
and one for the result of the recursive call.
Here we use a function because the double extension is awkward to handle.

To explain `recnat`, we consider the reduction rules informally.

1.  `recnat zero M N` reduces to `M`
    ... just like `case`
2.  `recnat (suc V) M N` reduces to `N · V · recnat V M N`
    we first pass the predecessor and then the result of the recursive call on the predecessor

In a first step towards defining the semantics, we define the semantics of `recnat`
as an Agda function. It is related to primitive recursion.

```
recnat′ : ∀ {X : Set} → ℕ → (x₀ : X) → (sₛ : ℕ → X → X) → X
recnat′ zero x₀ xₛ = x₀
recnat′ (suc n) x₀ xₛ = xₛ n (recnat′ n x₀ xₛ)
```

Some example terms

```
two′ : ℕ
two′ = 2

three′ : ℕ
three′ = 3

plus′ : ℕ → ℕ → ℕ
plus′ m n = recnat′ m n (λ _ r → suc r)

mult′ : ℕ → ℕ → ℕ
mult′ m n = recnat′ m zero (λ _ r → plus′ n r) 
```

and in agda...:

```
two : Γ ⊢ `ℕ
two = `suc `suc `zero

three : Γ ⊢ `ℕ
three = `suc `suc `suc `zero

plus : Γ ⊢ `ℕ ⇒ `ℕ ⇒ `ℕ
plus = ƛ ƛ recnat (` (S Z)) (` Z) (ƛ ƛ `suc (` Z))

mult : Γ ⊢ `ℕ ⇒ `ℕ ⇒ `ℕ
mult = ƛ ƛ recnat (` (S Z)) `zero (ƛ ƛ (plus · ` (S (S Z))) · ` Z)
```



















## Denotational semantics

The semantic domain of a type is defined by induction.

```
𝓣⟦_⟧ : Type → Set
𝓣⟦ A ⇒ B ⟧ = 𝓣⟦ A ⟧ → 𝓣⟦ B ⟧
𝓣⟦ `ℕ ⟧ = ℕ
```

We also need a semantics of typing contexts, which are modeled analogous to substitutions and renamings.

```
module classical where
  -- the classical interpretation of contexts is by nested pairs
  -- but it doesnt match the function representation for substitutions.
  𝓒⟦_⟧ : Context → Set
  𝓒⟦ ∅ ⟧ = ⊤
  𝓒⟦ Γ , A ⟧ = 𝓒⟦ Γ ⟧ × 𝓣⟦ A ⟧


𝓒⟦_⟧ : Context → Set
𝓒⟦ Γ ⟧ = ∀ A → Γ ∋ A → 𝓣⟦ A ⟧

extc : 𝓒⟦ Γ ⟧ → 𝓣⟦ A ⟧ → 𝓒⟦ Γ , A ⟧
extc γ a _ Z = a
extc γ a _ (S x) = γ _ x
```

The semantics of a term is defined by induction on terms.
As the definition is compositional we have to provide semantics for
*open terms*. Hence, the semantics of a term of type `Γ ⊢ A` is a *function*
that maps an element of the context semantics of `Γ` (a semantic environment)
to an element of the type semantics of the return type `A`.

```
𝓔⟦_⟧ : Γ ⊢ A → 𝓒⟦ Γ ⟧ → 𝓣⟦ A ⟧
𝓔⟦ ` x ⟧ γ             = γ _ x
𝓔⟦ ƛ_ {A = A} M ⟧ γ    = λ (v : 𝓣⟦ A ⟧) → 𝓔⟦ M ⟧ (extc γ v)
𝓔⟦ M · M₁ ⟧ γ          = 𝓔⟦ M ⟧ γ (𝓔⟦ M₁ ⟧ γ)  
𝓔⟦ `zero ⟧ γ           = zero
𝓔⟦ `suc M ⟧ γ          = suc (𝓔⟦ M ⟧ γ)
𝓔⟦ recnat M M₁ M₂ ⟧ γ  = recnat′ (𝓔⟦ M ⟧ γ) (𝓔⟦ M₁ ⟧ γ) (𝓔⟦ M₂ ⟧ γ)
```

Run our examples!

```
γ∅ : 𝓒⟦ ∅ ⟧
γ∅ _ ()

_ : 𝓔⟦ two ⟧ γ∅ ≡ 2
_ = refl

_ : 𝓔⟦ plus · two · two ⟧ γ∅ ≡ 4
_ = refl

_ : 𝓔⟦ mult · two · three ⟧ γ∅ ≡ 6
_ = refl

_ : 𝓔⟦ mult ⟧ γ∅ (𝓔⟦ two ⟧ γ∅) (𝓔⟦ three ⟧ γ∅) ≡ 6
_ = refl


γ1 : 𝓒⟦ ∅ , `ℕ ⟧
γ1 _ Z = 5

_ : 𝓔⟦ ` Z ⟧ γ1 ≡ 5
_ = refl
```




To compare with an operational semantics, we need to recapitulate some of the definitions
of the last chapter.





## Revised small-step semantics


### Renaming

As before, a renaming is a mapping between variable lookups in different environments:

```
Ren : Context → Context → Set
Ren Γ Δ = ∀ {A} → Γ ∋ A → Δ ∋ A
```

Extend a renaming to adapt to an extra binding.

```
extr : Ren Γ Δ → Ren (Γ , A) (Δ , A)
extr ρ Z = Z
extr ρ (S x) = S (ρ x)
```

We apply a renaming to a term.

```
rename : ∀ {Γ Δ}
  → Ren Γ Δ
  → Γ ⊢ A
  → Δ ⊢ A
rename ρ (` x) = ` (ρ x)
rename ρ (ƛ ⊢A) = ƛ rename (extr ρ) ⊢A
rename ρ (⊢A · ⊢A₁) = (rename ρ ⊢A) · (rename ρ ⊢A₁)
rename ρ `zero = `zero
rename ρ (`suc ⊢A) = `suc (rename ρ ⊢A)
rename ρ (recnat ⊢A ⊢A₁ ⊢A₂) = recnat (rename ρ ⊢A) (rename ρ ⊢A₁) (rename ρ ⊢A₂)
```

### Substitution

A substitution from Γ to Δ maps any variable of type `A` in an environment `Γ` to a term in environment Δ.

```
Sub : Context → Context → Set
Sub Γ Δ  = ∀ {A} → Γ ∋ A → Δ ⊢ A
```

Extension for substitution.

```
exts : Sub Γ Δ → Sub (Γ , A) (Δ , A)
exts σ Z = ` Z
exts σ (S x) = rename S_ (σ x)
```

We apply a substitution to a term.

```
subst : ∀ {Γ Δ}
  → Sub Γ Δ
  → Γ ⊢ A
  → Δ ⊢ A
subst σ (` x) = σ x
subst σ (ƛ ⊢A) = ƛ subst (exts σ) ⊢A
subst σ (⊢A · ⊢A₁) = (subst σ ⊢A) · (subst σ ⊢A₁)
subst σ `zero = `zero
subst σ (`suc ⊢A) = `suc (subst σ ⊢A)
subst σ (recnat ⊢A ⊢A₁ ⊢A₂) = recnat (subst σ ⊢A) (subst σ ⊢A₁) (subst σ ⊢A₂)
```

### special case: single substitution

Required for type preservation / β reduction

```
σ₀ : (M : Γ ⊢ B) → Sub (Γ , B) Γ
σ₀ M Z = M
σ₀ M (S x) = ` x

_[_] : ∀ {Γ A B}
  → Γ , B ⊢ A
  → Γ ⊢ B
    ---------
  → Γ ⊢ A
_[_] {Γ} {A} {B} N M = subst (σ₀ M) N
```

### Values

```
data Value  {Γ} : ∀ {A} → Γ ⊢ A → Set where

  ƛ_ : (N : Γ , A ⊢ B)
      ---------------------------
    → Value (ƛ N)

  `zero : 
      -----------------
      Value `zero

  `suc_ : ∀ {V : Γ ⊢ `ℕ}
    → Value V
      --------------
    → Value (`suc V)
```

### Reduction

Due to the intrinsic, Church-style encoding, reduction comes with proof of type preservation by construction!

```
infix 2 _⟶_

data _⟶_ : ∀ {Γ A} → (Γ ⊢ A) → (Γ ⊢ A) → Set where

  ξ-·₁ : ∀ {Γ A B} {L L′ : Γ ⊢ A ⇒ B} {M : Γ ⊢ A}
    → L ⟶ L′
      ---------------
    → L · M ⟶ L′ · M

  ξ-·₂ : ∀ {Γ A B} {V : Γ ⊢ A ⇒ B} {M M′ : Γ ⊢ A}
    → Value V
    → M ⟶ M′
      ---------------
    → V · M ⟶ V · M′

  β-ƛ : ∀ {Γ A B} {N : Γ , A ⊢ B} {W : Γ ⊢ A}
    → Value W
      --------------------
    → (ƛ N) · W ⟶ N [ W ]

  ξ-suc : ∀ {Γ} {M M′ : Γ ⊢ `ℕ}
    → M ⟶ M′
      -----------------
    → `suc M ⟶ `suc M′

  ξ-recnat : ∀ {Γ A} {L L′ : Γ ⊢ `ℕ} {M : Γ ⊢ A} {N : Γ  ⊢ `ℕ ⇒ A ⇒ A}
    → L ⟶ L′
      -------------------------
    → recnat L M N ⟶ recnat L′ M N

  β-zero :  ∀ {Γ A} {M : Γ ⊢ A} {N : Γ ⊢ `ℕ ⇒ A ⇒ A}
      -------------------
    → recnat `zero M N ⟶ M

  β-suc : ∀ {Γ A} {V : Γ ⊢ `ℕ} {M : Γ ⊢ A} {N : Γ ⊢ `ℕ ⇒ A ⇒ A}
    → Value V
      ----------------------------
    → recnat (`suc V) M N ⟶ N · V · recnat V M N
```

## Relation of small-step reduction to the denotational semantics

Soundness of small-step reduction:
Taking a step in the small-step reduction does not change the denotation.

```
sound⟶ : ∀ {M N : Γ ⊢ A} → M ⟶ N → (γ : 𝓒⟦ Γ ⟧) → 𝓔⟦ M ⟧ γ ≡ 𝓔⟦ N ⟧ γ
```




Renamings acting on semantic substitutions

```
postulate
  ext : ∀ {A : Set}{B : A → Set} {f g : (a : A) → B a} → (∀ x → f x ≡ g x) → f ≡ g


𝓡⟦_⟧ : Ren Γ Δ → 𝓒⟦ Δ ⟧ → 𝓒⟦ Γ ⟧
𝓡⟦ ρ ⟧ δ _ x = δ _ (ρ x)


extc-ρ : ∀ {v : 𝓣⟦ A ⟧} (δ : 𝓒⟦ Δ ⟧) (ρ : Ren Γ Δ)
  → extc (𝓡⟦ ρ ⟧ δ) v ≡ 𝓡⟦ extr ρ ⟧ (extc δ v)

extc-ρ δ ρ = ext λ B → ext λ{ Z → refl ; (S x) → refl }

sound-ren : ∀ (M : Γ ⊢ A) (δ : 𝓒⟦ Δ ⟧) (ρ : Ren Γ Δ)
  → 𝓔⟦ M ⟧ (𝓡⟦ ρ ⟧ δ) ≡ 𝓔⟦ rename ρ M ⟧ δ

sound-ren (` x) δ ρ = refl
sound-ren (ƛ M) δ ρ = ext (λ v → trans (cong 𝓔⟦ M ⟧ (extc-ρ δ ρ)) (sound-ren M (extc δ v) (extr ρ)))
sound-ren (M · M₁) δ ρ rewrite sound-ren M δ ρ | sound-ren M₁ δ ρ = refl
sound-ren `zero δ ρ = refl
sound-ren (`suc M) δ ρ  rewrite sound-ren M δ ρ = refl
sound-ren (recnat M M₁ M₂) δ ρ rewrite sound-ren M δ ρ | sound-ren M₁ δ ρ | sound-ren M₂ δ ρ = refl
```

Syntactic substitutions acting on semantics substitutions

```
𝓢⟦_⟧ : Sub Γ Δ → 𝓒⟦ Δ ⟧ → 𝓒⟦ Γ ⟧
𝓢⟦ σ ⟧ δ _ x = 𝓔⟦ σ x ⟧ δ

extc-exts : ∀ {v : 𝓣⟦ A ⟧} → (σ : Sub Γ Δ) (δ : 𝓒⟦ Δ ⟧)
  → extc {A = A} (𝓢⟦ σ ⟧ δ) v ≡ 𝓢⟦ exts σ ⟧ (extc {A = A} δ v)
extc-exts {v = v} σ δ = ext λ B → ext λ{ Z → refl ; (S x) → sound-ren (σ x) (extc δ v) S_ }

sound-sub : (M : Γ ⊢ A) (σ : Sub Γ Δ) (δ : 𝓒⟦ Δ ⟧)
  → 𝓔⟦ M ⟧ (𝓢⟦ σ ⟧ δ) ≡ 𝓔⟦ subst σ M ⟧ δ

sound-sub (` x) σ δ = refl
sound-sub (ƛ M) σ δ = ext (λ v → trans (cong 𝓔⟦ M ⟧ (extc-exts σ δ))
                                       (sound-sub M (exts σ) (extc δ v)))
sound-sub (M · M₁) σ δ rewrite sound-sub M σ δ | sound-sub M₁ σ δ = refl
sound-sub `zero σ δ = refl
sound-sub (`suc M) σ δ = cong suc (sound-sub M σ δ)
sound-sub (recnat M M₁ M₂) σ δ rewrite sound-sub M σ δ | sound-sub M₁ σ δ | sound-sub M₂ σ δ = refl

extc-σ₀ : (γ  : 𝓒⟦ Γ ⟧) (W  : Γ ⊢ A) → extc γ (𝓔⟦ W ⟧ γ) ≡ 𝓢⟦ σ₀ W ⟧ γ
extc-σ₀ γ W = ext λ B → ext λ{ Z → refl ; (S x) → refl}

```








```
-- sound⟶ : ∀ {M N : Γ ⊢ A} → M ⟶ N → (γ : 𝓒⟦ Γ ⟧) → 𝓔⟦ M ⟧ γ ≡ 𝓔⟦ N ⟧ γ
sound⟶ (ξ-·₁ M⟶N) γ              rewrite sound⟶ M⟶N γ = refl
sound⟶ (ξ-·₂ x M⟶N) γ            rewrite sound⟶ M⟶N γ = refl
sound⟶ (β-ƛ {N = N}{W = W} v) γ  = trans (cong 𝓔⟦ N ⟧ (extc-σ₀ γ W)) (sound-sub N (σ₀ W) γ)
sound⟶ (ξ-suc M⟶N) γ             rewrite sound⟶ M⟶N γ = refl
sound⟶ (ξ-recnat M⟶N) γ          rewrite sound⟶ M⟶N γ = refl
sound⟶ β-zero γ = refl
sound⟶ (β-suc x) γ = refl
```



Soundness of the small-step semantics: making a reduction does not change the semantics


It is possible to show completeness, in the sense that
for all `M : ∅ ⊢ ℕ` it holds that `𝓔⟦ M ⟧ γ∅ ≡ n` implies that `M ⟹ V`, `Value V`, and `V ∼ n`.
But it requires a new technique:
Logical relations

(BTW, this result implies that all closed terms of type ℕ terminate!)

