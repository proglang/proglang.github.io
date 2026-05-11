open import Relation.Binary.PropositionalEquality using (_≡_; _≢_; refl; cong; sym; module ≡-Reasoning)
open import Data.Nat using (ℕ; zero; suc; _+_; _*_; _∸_; _^_)

open ≡-Reasoning

-- Context

+-assoc : ∀ (m n p : ℕ) → (m + n) + p ≡ m + (n + p)
+-assoc zero    n p = refl
+-assoc (suc m) n p = cong suc (+-assoc m n p)

+-identity : ∀ (n : ℕ) → n + zero ≡ n
+-identity zero    = refl
+-identity (suc n) = cong suc (+-identity n)

+-suc : ∀ (m n : ℕ) → m + suc n ≡ suc (m + n)
+-suc zero    n = refl
+-suc (suc m) n = cong suc (+-suc m n)

+-comm : ∀ (m n : ℕ) → m + n ≡ n + m
+-comm m zero    = +-identity m
+-comm m (suc n) = 
  m + (suc n) ≡⟨ +-suc m n ⟩ 
  suc (m + n) ≡⟨ cong suc (+-comm m n) ⟩
  suc (n + m) ∎
  
-- Exercise operators (practice) -----------------------------------------------

-- Part 1: Give another example of a pair of operators that have an identity and
-- are associative, commutative, and distribute over one another. (You do not
-- have to prove these properties.)

-- Solution: For example, booleans with operators ∧ and ∨.

-- Part 2: Give an example of an operator that has an identity and is
-- associative but is not commutative. (You do not have to prove these
-- properties.)

-- Solutions:
-- - Lists with list concatenation _++_, e.g. [1, 2] ++ [3, 4, 5] ≡ [1, 2, 3, 4, 5]
-- - Matrices with matrix multiplication.

-- Part 1 is written out below, but not proven. Feel free to use it as further
-- exercise! Since we're talking about booleans, which are finite, the proofs
-- are comparatively simple and require no induction.

-- Part 2 is also written out below, and requires induction for the proofs.


data 𝔹 : Set where
  true : 𝔹
  false : 𝔹

_∧_ : 𝔹 → 𝔹 → 𝔹
true  ∧ y = y
false ∧ y = false

_∨_ : 𝔹 → 𝔹 → 𝔹
true  ∨ y = true
false ∨ y = y

-- Left and right identity of ∧ and ∨

∧-identityₗ : ∀ (x : 𝔹) → true ∧ x ≡ x
∧-identityₗ = {!!}

∧-identityᵣ : ∀ (x : 𝔹) → x ∧ true ≡ x
∧-identityᵣ = {!!}

∨-identityₗ : ∀ (x : 𝔹) → false ∧ x ≡ x
∨-identityₗ = {!!}

∨-identityᵣ : ∀ (x : 𝔹) → x ∧ false ≡ x
∨-identityᵣ = {!!}

-- Associativity of ∧ and ∨

∧-assoc : ∀ (x y z : 𝔹) → (x ∧ y) ∧ z ≡ x ∧ (y ∧ z)
∧-assoc = {!!}

∨-assoc : ∀ (x y z : 𝔹) → (x ∨ y) ∨ z ≡ x ∨ (y ∨ z)
∨-assoc = {!!}

-- Commutativity of ∧ and ∨

∧-comm : ∀ (x y : 𝔹) → x ∧ y ≡ y ∧ x
∧-comm = {!!}

∨-comm : ∀ (x y : 𝔹) → x ∨ y ≡ y ∨ x
∨-comm = {!!}

-- Distributivity of ∧ over ∨, and ∨ over ∧ - from both sides.

∧-distₗ-over-∨ : ∀ (x y z : 𝔹) → x ∨ (y ∧ z) ≡ (x ∨ y) ∧ (x ∨ z)
∧-distₗ-over-∨ = {!!}

∧-distᵣ-over-∨ : ∀ (x y z : 𝔹) → (x ∧ y) ∨ z ≡ (x ∨ z) ∧ (y ∨ z)
∧-distᵣ-over-∨ = {!!}

∨-distₗ-over-∧ : ∀ (x y z : 𝔹) → x ∧ (y ∨ z) ≡ (x ∧ y) ∨ (x ∧ z)
∨-distₗ-over-∧ = {!!}

∨-distᵣ-over-∧ : ∀ (x y z : 𝔹) → (x ∨ y) ∧ z ≡ (x ∧ z) ∨ (y ∧ z)
∨-distᵣ-over-∧ = {!!}

data List (A : Set) : Set where
  []  : List A
  _∷_ : A → List A → List A

infixr 5 _++_
_++_ : ∀ {A : Set} → List A → List A → List A
[]       ++ ys = ys
(x ∷ xs) ++ ys = x ∷ (xs ++ ys)

-- Left and right identity of _++_

++-identityₗ : ∀ {A : Set} (xs : List A) → [] ++ xs ≡ xs
++-identityₗ = {!!}

++-identityᵣ : ∀ {A : Set} (xs : List A) → xs ++ [] ≡ xs
++-identityᵣ = {!!}

-- Associativity of _++_

++-assoc : ∀ {A : Set} (xs ys zs : List A) → (xs ++ ys) ++ zs ≡ xs ++ (ys ++ zs)
++-assoc = {!!}

-- Exercise finite-+-assoc (stretch) -------------------------------------------

-- [ommited]

-- Exercise +-swap (recommended) -----------------------------------------------

-- Variant 1: using equational reasoning and `cong`.
-- Note, that the `begin` in equational reasoning is optional.
+-swap : ∀ (m n p : ℕ) → m + (n + p) ≡ n + (m + p)
+-swap m n p =
  m + (n + p) ≡⟨ sym (+-assoc m n p) ⟩
  (m + n) + p ≡⟨ cong (_+ p) (+-comm m n) ⟩ -- (*)
  (n + m) + p ≡⟨ +-assoc n m p ⟩
  n + (m + p) ∎

-- (*) The expression `_+ p` is syntactic sugar for `λ x → x + p`, i.e.
-- an anonymous function, which takes a single argument `x` and
-- returns `x + p`.

-- Variant 2: using `rewrite`.
-- Note the use of `sym` since we need to replace the right side of +-assoc with
-- its left side.
+-swap' : ∀ (m n p : ℕ) → m + (n + p) ≡ n + (m + p)
+-swap' m n p rewrite sym (+-assoc m n p) | sym (+-assoc n m p) | +-comm m n = refl

-- Exercise *-distrib-+ (recommended) ------------------------------------------

-- Variant 1: using equational reasoning and `cong`.
*-distᵣ-over-+ : ∀ (m n p : ℕ) → (m + n) * p ≡ m * p + n * p
*-distᵣ-over-+ zero n p =
  (0 + n) * p   ≡⟨⟩
  n * p         ≡⟨⟩
  0 * p + n * p ∎
*-distᵣ-over-+ (suc m) n p =
  (suc m + n) * p     ≡⟨⟩
  suc (m + n) * p     ≡⟨⟩
  p + (m + n) * p     ≡⟨ cong (p +_) (*-distᵣ-over-+ m n p) ⟩
  p + (m * p + n * p) ≡⟨ sym (+-assoc p (m * p) (n * p)) ⟩
  p + m * p + n * p   ≡⟨⟩
  suc m * p + n * p   ∎

-- Variant 2: using `rewrite`.
*-distᵣ-over-+' : ∀ (m n p : ℕ) → (m + n) * p ≡ m * p + n * p
*-distᵣ-over-+' zero n p = refl
*-distᵣ-over-+' (suc m) n p rewrite *-distᵣ-over-+' m n p | +-assoc p (m * p) (n * p) = refl

-- Exercise *-assoc (recommended) ----------------------------------------------

-- Variant 2: using equational reasoning and `cong`.
*-assoc : ∀ (m n p : ℕ) → (m * n) * p ≡ m * (n * p)
*-assoc zero n p =
  (0 * n) * p ≡⟨⟩
  0 * p       ≡⟨⟩
  0           ≡⟨⟩
  0 * (n * p) ∎
*-assoc (suc m) n p =
  (suc m * n) * p      ≡⟨⟩
  (n + m * n) * p      ≡⟨ *-distᵣ-over-+ n (m * n) p ⟩
  n * p + m * n * p    ≡⟨ cong (n * p +_) (*-assoc m n p) ⟩
  n * p +  m * (n * p) ≡⟨⟩
  suc m * (n * p)      ∎

-- Variant 1: using `rewrite`.
*-assoc' : ∀ (m n p : ℕ) → (m * n) * p ≡ m * (n * p)
*-assoc' zero n p = refl
*-assoc' (suc m) n p rewrite *-distᵣ-over-+ n (m * n) p | *-assoc' m n p = refl

-- Exercise *-comm (practice) --------------------------------------------------

-- Variant 1: using equational reasoning and `cong`.

n*0≡0 : ∀ (n : ℕ) → n * 0 ≡ 0
n*0≡0 zero =
  0 * 0 ≡⟨⟩
  0     ∎
n*0≡0 (suc n) =
  suc n * 0 ≡⟨⟩
  0 + n * 0 ≡⟨⟩
  n * 0     ≡⟨ n*0≡0 n ⟩
  0         ∎

*-comm-suc : ∀ (m n : ℕ) → n * suc m ≡ n + n * m
*-comm-suc m zero =
  0 * suc m ≡⟨⟩
  0         ≡⟨⟩
  0 + 0 * m ∎
*-comm-suc m (suc n) =
  suc n * suc m         ≡⟨⟩
  suc m + n * suc m     ≡⟨⟩
  suc (m + n * suc m)   ≡⟨ cong suc (cong (m +_) (*-comm-suc m n)) ⟩
  suc (m + (n + n * m)) ≡⟨ cong suc (sym (+-assoc m n (n * m))) ⟩
  suc ((m + n) + n * m) ≡⟨ cong suc (cong (_+ n * m) (+-comm m n)) ⟩
  suc ((n + m) + n * m) ≡⟨ cong suc (+-assoc n m (n * m)) ⟩
  suc (n + (m + n * m)) ≡⟨⟩
  suc (n + suc n * m)   ≡⟨⟩
  suc n + suc n * m     ∎

*-comm : ∀ (m n : ℕ) → m * n ≡ n * m
*-comm zero n =
  0 * n ≡⟨⟩
  0     ≡⟨ sym (n*0≡0 n) ⟩
  n * 0 ∎
*-comm (suc m) n =
  suc m * n ≡⟨⟩
  n + m * n ≡⟨ cong (n +_) (*-comm m n) ⟩
  n + n * m ≡⟨ sym (*-comm-suc m n) ⟩
  n * suc m ∎

-- Variant 2: using `rewrite`.

n*0≡0' : ∀ (n : ℕ) → n * 0 ≡ 0
n*0≡0' zero = refl
n*0≡0' (suc n) = n*0≡0' n

*-comm-suc' : ∀ (m n : ℕ) → n * suc m ≡ n + n * m
*-comm-suc' m zero = refl
*-comm-suc' m (suc n)
  rewrite *-comm-suc' m n
        | sym (+-assoc m n (n * m))
        | +-comm m n
        | +-assoc n m (n * m)
  = refl

*-comm' : ∀ (m n : ℕ) → m * n ≡ n * m
*-comm' zero n = sym (n*0≡0' n)
*-comm' (suc m) n rewrite *-comm' m n | *-comm-suc' m n = refl

-- Exercise 0∸n≡0 (practice) ---------------------------------------------------

-- Requires no induction, since the definition of ∸ is only recursive
-- if both operands are the successor of something.

0∸n≡n : ∀ (n : ℕ) → 0 ∸ n ≡ 0
0∸n≡n zero    = refl
0∸n≡n (suc n) = refl

-- Exercise ∸-+-assoc (practice) -----------------------------------------------

-- Proof by induction on `n`, and additionally case splitting on `m` in the
-- induction step.

-- Variant 1: using equational reasoning and `cong`.
∸-+-assoc : ∀ (m n p : ℕ) → (m ∸ n) ∸ p ≡ m ∸ (n + p)
∸-+-assoc m zero p =
  (m ∸ 0) ∸ p ≡⟨⟩
  m ∸ p       ≡⟨⟩
  m ∸ (0 + p) ∎
∸-+-assoc zero (suc n) p =
  (0 ∸ suc n) ∸ p ≡⟨⟩
  0 ∸ p           ≡⟨ 0∸n≡n p ⟩
  0               ≡⟨⟩
  0 ∸ suc (n + p) ≡⟨⟩
  0 ∸ (suc n + p) ∎
∸-+-assoc (suc m) (suc n) p =
  (suc m ∸ suc n) ∸ p ≡⟨⟩
  (m ∸ n) ∸ p         ≡⟨ ∸-+-assoc m n p ⟩
  m ∸ (n + p)         ≡⟨⟩
  suc m ∸ suc (n + p) ≡⟨⟩
  suc m ∸ (suc n + p) ∎

-- Variant 2: using the equality proofs directly.
∸-+-assoc' : ∀ (m n p : ℕ) → (m ∸ n) ∸ p ≡ m ∸ (n + p)
∸-+-assoc' m       zero    p = refl
∸-+-assoc' zero    (suc n) p = 0∸n≡n p
∸-+-assoc' (suc m) (suc n) p = ∸-+-assoc' m n p

-- Exercise +*^ (stretch) ------------------------------------------------------

-- Context

n+0≡0 : (n : ℕ) → n + 0 ≡ n
n+0≡0 zero    = refl
n+0≡0 (suc n) = cong suc (n+0≡0 n)

-- Actual Exercise

-- Variant 1: using equational reasoning and `cong`.

^-distribˡ-+-* : ∀ (m n p : ℕ) → m ^ (n + p) ≡ (m ^ n) * (m ^ p)
^-distribˡ-+-* m zero p =
  m ^ (0 + p)         ≡⟨⟩
  m ^ p               ≡⟨ sym (n+0≡0 (m ^ p)) ⟩
  m ^ p + 0           ≡⟨⟩
  m ^ p + 0 * (m ^ p) ≡⟨⟩
  1 * (m ^ p)         ≡⟨⟩
  (m ^ 0) * (m ^ p)   ∎
^-distribˡ-+-* m (suc n) p =
  m ^ (suc n + p)       ≡⟨⟩
  m ^ suc (n + p)       ≡⟨⟩
  m * m ^ (n + p)       ≡⟨ cong (m *_) (^-distribˡ-+-* m n p) ⟩
  m * (m ^ n * (m ^ p)) ≡⟨ sym (*-assoc m (m ^ n) (m ^ p)) ⟩
  (m * m ^ n) * (m ^ p) ≡⟨⟩
  (m ^ suc n) * (m ^ p) ∎

^-distribʳ-* : ∀ (m n p : ℕ) → (m * n) ^ p ≡ (m ^ p) * (n ^ p)
^-distribʳ-* m n zero =
  (m * n) ^ 0       ≡⟨⟩
  1                 ≡⟨⟩
  1 * 1             ≡⟨⟩
  (m ^ 0) * (n ^ 0) ∎
^-distribʳ-* m n (suc p) =
  (m * n) ^ suc p             ≡⟨⟩
  (m * n) * (m * n) ^ p       ≡⟨ cong (m * n *_) (^-distribʳ-* m n p) ⟩
  (m * n) * (m ^ p * n ^ p)   ≡⟨ *-assoc m n (m ^ p * n ^ p) ⟩
  m * (n * (m ^ p * n ^ p))   ≡⟨ cong (m *_) (sym (*-assoc n (m ^ p) (n ^ p))) ⟩
  m * ((n * m ^ p) * (n ^ p)) ≡⟨ cong (m *_) (cong (_* n ^ p) (*-comm n (m ^ p))) ⟩
  m * ((m ^ p * n) * (n ^ p)) ≡⟨ cong (m *_) (*-assoc (m ^ p) n (n ^ p)) ⟩
  m * (m ^ p * (n * n ^ p))   ≡⟨ sym (*-assoc m (m ^ p) (n * (n ^ p))) ⟩
  (m * m ^ p) * (n * n ^ p)   ≡⟨⟩
  (m ^ suc p) * (n ^ suc p)   ∎

-- Lemma for ^-*-assoc
1^n≡1 : ∀ (n : ℕ) → 1 ^ n ≡ 1
1^n≡1 zero =
  1 ^ 0 ≡⟨⟩
  1     ∎
1^n≡1 (suc n) =
  1 ^ suc n          ≡⟨⟩
  1 * 1 ^ n          ≡⟨⟩
  1 ^ n + 0 * 1 ^ n  ≡⟨⟩
  1 ^ n + 0          ≡⟨ n+0≡0 (1 ^ n) ⟩
  1 ^ n              ≡⟨ 1^n≡1 n ⟩
  1                  ∎

^-*-assoc : ∀ (m n p : ℕ) → (m ^ n) ^ p ≡ m ^ (n * p)
^-*-assoc m zero p =
  (m ^ 0) ^ p ≡⟨⟩
  1 ^ p       ≡⟨ 1^n≡1 p ⟩
  1           ≡⟨⟩
  m ^ 0       ≡⟨⟩
  m ^ (0 * p) ∎
  --
^-*-assoc m (suc n) p =
  (m ^ suc n) ^ p     ≡⟨⟩
  (m * m ^ n) ^ p     ≡⟨ ^-distribʳ-* m (m ^ n) p ⟩
  m ^ p * (m ^ n) ^ p ≡⟨ cong ((m ^ p) *_) (^-*-assoc m n p) ⟩
  m ^ p * m ^ (n * p) ≡⟨ sym (^-distribˡ-+-* m p (n * p)) ⟩
  m ^ (p + n * p)     ≡⟨⟩
  m ^ (suc n * p)     ∎

-- Variant 2: using `rewrite`.

^-distribˡ-+-*' : ∀ (m n p : ℕ) → m ^ (n + p) ≡ (m ^ n) * (m ^ p)
^-distribˡ-+-*' m zero    p rewrite n+0≡0 (m ^ p) = refl
^-distribˡ-+-*' m (suc n) p rewrite *-assoc m (m ^ n) (m ^ p) | ^-distribˡ-+-*' m n p = refl

^-distribʳ-*' : ∀ (m n p : ℕ) → (m * n) ^ p ≡ (m ^ p) * (n ^ p)
^-distribʳ-*' m n zero = refl
^-distribʳ-*' m n (suc p)
  rewrite ^-distribʳ-*' m n p
        | *-assoc m n (m ^ p * n ^ p)
        | sym (*-assoc n (m ^ p) (n ^ p))
        | *-comm n (m ^ p)
        | *-assoc (m ^ p) n (n ^ p)
        | sym (*-assoc m (m ^ p) (n * (n ^ p)))
  = refl

-- Lemma for ^-*-assoc
1^n≡1' : ∀ (n : ℕ) → 1 ^ n ≡ 1
1^n≡1' zero = refl
1^n≡1' (suc n) rewrite 1^n≡1' n | n+0≡0 1 = refl

^-*-assoc' : ∀ (m n p : ℕ) → (m ^ n) ^ p ≡ m ^ (n * p)
^-*-assoc' m zero p rewrite 1^n≡1 p = refl
^-*-assoc' m (suc n) p
  rewrite ^-distribʳ-* m (m ^ n) p
        | ^-*-assoc' m n p
        | ^-distribˡ-+-* m p (n * p)
  = refl

-- Exercise Bin-laws (stretch) -------------------------------------------------

-- Context

data Bin : Set where
  ⟨⟩ : Bin
  _O : Bin → Bin
  _I : Bin → Bin

inc : Bin → Bin
inc ⟨⟩ = ⟨⟩ I
inc (b O) = b I
inc (b I) = (inc b) O

to : ℕ → Bin
to zero = ⟨⟩ O
to (suc n) = inc (to n)

from : Bin → ℕ
from ⟨⟩ = zero
from (b O) = 0 + 2 * from b
from (b I) = 1 + 2 * from b

-- Actual Exercise

-- Lemma for inc-is-suc.
*-distₗ-over-+ : ∀ (m n p : ℕ) → m * (n + p) ≡ m * n + m * p
*-distₗ-over-+ zero n p =
  0 * (n + p)   ≡⟨⟩
  0             ≡⟨⟩
  0 + 0         ≡⟨⟩
  0 * n + 0 * p ∎
*-distₗ-over-+ (suc m) n p =
  suc m * (n + p)           ≡⟨⟩
  (n + p) + m * (n + p)     ≡⟨ cong (n + p +_) (*-distₗ-over-+ m n p) ⟩
  (n + p) + (m * n + m * p) ≡⟨ +-assoc n p (m * n + m * p) ⟩
  n + (p + (m * n + m * p)) ≡⟨ cong (n +_) (sym (+-assoc p (m * n) (m * p))) ⟩
  n + ((p + m * n) + m * p) ≡⟨ cong (n +_) (cong (_+ m * p) (+-comm p (m * n))) ⟩
  n + ((m * n + p) + m * p) ≡⟨ cong (n +_) (+-assoc (m * n) p (m * p)) ⟩
  n + (m * n + (p + m * p)) ≡⟨ sym (+-assoc n (m * n) (p + m * p)) ⟩
  (n + m * n) + (p + m * p) ≡⟨⟩
  suc m * n + suc m * p     ∎

inc-is-suc : ∀ (b : Bin) → from (inc b) ≡ suc (from b)
inc-is-suc ⟨⟩ =
  from (inc ⟨⟩)          ≡⟨⟩
  from (⟨⟩ I)            ≡⟨⟩
  1                      ≡⟨⟩
  suc 0                  ≡⟨⟩
  suc (from ⟨⟩)          ∎
inc-is-suc (b O) =
  from (inc (b O))       ≡⟨⟩
  from (b I)             ≡⟨⟩
  1 + (2 * from b)       ≡⟨⟩
  1 + from (b O)         ∎
inc-is-suc (b I) =
  from (inc (b I))       ≡⟨⟩
  from ((inc b) O)       ≡⟨⟩
  0 + (2 * from (inc b)) ≡⟨⟩
  2 * from (inc b)       ≡⟨ cong (2 *_) (inc-is-suc b) ⟩
  2 * (1 + from b)       ≡⟨ *-distₗ-over-+ 2 1 (from b) ⟩
  2 + 2 * from b         ≡⟨⟩
  1 + from (b I)         ∎

from-to-inverse : ∀ (n : ℕ) → from (to n) ≡ n
from-to-inverse zero =
  from (to 0) ≡⟨⟩
  from (⟨⟩ O) ≡⟨⟩
  0           ∎
from-to-inverse (suc n) =
  from (to (suc n)) ≡⟨ refl ⟩
  from (inc (to n)) ≡⟨ inc-is-suc (to n) ⟩
  suc (from (to n)) ≡⟨ cong suc (from-to-inverse n) ⟩
  suc n             ∎

-- Counter example.
-- (There are in fact infinitely many counter examples, because all bitstrings
-- consisting only of zeros, i.e. `⟨⟩ O O ... O` are mapped to the natural
-- number `0` which is then mapped back to the bitstring `⟨⟩ O`.)
to-from-not-inverse : to (from ⟨⟩) ≡ ⟨⟩ O
to-from-not-inverse = refl
