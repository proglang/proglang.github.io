open import Relation.Nullary using (¬_)
open import Relation.Binary.PropositionalEquality using (_≡_; refl; cong; sym; _≢_; cong₂)
open import Data.Nat using (ℕ; zero; suc; _+_; _*_; _∸_; _^_)
open import Data.Product using (_×_; _,_; proj₁; proj₂)
open import Data.Sum using (_⊎_; inj₁; inj₂)
open import Data.Empty using (⊥; ⊥-elim)

-- Context

infix 0 _≃_
record _≃_ (A B : Set) : Set where
  field
    to      : A → B
    from    : B → A
    from∘to : ∀ (x : A) → from (to x) ≡ x
    to∘from : ∀ (y : B) → to (from y) ≡ y
open _≃_

data _<_ : ℕ → ℕ → Set where
  z<s : ∀ {n : ℕ} → zero < suc n
  s<s : ∀ {m n : ℕ} → m < n → suc m < suc n

-- Exercise <-irreflexive (recommended) ----------------------------------------

-- Recall that `¬ (n < n)` is a function type `n < n → ⊥`

<-irreflexive : ∀ {n : ℕ} → ¬ (n < n)
<-irreflexive = λ { (s<s n<n) → <-irreflexive n<n }

-- Note that
--   <-irreflexive : ∀ {n : ℕ} → ¬ (n < n)
-- reduces to
--   <-irreflexive : ∀ {n : ℕ} → n < n → ⊥
-- so we can also write:

<-irreflexive' : ∀ {n : ℕ} → ¬ (n < n)
<-irreflexive' (s<s n<n) = <-irreflexive n<n

-- Exercise trichotomy (recommended) -------------------------------------------

-- Generalized Trichotomy for some arbitrary binary relation _<_.
data Trichotomy {A : Set} (_<_ : A → A → Set) : A → A → Set where
  tri-< : ∀ {x y : A} →   x < y → ¬ x ≡ y → ¬ y < x → Trichotomy _<_ x y
  tri-≡ : ∀ {x y : A} → ¬ x < y →   x ≡ y → ¬ y < x → Trichotomy _<_ x y
  tri-> : ∀ {x y : A} → ¬ x < y → ¬ x ≡ y →   y < x → Trichotomy _<_ x y

<-trichotomy : ∀ {m n : ℕ} → Trichotomy _<_ m n
<-trichotomy {zero}  {suc n} = tri-< z<s    (λ ()) (λ ())
<-trichotomy {zero}  {zero}  = tri-≡ (λ ()) refl   (λ ())
<-trichotomy {suc m} {zero}  = tri-> (λ ()) (λ ()) z<s
<-trichotomy {suc m} {suc n} with <-trichotomy {m} {n}
... | tri-<  m<n ¬m≡n ¬m>n = tri-< (s<s m<n)                   (λ { refl → ¬m≡n refl}) (λ { (s<s m>n) → ¬m>n m>n})
... | tri-≡ ¬m<n  m≡n ¬m>n = tri-≡ (λ { (s<s m<n) → ¬m<n m<n}) (cong suc m≡n)          (λ { (s<s m>n) → ¬m>n m>n})
... | tri-> ¬m<n ¬m≡n  m>n = tri-> (λ { (s<s m<n) → ¬m<n m<n}) (λ { refl → ¬m≡n refl}) (s<s m>n)

-- Alternative formalization using product (_×_) and sum (_×_) types:
Trichotomy' : ∀ {A : Set} → (A → A → Set) → (A → A → Set)
Trichotomy' _<_ x y = ((  x < y) × (¬ x ≡ y) × (¬ y < x))
                    ⊎ ((¬ x < y) × (  x ≡ y) × (¬ y < x))
                    ⊎ ((¬ x < y) × (¬ x ≡ y) × (  y < x)) -- all parentheses can be ommited here

-- Proof is identical, but less readable, since the tri constructors are now written as:
--   tri-< p q r    <=>    inj₁ (p , q , r)
--   tri-≡ p q r    <=>    inj₂ (inj₁ (p , q , r))
--   tri-> p q r    <=>    inj₂ (inj₂ (p , q , r))
<-trichotomy' : ∀ {m n : ℕ} → Trichotomy' (_<_) m n
<-trichotomy' {zero}  {suc n} = inj₁       (z<s    , (λ ()) , (λ ()))
<-trichotomy' {zero}  {zero}  = inj₂ (inj₁ ((λ ()) , refl   , (λ ())))
<-trichotomy' {suc m} {zero}  = inj₂ (inj₂ ((λ ()) , (λ ()) , z<s))
<-trichotomy' {suc m} {suc n} with <-trichotomy' {m} {n}
... | inj₁       ( m<n , ¬m≡n , ¬m>n)  = inj₁       (s<s m<n                     , (λ { refl → ¬m≡n refl}) , (λ { (s<s m>n) → ¬m>n m>n}))
... | inj₂ (inj₁ (¬m<n ,  m≡n , ¬m>n)) = inj₂ (inj₁ ((λ { (s<s m<n) → ¬m<n m<n}) , cong suc m≡n            , (λ { (s<s m>n) → ¬m>n m>n})))
... | inj₂ (inj₂ (¬m<n , ¬m≡n ,  m>n)) = inj₂ (inj₂ ((λ { (s<s m<n) → ¬m<n m<n}) , (λ { refl → ¬m≡n refl}) , s<s m>n))

-- Exercise ⊎-dual-× (recommended) ---------------------------------------------

postulate
  fun-ext :
    ∀ {A B : Set} {f g : A → B} →
    (∀ (a : A) → f a ≡ g a) →
    f ≡ g

⊎-dual-× : {A B : Set} → ¬ (A ⊎ B) ≃ (¬ A) × (¬ B)
⊎-dual-× = record
  { to      = λ ¬A⊎B → (λ a → ¬A⊎B (inj₁ a)) , λ b → ¬A⊎B (inj₂ b)
  ; from    = λ { (¬A , ¬B) (inj₁ a) → ¬A a
                ; (¬A , ¬B) (inj₂ b) → ¬B b
                }
  ; from∘to = λ ¬A⊎B → fun-ext (λ { (inj₁ a) → refl ; (inj₂ b) → refl})
  ; to∘from = λ { (¬A , ¬B) → refl }
  }

-- Exercise Classical (stretch) ------------------------------------------------

-- Consider the following principles:

Excluded-Middle             = ∀ (A : Set) → A ⊎ ¬ A
Double-Negation-Elimination = ∀ (A : Set) → ¬ ¬ A → A
Peirce’s-Law                = ∀ (A B : Set) → ((A → B) → A) → A
Implication-as-disjunction  = ∀ (A B : Set) → (A → B) → ¬ A ⊎ B
De-Morgan                   = ∀ (A B : Set) → ¬ (¬ A × ¬ B) → A ⊎ B

-- Show that each of these implies all the others.

-- Excluded-Middle             = ∀ (A : Set) → A ⊎ ¬ A
-- De-Morgan                   = ∀ (A B : Set) → ¬ (¬ A × ¬ B) → A ⊎ B
em→dm : Excluded-Middle → De-Morgan
em→dm em A B ¬[¬a×¬b] with em A | em B
... | inj₁  a | _       = inj₁ a
... | _       | inj₁  b = inj₂ b
... | inj₂ ¬a | inj₂ ¬b = ⊥-elim (¬[¬a×¬b] (¬a , ¬b))

-- De-Morgan                   = ∀ (A B : Set) → ¬ (¬ A × ¬ B) → A ⊎ B
-- Double-Negation-Elimination = ∀ (A : Set) → ¬ ¬ A → A
dm→dne : De-Morgan → Double-Negation-Elimination
dm→dne dm A ¬¬a with dm A A (λ { (¬a , ¬a') → ¬¬a ¬a })
... | inj₁ a = a
... | inj₂ a = a

-- Double-Negation-Elimination = ∀ (A : Set) → ¬ ¬ A → A
-- Peirce’s-Law                = ∀ (A B : Set) → ((A → B) → A) → A
dne→pl : Double-Negation-Elimination → Peirce’s-Law
dne→pl dne A B [a→b]→a = dne A (λ ¬a → ¬a ([a→b]→a (λ a → ⊥-elim (¬a a))))

-- Peirce’s-Law                = ∀ (A B : Set) → ((A → B) → A) → A
-- Implication-as-disjunction  = ∀ (A B : Set) → (A → B) → ¬ A ⊎ B
pl→iad : Peirce’s-Law → Implication-as-disjunction
pl→iad pl A B a→b = pl (¬ A ⊎ B) ⊥ (λ ¬[¬a⊎b] → inj₁ (λ a → ¬[¬a⊎b] (inj₂ (a→b a))))

-- Implication-as-disjunction  = ∀ (A B : Set) → (A → B) → ¬ A ⊎ B
-- Excluded-Middle             = ∀ (A : Set) → A ⊎ ¬ A
iad→em : Implication-as-disjunction → Excluded-Middle
iad→em iad A with iad A A (λ a → a)
... | inj₁ b = inj₂ b
... | inj₂ a = inj₁ a

-- Note that we now have a cycle of implications, so everything implies everything:
--
--   em → dm → dne → pl → iad
--   ↑                      |
--   ⌊______________________⌋

-- Exercise Stable (stretch) ---------------------------------------------------

-- Say that a formula is stable if double negation elimination holds for it:

Stable : Set → Set
Stable A = ¬ ¬ A → A

-- Show that any negated formula is stable, and that the conjunction of two stable formulas is stable.

¬-Stable : ∀ (A : Set) → Stable (¬ A)
¬-Stable A = λ ¬¬¬a a → ¬¬¬a (λ ¬a → ¬a a)

×-preserves-Stable : ∀ {A B : Set} →
  Stable A →
  Stable B →
  Stable (A × B)
×-preserves-Stable sa sb =
  λ ¬¬[a×b] →
    sa (λ ¬a → ¬¬[a×b] (λ { (a , _) → ¬a a })) ,
    sb (λ ¬b → ¬¬[a×b] (λ { (_ , b) → ¬b b }))
