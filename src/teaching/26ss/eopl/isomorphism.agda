-- Context ---------------------------------------------------------------------

open import Relation.Binary.PropositionalEquality
open import Data.Nat using (ℕ; zero; suc; _+_; _*_)
open import Function using (_∘_)

-- Isomorphisms
infix 0 _≃_
record _≃_ (A B : Set) : Set where
  field
    to   : A → B
    from : B → A
    from∘to : ∀ (x : A) → from (to x) ≡ x
    to∘from : ∀ (y : B) → to (from y) ≡ y
open _≃_

-- Embeddings
infix 0 _≲_
record _≲_ (A B : Set) : Set where
  field
    to      : A → B
    from    : B → A
    from∘to : ∀ (x : A) → from (to x) ≡ x
open _≲_

-- Exercise ≃-implies-≲ (practice)----------------------------------------------

≃-implies-≲ : ∀ {A B : Set} → A ≃ B → A ≲ B
≃-implies-≲ A≃B =
  record
    { to      = to A≃B
    ; from    = from A≃B
    ; from∘to = from∘to A≃B
    }

-- Exercise _⇔_ (practice) -----------------------------------------------------

infix 0 _⇔_
record _⇔_ (A B : Set) : Set where
  field
    to   : A → B
    from : B → A

open _⇔_

⇔-refl : ∀ {A : Set} → A ⇔ A
⇔-refl = record
  { to   = λ x → x
  ; from = λ x → x
  }

⇔-sym : ∀ {A B : Set} → A ⇔ B → B ⇔ A
⇔-sym A⇔B =
  record
    { to   = from A⇔B
    ; from = to A⇔B
    }

⇔-trans : ∀ {A B C : Set} → A ⇔ B → B ⇔ C → A ⇔ C
⇔-trans A⇔B B⇔C =
  record
    { to   = to B⇔C   ∘ to A⇔B
    ; from = from A⇔B ∘ from B⇔C
    }

-- Exercise Bin-embedding (stretch) --------------------------------------------

-- Context

-- In `induction.agda` we defined and proved the following:
postulate
  Bin : Set
  toB : ℕ → Bin
  fromB : Bin → ℕ
  from-to-inverse : ∀ (n : ℕ) → fromB (toB n) ≡ n

-- Exercise

-- Using the above, establish that there is an embedding of ℕ into Bin.

ℕ≲Bin : ℕ ≲ Bin
ℕ≲Bin =
  record
    { to      = toB
    ; from    = fromB
    ; from∘to = from-to-inverse
    }

-- Why do `to` and `from` not form an isomorphism?

-- They do not form an isomorphism, because the other direction `to∘from` does
-- not hold, because there are multiple bistrings representing the same natural
-- number, e.g. both `from (⟨⟩ O)` and `from (⟨⟩ O O)` are equivalent to `0`.
