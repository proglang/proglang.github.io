-- Context ---------------------------------------------------------------------

open import Relation.Binary.PropositionalEquality using (_≡_; refl; cong; sym; _≢_)
open import Data.Nat using (ℕ; zero; suc; _+_; _*_; _∸_; _^_; _>_)
open import Data.Product using (_×_; _,_; proj₁; proj₂)
open import Data.Sum using (_⊎_; inj₁; inj₂)
open import Data.Empty using (⊥)

-- THE PLAN 
-- 0) [[accumulate exercises you want to discuss]]
-- 1) exercise part:  quickly discuss some connectives exercises
-- 2) lecture part 1: continue with last connective (implication)
-- 3) lecture part 2: discuss negation.

-- Isomorphisms
infix 0 _≃_
record _≃_ (A B : Set) : Set where
  field
    to   : A → B
    from : B → A
    from∘to : ∀ (x : A) → from (to x) ≡ x
    to∘from : ∀ (y : B) → to (from y) ≡ y
open _≃_

-- Equivalences
infix 1 _⇔_
record _⇔_ (A B : Set) : Set where
  field
    to   : A → B
    from : B → A
open _⇔_

-- Exercise ⇔≃× (recommended) --------------------------------------------------

⇔≃× : ∀ {A B : Set} → (A ⇔ B) ≃ (A → B) × (B → A)
⇔≃× = record
  { to      = λ A≃B → to A≃B , from A≃B
  ; from    = λ { (to , from) → record { to = to ; from = from } }
  ; from∘to = λ _ → refl
  ; to∘from = λ _ → refl
  }

-- Exercise ⊎-comm (recommended) -----------------------------------------------

⊎-swap : ∀ {A B : Set} → A ⊎ B → B ⊎ A
⊎-swap (inj₁ a) = inj₂ a
⊎-swap (inj₂ b) = inj₁ b

⊎-swap-involutive : ∀ {A B : Set} (A⊎B : A ⊎ B) → ⊎-swap (⊎-swap A⊎B) ≡ A⊎B
⊎-swap-involutive (inj₁ a) = refl
⊎-swap-involutive (inj₂ b) = refl

⊎-comm : ∀ {A B : Set} → A ⊎ B ≃ B ⊎ A
⊎-comm = record 
  { to = λ { (inj₁ x) → inj₂ x
           ; (inj₂ y) → inj₁ y }
  ; from = λ { (inj₁ x) → inj₂ x
           ; (inj₂ y) → inj₁ y }
  ; from∘to = λ { (inj₁ x) → refl
                ; (inj₂ y) → refl }
  ; to∘from = λ { (inj₁ x) → refl
                ; (inj₂ y) → refl }
  }

-- Exercise ⊎-assoc (practice) -------------------------------------------------
-- uses lambda where syntax: https://agda.readthedocs.io/en/latest/language/lambda-abstraction.html#pattern-lambda
⊎-assoc : ∀ {A B C : Set} → (A ⊎ B) ⊎ C ≃ A ⊎ (B ⊎ C)
⊎-assoc = record
  { to      = λ where
                  (inj₁ (inj₁ a)) → inj₁ a
                  (inj₁ (inj₂ b)) → inj₂ (inj₁ b)
                  (inj₂ c)        → inj₂ (inj₂ c)
  ; from    = λ where
                  (inj₁ a)        → inj₁ (inj₁ a)
                  (inj₂ (inj₁ b)) → inj₁ (inj₂ b)
                  (inj₂ (inj₂ c)) → inj₂ c
  ; from∘to = λ where
                  (inj₁ (inj₁ a)) → refl
                  (inj₁ (inj₂ b)) → refl
                  (inj₂ c)        → refl
  ; to∘from = λ where
                  (inj₁ a)        → refl
                  (inj₂ (inj₁ b)) → refl
                  (inj₂ (inj₂ c)) → refl
  }

-- Exercise ⊥-identityˡ (recommended) ------------------------------------------

⊥-identityˡ : ∀ {A : Set} → ⊥ ⊎ A ≃ A
⊥-identityˡ = record 
  { to = λ { (inj₂ y) → y }
  ; from = λ x → inj₂ x 
  ; from∘to = λ { (inj₂ y) → refl }
  ; to∘from = λ y → refl 
  }

-- (*): Note that in this example, Agda is smart enough to figure out that we
-- don't need to cover the inj₁ constructor. Two more explicit ways to write
-- this down is

⊥-identityˡ' : ∀ {A : Set} → ⊥ ⊎ A ≃ A
⊥-identityˡ' = record
  { to      = λ where
                  (inj₁ ())
                  (inj₂ a) → a
  ; from    = inj₂
  ; from∘to = λ where
                  (inj₁ ())
                  (inj₂ a) → refl
  ; to∘from = λ _ → refl
  }

-- Exercise ⊥-identityʳ (practice) ---------------------------------------------

⊥-identityʳ : ∀ {A : Set} → A ⊎ ⊥ ≃ A
⊥-identityʳ = record
  { to      = λ { (inj₁ a) → a }
  ; from    = inj₁
  ; from∘to = λ { (inj₁ a) → refl }
  ; to∘from = λ _ → refl
  }

-- Exercise ⊎-weak-× (recommended) ---------------------------------------------

⊎-weak-× : ∀ {A B C : Set} → (A ⊎ B) × C → A ⊎ (B × C)
⊎-weak-× (inj₁ x , z) = inj₁ x
⊎-weak-× (inj₂ y , z) = inj₂ (y , z)

⊎-strong-× : ∀ {A B C : Set} → (A ⊎ B) × C ≃ A × C ⊎ B × C
⊎-strong-× = record
  { to      = λ where
                  (inj₁ a , c) → inj₁ (a , c)
                  (inj₂ b , c) → inj₂ (b , c)
  ; from    = λ where
                  (inj₁ (a , c)) → inj₁ a , c
                  (inj₂ (a , c)) → inj₂ a , c
  ; from∘to = λ where
                  (inj₁ a , c) → refl
                  (inj₂ b , c) → refl
  ; to∘from = λ where
                  (inj₁ (a , c)) → refl
                  (inj₂ (a , c)) → refl
  }

-- Exercise ⊎×-implies-×⊎ (practice) -------------------------------------------

⊎×-implies-×⊎ : ∀ {A B C D : Set} → (A × B) ⊎ (C × D) → (A ⊎ C) × (B ⊎ D)
⊎×-implies-×⊎ (inj₁ (a , b)) = inj₁ a , inj₁ b
⊎×-implies-×⊎ (inj₂ (c , d)) = inj₂ c , inj₂ d

-- The other direction
--
--   (A ⊎ C) × (B ⊎ D) → (A × B) ⊎ (C × D)
--
-- is not true, as the following counterexample shows:
-- if we have an `A` and a `D`, then we are missing
-- either a `B` to construct `A × B` or a `C` to construct `C × D`.

--------------------------------------------------------------------------------
-- LECTURE PART ON IMPLICATION -------------------------------------------------
-------------------------------------------------------------------------------- 

variable 
  A B C : Set 
  n : ℕ 

-- Implication `A → B` *is* the function type: evidence for `A → B` is a
-- function that turns evidence for `A` into evidence for `B`.
-- 
-- Introduction is defining a function (`λ (x : A) → N`), elimination is
-- applying one. The elimination rule is *modus ponens*:

→-elim : (A → B) → A → B
→-elim f a = f a

-- Elimination after introduction is the identity (`η`):

η-→ : ∀ (f : A → B) → (λ x → →-elim f x) ≡ f
η-→ f = refl

-- Implication binds less tightly than any other operator, so `A ⊎ B → B ⊎ A`
-- parses as `(A ⊎ B) → (B ⊎ A)`.
-- 
-- `A → B` is also called the *function space* or *exponential* `Bᴬ`: if `A`
-- has `m` and `B` has `n` members, then `A → B` has `nᵐ` members. Many laws
-- for numeric exponentials carry over to types as isomorphisms.
-- 
-- Currying — corresponds to `(pⁿ)ᵐ ≡ pⁿ*ᵐ`:

currying : (A → B → C) ≃ (A × B → C)
currying = record 
  { to      = λ where 
                f (fst , snd) → f fst snd 
  ; from    = λ g a b → g (a , b) 
  ; from∘to = λ _ → refl 
  ; to∘from = λ _ → refl 
  }

-- Instead of a function taking a pair, we take the first argument and return a
-- function expecting the second. Agda is optimised for currying, so `2 + 3`
-- abbreviates `_+_ 2 3`.

⊎-elim : A ⊎ B → (A → C) → (B → C) → C
⊎-elim (inj₁ x) ac bc = ac x
⊎-elim (inj₂ y) ac bc = bc y

×-elim : A × B → (A → B → C) → C
×-elim (a , b) abc = abc a b

⊥-elim : ⊥ → C
⊥-elim ()
