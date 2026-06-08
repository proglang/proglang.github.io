	-*- mode: agda2;-*-

```
module lecture where
open import Relation.Binary.PropositionalEquality using (_≡_; refl; cong)
open import Data.Empty using (⊥)
open import Data.Nat using (ℕ; zero; suc; _<_; _≤_; s≤s; z≤n)
open import Data.Sum using (_⊎_; inj₁; inj₂)
open import Data.Product using (_×_; proj₁; proj₂; _,_)

-- from isomorphism
infix 0 _≃_
record _≃_ (A B : Set) : Set where
  field
    to   : A → B
    from : B → A
    from∘to : ∀ (x : A) → from (to x) ≡ x
    to∘from : ∀ (y : B) → to (from y) ≡ y
open _≃_

```

Let's assume that A and B are implicitly quantified as of type Set:

```
variable
  A B C : Set
  n : ℕ
```

# Negation

Constructive negation `¬ A` is modeled by *reductio ad absurdum*, i.e,
if we assume `A`, then we obtain a contradiction.


Negation can now be defined as a function that maps to the empty type.

```
infix 3 ¬_
¬_ : Set → Set
¬ A = A → ⊥

¬-elim : ¬ A → ¬ A
¬-elim ¬x = ¬x
```

For convenience, we define an eliminator for negation.

```
contradiction : ¬ A → A → B
contradiction ¬x x = ⊥-elim (¬x x)
```


In classical logic, double negation of some proposition is equivalent to the proposition.
In intuitionistic logic, only one direction holds.

```
¬¬-intro : A → ¬ (¬ A)
¬¬-intro a ¬a = ¬a a
```

The reverse direction does not hold, but ...


Contraposition holds

```
contraposition : (A → B) → (¬ B → ¬ A)
contraposition f ¬b a = ¬b (f a)
```

Inequality

```
_≢_ : A → A → Set
x ≢ y = ¬ (x ≡ y)

1≢2 : 1 ≢ 2
1≢2 ()

z≠suc : ∀ {n : ℕ} → zero ≢ suc n
z≠suc ()

```

Any two proofs of a negation are equal!

```
postulate
  fun-ext : {f g : A → B} → (∀ x → f x ≡ g x) → f ≡ g

assimilate : (p q : ¬ A) → p ≡ q
assimilate p q = fun-ext λ x → ⊥-elim (p x)
```

Ex: Show that `_<_` is irreflexive.

```
<-irrefl : ¬ (n < n)
<-irrefl (s≤s n<n) = <-irrefl n<n 
```

Ex: Show trichotomy
Trichotomy is a property of total orderings on A.
For m, n ∈ A either
* m < n ( and m ≢ n and ¬ (m > n))
* m ≡ n ...
* m > n ...

```
data Trichotomy (m n : ℕ) : Set where
  m<n : m < n → m ≢ n → ¬ (n < m) → Trichotomy m n
  m≡n : ¬ (m < n) → m ≡ n → ¬ (n < m) → Trichotomy m n
  m>n : ¬ (m < n) → m ≢ n → n < m → Trichotomy m n

trichotomy : (m n : ℕ) → Trichotomy m n
trichotomy zero zero = m≡n <-irrefl refl <-irrefl
trichotomy zero (suc n) = m<n (s≤s z≤n) z≠suc λ{ () }
trichotomy (suc m) zero = m>n (λ()) (λ{ ()}) (s≤s z≤n)
trichotomy (suc m) (suc n)
  with trichotomy m n
... | m<n x y z = m<n (s≤s x)               (λ {refl → y refl}) λ { (s≤s x₁) → z x₁}
... | m≡n x y z = m≡n (λ{ (s≤s x₁) → x x₁}) (cong suc y)        λ{ (s≤s x₁) → z x₁}
... | m>n x y z = m>n (λ{ (s≤s x₁) → x x₁}) (λ{ refl → y refl}) (s≤s z)
```

## Classical vs. intuitionistic logic

In classical logic, we can prove some additional theorems.
* double negation elimination:  `¬ ¬ A → A` 
* law of excluded middle: `A ⊎ ¬ A`
* Peirce's law: `((A → B) → A) → A`
* Implication as disjunction: `(A → B) → ¬ A ⊎ B`
* De Morgan's law: `¬ (¬ A × ¬ B) → A ⊎ B`

Neither of those hold in intuitionistic logic. But, **for example**, the law of excluded middle cannot be refuted, either.
Hence, its adoption as a postulate does not affect the consistency of the logic.

```
postulate
  em : ∀ {A : Set} → A ⊎ ¬ A
```

```
em-irrefutable : ∀ {A : Set} → ¬ ¬ (A ⊎ ¬ A)
em-irrefutable k = {!   !}
```