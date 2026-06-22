open import Data.Nat using (ℕ; suc; zero; _+_; _≤?_; _≤_; z≤n; s≤s)
open import Data.Bool using (Bool; true; false)
open import Relation.Nullary using (¬_; Dec; _because_; does; proof; yes; no)
open import Relation.Binary.PropositionalEquality using (_≡_; refl; sym; trans; cong; subst; module ≡-Reasoning)
open ≡-Reasoning
open import Data.Product
open import Data.Sum
open import Data.Empty
open import Data.Unit using (⊤; tt)
open import Relation.Nullary.Negation using () renaming (contradiction to ¬¬-intro)

-- Context ---------------------------------------------------------------------

infix 0 _⇔_
record _⇔_ (A B : Set) : Set where
  field
    to   : A → B
    from : B → A

open _⇔_

infix 4 _≤ᵇ_

_≤ᵇ_ : ℕ → ℕ → Bool
zero ≤ᵇ n       =  true
suc m ≤ᵇ zero   =  false
suc m ≤ᵇ suc n  =  m ≤ᵇ n

T : Bool → Set
T true   =  ⊤
T false  =  ⊥

T→≡ : ∀ (b : Bool) → T b → b ≡ true
T→≡ true tt   =  refl
T→≡ false ()

≡→T : ∀ {b : Bool} → b ≡ true → T b
≡→T refl  =  tt

≤ᵇ→≤ : ∀ (m n : ℕ) → T (m ≤ᵇ n) → m ≤ n
≤ᵇ→≤ zero    n       tt  =  z≤n
≤ᵇ→≤ (suc m) zero    ()
≤ᵇ→≤ (suc m) (suc n) t   =  s≤s (≤ᵇ→≤ m n t)

≤→≤ᵇ : ∀ {m n : ℕ} → m ≤ n → T (m ≤ᵇ n)
≤→≤ᵇ z≤n        =  tt
≤→≤ᵇ (s≤s m≤n)  =  ≤→≤ᵇ m≤n

⌊_⌋ : ∀ {A : Set} → Dec A → Bool
⌊ yes x ⌋  =  true
⌊ no ¬x ⌋  =  false

_≤ᵇ′_ : ℕ → ℕ → Bool
m ≤ᵇ′ n  =  ⌊ m ≤? n ⌋

toWitness : ∀ {A : Set} {D : Dec A} → T ⌊ D ⌋ → A
toWitness {A} {yes x} tt  =  x
toWitness {A} {no ¬x} ()

fromWitness : ∀ {A : Set} {D : Dec A} → A → T ⌊ D ⌋
fromWitness {A} {yes x} _  =  tt
fromWitness {A} {no ¬x} x  =  ¬x x

≤ᵇ′→≤ : ∀ {m n : ℕ} → T (m ≤ᵇ′ n) → m ≤ n
≤ᵇ′→≤  =  toWitness

≤→≤ᵇ′ : ∀ {m n : ℕ} → m ≤ n → T (m ≤ᵇ′ n)
≤→≤ᵇ′  =  fromWitness

infixr 6 _∧_

_∧_ : Bool → Bool → Bool
true  ∧ true  = true
false ∧ _     = false
_     ∧ false = false

infixr 6 _×-dec_

_×-dec_ : ∀ {A B : Set} → Dec A → Dec B → Dec (A × B)
yes x ×-dec yes y = yes (x , y)
no ¬x ×-dec _     = no λ{ (x , y) → ¬x x }
_     ×-dec no ¬y = no λ{ (x , y) → ¬y y }

infixr 5 _∨_

_∨_ : Bool → Bool → Bool
true  ∨ _      = true
_     ∨ true   = true
false ∨ false  = false

infixr 5 _⊎-dec_

_⊎-dec_ : ∀ {A B : Set} → Dec A → Dec B → Dec (A ⊎ B)
yes x ⊎-dec _     = yes (inj₁ x)
_     ⊎-dec yes y = yes (inj₂ y)
no ¬x ⊎-dec no ¬y = no λ{ (inj₁ x) → ¬x x ; (inj₂ y) → ¬y y }

not : Bool → Bool
not true  = false
not false = true

¬? : ∀ {A : Set} → Dec A → Dec (¬ A)
¬? (yes x)  =  no (¬¬-intro x)
¬? (no ¬x)  =  yes ¬x

_⊃_ : Bool → Bool → Bool
_     ⊃ true   =  true
false ⊃ _      =  true
true  ⊃ false  =  false

_→-dec_ : ∀ {A B : Set} → Dec A → Dec B → Dec (A → B)
_     →-dec yes y  =  yes (λ _ → y)
no ¬x →-dec _      =  yes (λ x → ⊥-elim (¬x x))
yes x →-dec no ¬y  =  no (λ f → ¬y (f x))

infix 4 _<_

data _<_ : ℕ → ℕ → Set where
  z<s : ∀ {n : ℕ} → zero < suc n
  s<s : ∀ {m n : ℕ} → m < n → suc m < suc n

-- Exercise _<?_ (recommended) -------------------------------------------------

_<?_ : ∀ (m n : ℕ) → Dec (m < n)
zero  <? zero  = no (λ ())
zero  <? suc n = yes z<s
suc m <? zero  = no (λ ())
suc m <? suc n with m <? n
… | yes m<n = yes (s<s m<n)
… | no ¬m<n = no (λ { (s<s m<n) → ¬m<n m<n })

-- Exercise _≡ℕ?_ (practice) ---------------------------------------------------

_≡ℕ?_ : ∀ (m n : ℕ) → Dec (m ≡ n)
zero  ≡ℕ? zero  = yes refl
zero  ≡ℕ? suc n = no (λ ())
suc m ≡ℕ? zero  = no (λ ())
suc m ≡ℕ? suc n with m ≡ℕ? n
... | yes refl = yes refl
... | no  m≢n  = no λ { refl → m≢n refl }

-- Exercise erasure (practice) -------------------------------------------------

-- Show that erasure relates corresponding boolean and decidable operations:

∧-× : ∀ {A B : Set} (x : Dec A) (y : Dec B) → ⌊ x ⌋ ∧ ⌊ y ⌋ ≡ ⌊ x ×-dec y ⌋
∧-× (no ¬A) (no ¬B) = refl
∧-× (no ¬A) (yes B) = refl
∧-× (yes A) (no ¬B) = refl
∧-× (yes A) (yes B) = refl

∨-⊎ : ∀ {A B : Set} (x : Dec A) (y : Dec B) → ⌊ x ⌋ ∨ ⌊ y ⌋ ≡ ⌊ x ⊎-dec y ⌋
∨-⊎ (no ¬A) (no ¬B) = refl
∨-⊎ (no ¬A) (yes B) = refl
∨-⊎ (yes A) (no ¬B) = refl
∨-⊎ (yes A) (yes B) = refl

not-¬ : ∀ {A : Set} (x : Dec A) → not ⌊ x ⌋ ≡ ⌊ ¬? x ⌋
not-¬ (no ¬A) = refl
not-¬ (yes A) = refl

-- Exercise iff-erasure (recommended) ------------------------------------------

-- Give analogues of the _⇔_ operation from Chapter Isomorphism, operation on
-- booleans and decidables, and also show the corresponding erasure:

_iff_ : Bool → Bool → Bool
true  iff true  = true
false iff false = true
_     iff _     = false

_⇔-dec_ : ∀ {A B : Set} → Dec A → Dec B → Dec (A ⇔ B)
yes A ⇔-dec yes B = yes (record { to   = λ _ → B
                                ; from = λ _ → A })
no ¬A ⇔-dec no ¬B = yes (record { to   = λ A → ⊥-elim (¬A A)
                                ; from = λ B → ⊥-elim (¬B B) })
no ¬A ⇔-dec yes B = no λ A⇔B → ¬A (from A⇔B B)
yes A ⇔-dec no ¬B = no λ A⇔B → ¬B (to   A⇔B A)

iff-⇔ : ∀ {A B : Set} (x : Dec A) (y : Dec B) → ⌊ x ⌋ iff ⌊ y ⌋ ≡ ⌊ x ⇔-dec y ⌋
iff-⇔ (no ¬A) (no ¬B) = refl
iff-⇔ (no ¬A) (yes B) = refl
iff-⇔ (yes A) (no ¬B) = refl
iff-⇔ (yes A) (yes B) = refl

-- Exercise False --------------------------------------------------------------

-- "Give analogues of True, toWitness, and fromWitness which work with
-- negated properties. Call these False, toWitnessFalse, and
-- fromWitnessFalse."

False : Bool → Set
False true   =  ⊥
False false  =  ⊤

toWitness' : ∀ {A : Set} {D : Dec A} → False ⌊ D ⌋ → ¬ A
toWitness' {A} {yes x} ()
toWitness' {A} {no ¬x} tt = ¬x

fromWitness' : ∀ {A : Set} {D : Dec A} → ¬ A → False ⌊ D ⌋
fromWitness' {A} {yes x} ¬x = ¬x x
fromWitness' {A} {no ¬x} _  = tt

-- Original definitions for comparison:

-- T : Bool → Set
-- T true   =  ⊤
-- T false  =  ⊥

-- toWitness : ∀ {A : Set} {D : Dec A} → T ⌊ D ⌋ → A
-- toWitness {A} {yes x} tt  =  x
-- toWitness {A} {no ¬x} ()

-- fromWitness : ∀ {A : Set} {D : Dec A} → A → T ⌊ D ⌋
-- fromWitness {A} {yes x} _  =  tt
-- fromWitness {A} {no ¬x} x  =  ¬x x

-- Exercise Bin ----------------------------------------------------------------

-- Context

data Bin : Set where
  ⟨⟩ : Bin
  _O : Bin → Bin
  _I : Bin → Bin

data One : Bin → Set where
  one-I         : One (⟨⟩ I)
  one-left-of-O : ∀ {b : Bin} → One b → One (b O)
  one-left-of-I : ∀ {b : Bin} → One b → One (b I)

data Can : Bin → Set where
  can-zero : Can (⟨⟩ O)
  can-one  : ∀ {b : Bin} → One b → Can b

-- Exercise

-- Approach A, use decidable equality on bitstrings:

_≟_ : ∀ (x y : Bin) → Dec (x ≡ y)
⟨⟩ ≟ ⟨⟩       = yes refl
⟨⟩ ≟ (y O)    = no λ()
⟨⟩ ≟ (y I)    = no λ()
(x O) ≟ ⟨⟩    = no λ()
(x O) ≟ (y I) = no λ()
(x I) ≟ ⟨⟩    = no λ()
(x I) ≟ (y O) = no λ()
(x O) ≟ (y O) with x ≟ y
… | yes refl = yes refl
… | no ¬x≡y  = no λ { refl → ¬x≡y refl }
(x I) ≟ (y I) with x ≟ y
… | yes refl = yes refl
… | no ¬x≡y  = no λ { refl → ¬x≡y refl }

One? : ∀ b → Dec (One b)
One? ⟨⟩ = no λ { ()}
One? (b O) with One? b
... | yes x = yes (one-left-of-O x)
... | no x = no λ { (one-left-of-O a) → x a}
One? (⟨⟩ I) = yes one-I
One? ((b O) I) with One? (b O)
... | yes x = yes (one-left-of-I x)
... | no x = no λ { (one-left-of-I a) → x a}
One? ((b I) I) with One? (b I)
... | yes x = yes (one-left-of-I x)
... | no x = no λ { (one-left-of-I a) → x a}

Can? : ∀ b → Dec (Can b)
Can? b
  with One? b
… | yes one-b = yes (can-one one-b)
… | no ¬one-b
  with b ≟ (⟨⟩ O)
… | yes refl = yes can-zero
… | no ¬b≡⟨⟩O = no λ where
  can-zero        → ¬b≡⟨⟩O refl
  (can-one one-b) → ¬one-b one-b

-- Approach B, use deeper pattern matching:

One?' : ∀ b → Dec (One b)
One?' ⟨⟩ = no (λ ())
One?' (b O) with One?' b
… | yes one-b = yes (one-left-of-O one-b)
… | no ¬one-b = no (λ { (one-left-of-O one-b) → ¬one-b one-b })
One?' (b I)
  with One?' b
… | yes one-b = yes (one-left-of-I one-b)
… | no ¬one-b
  with b ≟ ⟨⟩
… | yes refl = yes one-I
… | no  b≢⟨⟩ = no λ where
    one-I                 → ⊥-elim (b≢⟨⟩ refl)
    (one-left-of-I one-b) → ¬one-b one-b

Can?' : ∀ b → Dec (Can b)
Can?' ⟨⟩ = no λ { (can-one ()) }
Can?' (⟨⟩ O) = yes can-zero
Can?' ((b O) O) with One?' ((b O) O)
… | yes one-bI = yes (can-one one-bI)
… | no ¬one-bI = no (λ { (can-one one-bI) → ¬one-bI one-bI })
Can?' ((b I) O) with One?' ((b I) O)
… | yes one-bI = yes (can-one one-bI)
… | no ¬one-bI = no (λ { (can-one one-bI) → ¬one-bI one-bI })
Can?' (b I) with One?' (b I)
… | yes one-bI = yes (can-one one-bI)
… | no ¬one-bI = no (λ { (can-one one-bI) → ¬one-bI one-bI })
