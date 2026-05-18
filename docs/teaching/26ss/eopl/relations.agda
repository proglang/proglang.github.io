open import Relation.Binary.PropositionalEquality using (_≡_; _≢_; refl; cong; sym; module ≡-Reasoning)
open import Data.Nat using (ℕ; zero; suc; _+_; _*_)
open import Data.Nat.Properties using (+-comm; *-comm)

open ≡-Reasoning

-- Context

infix 4 _≤_

data _≤_ : ℕ → ℕ → Set where
  z≤n : ∀ {n} → zero ≤ n
  s≤s : ∀ {m n} → m ≤ n → suc m ≤ suc n

-- Exercise orderings (practice) -----------------------------------------------

-- Preorder which is not a partial order:
--   Consider a directed graph, where n ≤ n' holds if node n' can be reached
--   from node n by walking along a path of zero or more edges.
--   This relation is
--   - reflexive, because each node is reachable from itself by walking along zero
--     edges.
--   - transitive, because paths can be joined to longer paths.
--   - not anti-symmetric: We can have two distinct nodes n and n', where there's
--     an edge both from n to n' and from n' to n, i.e.
--     n ≤ n' ∧ n' ≤ n  does not imply  n ≡ n'.

-- Partial order which is not a total order:
--   The subset-relation ⊆ satisfies this criterion. It is
--   - reflexive: ∀ A. A ⊆ A
--   - transitive: ∀ A B C. A ⊆ B ∧ B ⊆ C → A ⊆ C
--   - anti-symmetric: ∀ A B. A ⊆ B ∧ B ⊆ A → A = B
--   but not total: {0} ⊈ {1} and {1} ⊈ {0}
--
--   Alternatively, we can obtain such an order by lifting ≤ on ℕ over pairs, i.e.
--   (m₁, m₂) ≤' (n₁, n₂) iff m₁ ≤ n₁ ∧ m₂ ≤ n₂.
--   This relation is
--   - reflexive
--   - transitive
--   - antisymmetric, because if (m₁, m₂) ≤' (n₁, n₂) and (n₁, n₂) ≤' (m₁, m₂),
--     then by definition of ≤' we have m₁ ≤ n₁, n₁ ≤ m₁, m₂ ≤ n₂, n₂ ≤ n₂,
--     so by antisymmetry of ≤, we have m₁ = n₁ and m₂ = n₂, which implies
--     (m₁, m₂) = (n₁, n₂)
--   - not total, because for example neither (1, 2) ≤' (2, 1) nor (2, 1) ≤' (1, 2)
--     is true.

≤-refl : ∀ {n} → n ≤ n
≤-refl {zero} = z≤n
≤-refl {suc n} = s≤s ≤-refl

≤-trans : ∀ {m n p} → m ≤ n → n ≤ p → m ≤ p
≤-trans z≤n n≤p = z≤n
≤-trans (s≤s m≤n) (s≤s n≤p) = s≤s (≤-trans m≤n n≤p)

-- Exercise ≤-antisym-cases (practice) -----------------------------------------

≤-antisym : ∀ {m n : ℕ}
  → m ≤ n
  → n ≤ m
    -----
  → m ≡ n
≤-antisym z≤n       z≤n       = refl
≤-antisym (s≤s m≤n) (s≤s n≤m) = cong suc (≤-antisym m≤n n≤m)

-- Question: Why can the following cases be omitted?
--
--   ≤-antisym z≤n       (s≤s n≤m) = ?
--   ≤-antisym (s≤s m≤n) z≤n       = ?
--
-- By looking at the constructors of _≤_ we can see that z≤n requires that
-- the left side of the inequality is 0, while s≤s requires that the right side
-- of the inequality is the successor of something:
--
--   data _≤_ : ℕ → ℕ → Set where
--     z≤n : ∀ {n} → zero ≤ n
--     s≤s : ∀ {m n} → m ≤ n → suc m ≤ suc n
--
-- If we look at ≤-antisym, then we can see that the parameters `m ≤ n` and
-- `n ≤ m` share the variable `m`.
-- Hence, if we know that the first parameter of type `m ≤ n` is constructed via
-- `z≤n`, then `m` must be 0, so the second paramter of type `n ≤ m` is actually
-- of type `n ≤ 0`, which can not be constructed by `s≤s`, since `0` is not
-- the successor of something.
--
-- The second case can be omitted for the same reason.

-- Note: Here we can use parameters (and not indices) 
-- because m and n are constant across the constructors.
data Total (m n : ℕ) : Set where

  forward :
      m ≤ n
      ---------
    → Total m n

  flipped :
      n ≤ m
      ---------
    → Total m n

≤-total : ∀ (m n : ℕ) → Total m n
≤-total zero    n                         =  forward z≤n
≤-total (suc m) zero                      =  flipped z≤n
≤-total (suc m) (suc n) with ≤-total m n
...                        | forward m≤n  =  forward (s≤s m≤n)
...                        | flipped n≤m  =  flipped (s≤s n≤m)


+-monoʳ-≤ : ∀ {n p q} → p ≤ q → n + p ≤ n + q
+-monoʳ-≤ {zero} p≤q = p≤q
+-monoʳ-≤ {suc n} p≤q = s≤s (+-monoʳ-≤ p≤q)

+-monoˡ-≤ : ∀ {m n p} → m ≤ n → m + p ≤ n + p
-- +-monoˡ-≤ {m} {n} {p} m≤n rewrite +-comm m p | +-comm n p = +-monoʳ-≤ m≤n
+-monoˡ-≤ {m} {n} {p} m≤n = subst-≤ (+-comm p m) (+-comm  p n) (+-monoʳ-≤ m≤n)
  where subst-≤ : ∀ {m n p q} → m ≡ n → p ≡ q → m ≤ p → n ≤ q
        subst-≤ refl refl m≤p = m≤p

+-mono-≤ : ∀ {m n p q} → m ≤ n → p ≤ q → m + p ≤ n + q
+-mono-≤ m≤n p≤q = ≤-trans (+-monoˡ-≤ m≤n) (+-monoʳ-≤ p≤q)

-- Exercise *-mono-≤ (stretch) -------------------------------------------------

*-mono-≤ : ∀ {m n p q : ℕ}
  → m ≤ n
  → p ≤ q
    -------------
  → m * p ≤ n * q
*-mono-≤ z≤n p≤q = z≤n
*-mono-≤ (s≤s m≤n) p≤q = +-mono-≤ p≤q (*-mono-≤ m≤n p≤q)

infix 4 _<_

data _<_ : ℕ → ℕ → Set where
  z<s : ∀ {n : ℕ} → zero < suc n
  s<s : ∀ {m n : ℕ} → m < n → suc m < suc n

-- Exercise <-trans (recommended) ----------------------------------------------

-- By induction on m < n. Similar to `≤-antisym-cases`, matching on the proof
-- of `m < n` determines that `n` has to be the successor of something,
-- so the proof of `n < p` can only be via `s<s` and not `z<s`.
<-trans : ∀ {m n p : ℕ} → m < n → n < p → m < p
<-trans z<s       (s<s n<p) = z<s
<-trans (s<s m<n) (s<s n<p) = s<s (<-trans m<n n<p)

-- Exercise trichotomy (practice) ----------------------------------------------

infix 4 _>_

_>_ : ℕ → ℕ → Set
m > n = n < m

module Variant1 where

  data <-Trichotomy (m n : ℕ) : Set where
    tri-< : m < n → <-Trichotomy m n
    tri-≡ : m ≡ n → <-Trichotomy m n
    tri-> : m > n → <-Trichotomy m n

  <-trichotomy : ∀ (m n : ℕ) → <-Trichotomy m n
  <-trichotomy zero    zero    = tri-≡ refl
  <-trichotomy zero    (suc n) = tri-< z<s
  <-trichotomy (suc m) zero    = tri-> z<s
  <-trichotomy (suc m) (suc n) with <-trichotomy m n
  ...                          | tri-< m<n = tri-< (s<s m<n)
  ...                          | tri-≡ m≡n = tri-≡ (cong suc m≡n)
  ...                          | tri-> m>n = tri-> (s<s m>n)

module Variant2 where

  -- This type describes the disjunction of two propositions A ∨ B, and will
  -- be covered in Chapter 'Connectives'. A proof of A ∨ B is either a proof
  -- of A (via constructor inj₁) or a proof of B (via constructor inj₂).
  infixr 1 _∨_
  data _∨_ (A : Set) (B : Set) : Set where
    inj₁ : A → A ∨ B
    inj₂ : B → A ∨ B

  -- This type describes the trichotomy property for an arbitrary binary
  -- relation R.
  -- `Trichotomy _<_` is equivalent to
  -- `∀ (m n : ℕ) → <-Trichotomy m n` from `Variant1`.
  Trichotomy : ∀ {A : Set} → (A → A → Set) → Set
  Trichotomy {A} R = ∀ (x y : A) → R x y ∨ x ≡ y ∨ R y x

  -- The actual proof is the same as in `Variant1`, except that we now
  -- use combinations of `inₗ` and `inᵣ` instead of `tri-<`, `tri-≡`, and `tri->`,
  -- which makes it less readable on first sight.
  <-trichotomy : Trichotomy _>_
  <-trichotomy zero    zero    = inj₂ (inj₁ refl)
  <-trichotomy zero    (suc n) = inj₂ (inj₂ z<s)
  <-trichotomy (suc m) zero    = inj₁ z<s
  <-trichotomy (suc m) (suc n) with <-trichotomy m n
  ...                          | inj₁ n<m        = inj₁ (s<s n<m)
  ...                          | inj₂ (inj₁ n≡m) = inj₂ (inj₁ (cong suc n≡m))
  ...                          | inj₂ (inj₂ n>m) = inj₂ (inj₂ (s<s n>m))

-- Exercise +-mono-< (practice) ------------------------------------------------


+-monoʳ-< : ∀ {m p q : ℕ} → p < q → m + p < m + q
+-monoʳ-< {zero}  p<q = p<q
+-monoʳ-< {suc n} p<q = s<s (+-monoʳ-< p<q)

+-monoˡ-< : ∀ {m n p : ℕ} → m < n → m + p < n + p
+-monoˡ-< {m} {n} {p} m<n = subst-< (+-comm p m) (+-comm p n) (+-monoʳ-< m<n)
-- +-monoˡ-< {m} {n} {p} m<n rewrite +-comm m p | +-comm n p = +-monoʳ-< m<n
  where subst-< : ∀ {m n p q} → m ≡ n → p ≡ q → m < p → n < q
        subst-< refl refl m<p = m<p

+-mono-< : ∀ {m n p q : ℕ} → m < n → p < q → m + p < n + q
+-mono-< m<n p<q = <-trans (+-monoˡ-< m<n) (+-monoʳ-< p<q)

-- Exercise ≤-iff-< (recommended) ----------------------------------------------

<→≤ : ∀ {m n} → m < n → suc m ≤ n
<→≤ z<s       = s≤s z≤n
<→≤ (s<s m<n) = s≤s (<→≤ m<n)

-- By induction on `m`.
≤→< : ∀ {m n} → suc m ≤ n → m < n
≤→< {zero}  {suc n} sm≤n       = z<s
≤→< {suc m} {suc n} (s≤s sm≤n) = s<s (≤→< sm≤n)

-- By induction on `sm≤n`.
≤→<' : ∀ {m n} → suc m ≤ n → m < n
≤→<' (s≤s z≤n)     = z<s
≤→<' (s≤s (s≤s x)) = s<s (≤→<' (s≤s x))

-- Exercise <-trans-revisited (practice) ---------------------------------------

-- Basic Idea:
-- Use <→≤ to convert the assumptions from < to ≤, i.e.
--   <→≤ m<n : suc m ≤ n
--   <→≤ n<p : suc n ≤ p
-- then apply transitivity of ≤ and use ≤→< to convert the result from ≤ back to <.

-- Problem: we cannot apply ≤-trans directly, because we miss a proof for
-- n ≤ suc n, so we prove it as a lemma first:

n≤sn : ∀ {n : ℕ} → n ≤ suc n
n≤sn {zero}  = z≤n
n≤sn {suc n} = s≤s n≤sn

<-trans' : ∀ {m n p : ℕ} → m < n → n < p → m < p
<-trans' m<n n<p =
  let sm≤n = <→≤ m<n in
  let sn≤p = <→≤ n<p in
  let sm≤p = ≤-trans sm≤n (≤-trans n≤sn sn≤p) in
  let m<p  = ≤→< sm≤p in
  m<p

-- or without let:
<-trans'' : ∀ {m n p : ℕ} → m < n → n < p → m < p
<-trans'' m<n n<p = ≤→< (≤-trans (<→≤ m<n) (≤-trans n≤sn (<→≤ n<p)))

data even : ℕ → Set
data odd  : ℕ → Set

data even where
  zero : even zero
  suc  : ∀ {n : ℕ} → odd n → even (suc n)

data odd where
  suc   : ∀ {n : ℕ} → even n → odd (suc n)

e+e≡e : ∀ {m n : ℕ} → even m → even n → even (m + n)
o+e≡o : ∀ {m n : ℕ} → odd m → even n → odd (m + n)

e+e≡e zero     en  =  en
e+e≡e (suc om) en  =  suc (o+e≡o om en)

o+e≡o (suc em) en  =  suc (e+e≡e em en)

-- Exercise o+o≡e (stretch) ----------------------------------------------------

o+o≡e : ∀ {m n : ℕ} → odd m → odd n → even (m + n)
o+o≡e {suc m} {suc n} (suc em) (suc en) rewrite +-comm m (suc n) = suc (suc (e+e≡e en em))

-- Exercise Bin-predicatives (stretch) -----------------------------------------

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

-- Exercise

data One : Bin → Set where
  one-I         : One (⟨⟩ I)
  one-left-of-O : ∀ {b : Bin} → One b → One (b O)
  one-left-of-I : ∀ {b : Bin} → One b → One (b I)

data Can : Bin → Set where
  can-zero : Can (⟨⟩ O)
  can-one  : ∀ {b : Bin} → One b → Can b

-- Lemma
inc-preserves-One : ∀ {b : Bin} → One b → One (inc b)
inc-preserves-One one-I                 = one-left-of-O one-I
inc-preserves-One (one-left-of-O one-b) = one-left-of-I one-b
inc-preserves-One (one-left-of-I one-b) = one-left-of-O (inc-preserves-One one-b)

inc-preserves-Can : ∀ {b : Bin} → Can b → Can (inc b)
inc-preserves-Can can-zero        = can-one one-I
inc-preserves-Can (can-one one-b) = can-one (inc-preserves-One one-b)

to-Can : ∀ {n : ℕ} → Can (to n)
to-Can {zero}  = can-zero
to-Can {suc n} = inc-preserves-Can (to-Can {n})

-- Next we're going to prove lemmas for:
--
--   to-from-inverse-Can : ∀ {b : Bin} → Can b → to (from b) ≡ b
--
-- Note that I didn't start by proving the lemmas, but by trying to prove the
-- theorem, which made it apparent which lemmas are needed. Hence, it's probably
-- easiest to read the rest of the code backwards.

*-mono-≤ʳ : ∀ {m p q : ℕ} → p ≤ q → m * p ≤ m * q
*-mono-≤ʳ {m} p≤q = *-mono-≤ (≤-refl {m}) p≤q

one→1≤ : ∀ {b : Bin} → One b → 1 ≤ from b
one→1≤ one-I = s≤s z≤n
one→1≤ {b} (one-left-of-O one-b) =
  let 1≤2 = s≤s z≤n in
  let 2≤2*from-b = *-mono-≤ʳ {2} (one→1≤ one-b) in
  ≤-trans 1≤2 2≤2*from-b
one→1≤ (one-left-of-I one-b) = s≤s z≤n

2*-is-shiftl' : ∀ {n : ℕ} → to (2 * suc n) ≡ (to (suc n)) O
2*-is-shiftl' {zero} = refl
2*-is-shiftl' {suc n} =
  to (2 * suc (suc n))       ≡⟨ cong to (*-comm 2 (suc (suc n))) ⟩
  to (suc (suc n) * 2)       ≡⟨⟩
  to (2 + (suc n * 2))       ≡⟨ cong to (cong (2 +_) (*-comm (suc n) 2)) ⟩
  to (2 + 2 * suc n)         ≡⟨⟩
  inc (inc (to (2 * suc n))) ≡⟨ cong inc (cong inc( 2*-is-shiftl' {n})) ⟩
  inc (inc ((to (suc n)) O)) ≡⟨⟩
  (inc (to (suc n))) O       ≡⟨⟩
  (to (suc (suc n))) O       ∎

2*-is-shiftl : ∀ {n : ℕ} → 1 ≤ n → to (2 * n) ≡ (to n) O
2*-is-shiftl {suc n} (s≤s z≤n) = 2*-is-shiftl' {n}

to-from-inverse-One : ∀ {b : Bin} → One b → to (from b) ≡ b
to-from-inverse-One one-I                 = refl
to-from-inverse-One {b O} (one-left-of-O one-b) =
  to (from (b O))       ≡⟨⟩
  to (2 * from b)       ≡⟨ 2*-is-shiftl (one→1≤ one-b) ⟩
  to (from b) O         ≡⟨ cong _O (to-from-inverse-One one-b) ⟩
  b O                   ∎
to-from-inverse-One {b I} (one-left-of-I one-b) =
  to (from (b I))       ≡⟨⟩
  to (1 + 2 * from b)   ≡⟨⟩
  inc (to (2 * from b)) ≡⟨ cong inc (2*-is-shiftl (one→1≤ one-b)) ⟩
  inc (to (from b) O)   ≡⟨⟩
  to (from b) I         ≡⟨ cong _I (to-from-inverse-One one-b) ⟩
  b I                   ∎

to-from-inverse-Can : ∀ {b : Bin} → Can b → to (from b) ≡ b
to-from-inverse-Can can-zero        = refl
to-from-inverse-Can (can-one one-b) = to-from-inverse-One one-b
