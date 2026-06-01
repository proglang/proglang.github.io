open import Level using (Level; _⊔_) renaming (zero to lzero; suc to lsuc)
open import Data.Nat using (ℕ; zero; suc; _+_)
open import Data.Nat.Properties using (+-comm; +-identityʳ; +-suc)
open import Relation.Binary.PropositionalEquality using (_≡_; refl; sym; trans; cong; subst; module ≡-Reasoning)

-- The Plan
-- ========
--
-- 1) Talk about "definitional vs propositional" equality
-- 2) Recap universe levels and universe polymorphism
-- 3) Isomorphisms
-- 4) Paradoxes! (if we have time)

-- Appendix: solutions for equality chapter exercises

------------------------------------------------------

foo : ∀ n → n + 0 ≡ n
foo zero = refl
foo (suc n) = cong suc (foo n)

-- propositional equality
data _≡′_ {A : Set} (x : A) : A → Set where
  refl : x ≡′ x -- equal if they are definitional equal..

cong′ : ∀ {A B : Set} (f : A → B) {x y : A}
  → x ≡ y
    ---------
  → f x ≡ f y
-- unification!
cong′ f refl  =  refl

subst′ : ∀ {A : Set} {x y : A} (P : A → Set)
  → x ≡ y
    ---------
  → P x → P y
subst′ P refl px = px
------------------------------------------------------

data _≡ℓ_ {ℓ : Level} {A : Set ℓ} (x : A) : A → Set ℓ where
  refl′ : x ≡ℓ x

lemma : Set₁ ≡ℓ Set₁
lemma = refl′

_∘_ : ∀ {ℓ₁ ℓ₂ ℓ₃ : Level} {A : Set ℓ₁} {B : Set ℓ₂} {C : Set ℓ₃}
  → (B → C) → (A → B) → (A → C)
(g ∘ f) x = g (f x)

open import Function

_⨾_ : ∀ {ℓ₁ ℓ₂ ℓ₃ : Level} {A : Set ℓ₁} {B : Set ℓ₂} {C : Set ℓ₃}
  → (A → B) → (B → C) → (A → C)
(f ⨾ g) x = g (f x)
------------------------------------------------------

infix 4 _≤_
data _≤_ : ℕ → ℕ → Set where
  z≤n : ∀ {n} → zero ≤ n
  s≤s : ∀ {m n} → m ≤ n → suc m ≤ suc n

≤-refl : ∀ {n} → n ≤ n
≤-refl {zero} = z≤n
≤-refl {suc n} = s≤s ≤-refl

≤-trans : ∀ {m n p} → m ≤ n → n ≤ p → m ≤ p
≤-trans z≤n n≤p = z≤n
≤-trans (s≤s m≤n) (s≤s n≤p) = s≤s (≤-trans m≤n n≤p)

-- Exercise ≤-Reasoning (stretch) ----------------------------------------------

module ≤-Reasoning where

  infixr 1 begin_
  infixr 2 _≤⟨_⟩_ _≡⟨_⟩_ _≡⟨⟩_
  infix  3 _∎

  begin_ : ∀ {m n} → m ≤ n → m ≤ n
  begin p = p

  _≤⟨_⟩_ : ∀ m {n p} → m ≤ n → n ≤ p → m ≤ p
  m ≤⟨ m≤n ⟩ n≤p = ≤-trans m≤n n≤p

  _∎ : ∀ n → n ≤ n
  _∎ e = ≤-refl

  -- Allows using ≡-proofs in ≤-chains, used in +-monoˡ-≤.
  _≡⟨_⟩_ : ∀ m {n p} → m ≡ n → n ≤ p → m ≤ p
  m ≡⟨ refl ⟩ n≤p = n≤p

  _≡⟨⟩_ : ∀ m {n} → m ≤ n → m ≤ n
  m ≡⟨⟩ m≤n = m≤n

module OldProofs where

  +-monoʳ-≤ : ∀ {n p q} → p ≤ q → n + p ≤ n + q
  +-monoʳ-≤ {zero}  p≤q = p≤q
  +-monoʳ-≤ {suc n} p≤q = s≤s (+-monoʳ-≤ p≤q)

  +-monoˡ-≤ : ∀ {m n p} → m ≤ n → m + p ≤ n + p
  +-monoˡ-≤ {m} {n} {p} m≤n rewrite +-comm m p | +-comm n p = +-monoʳ-≤ m≤n

  +-mono-≤ : ∀ {m n p q} → m ≤ n → p ≤ q → m + p ≤ n + q
  +-mono-≤ m≤n p≤q = ≤-trans (+-monoˡ-≤ m≤n) (+-monoʳ-≤ p≤q)

module NewProofs where

  +-monoʳ-≤ : ∀ {n p q} →
    p ≤ q →
    n + p ≤ n + q
  +-monoʳ-≤ {zero} {p} {q} p≤q =
    let open ≤-Reasoning in
    0 + p  ≡⟨⟩
    p      ≤⟨ p≤q ⟩
    q      ≡⟨⟩
    0 + q  ∎
  +-monoʳ-≤ {suc n} {p} {q} p≤q =
    let open ≤-Reasoning in
    suc n + p    ≡⟨⟩
    suc (n + p)  ≤⟨ s≤s (+-monoʳ-≤ p≤q) ⟩
    suc (n + q)  ≡⟨⟩
    suc n + q    ∎

  +-monoˡ-≤ : ∀ {m n p} →
    m ≤ n →
    m + p ≤ n + p
  +-monoˡ-≤ {m} {n} {p} m≤n =
    let open ≤-Reasoning in
    m + p  ≡⟨ +-comm m p ⟩
    p + m  ≤⟨ +-monoʳ-≤ m≤n ⟩
    p + n  ≡⟨ +-comm p n ⟩
    n + p  ∎

  +-mono-≤ : ∀ {m n p q} →
    m ≤ n →
    p ≤ q →
    m + p ≤ n + q
  +-mono-≤ {m} {n} {p} {q} m≤n p≤q =
    let open ≤-Reasoning in
    m + p  ≤⟨ +-monoˡ-≤ m≤n ⟩
    n + p  ≤⟨ +-monoʳ-≤ p≤q ⟩
    n + q  ∎

