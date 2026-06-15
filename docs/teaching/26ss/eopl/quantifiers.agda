open import Data.Empty using (⊥; ⊥-elim)
open import Data.Nat
open import Data.Nat.Properties
open import Data.Product
open import Data.Sum
open import Relation.Binary.PropositionalEquality using (_≡_; refl; sym; trans; cong; subst; module ≡-Reasoning)
open import Relation.Nullary using (¬_)
open ≡-Reasoning

--------------
-- The Plan --
--------------
-- 1) discuss quantifier exercises
  -- 1.1) discuss definition
  -- 1.2) some proofs
-- 2) lecture part: decidable

-- Context ---------------------------------------------------------------------

infix 0 _≃_
record _≃_ (A B : Set) : Set where
  field
    to   : A → B
    from : B → A
    from∘to : ∀ (x : A) → from (to x) ≡ x
    to∘from : ∀ (y : B) → to (from y) ≡ y

-- Exercise ∀-distrib-× (recommended) ------------------------------------------

-- "Show that universals distribute over conjunction.
--  Compare this with the result (→-distrib-×) in Chapter Connectives."

∀-distrib-× : ∀ {A : Set} {B C : A → Set} →
  (∀ (x : A) → B x × C x) ≃ (∀ (x : A) → B x) × (∀ (x : A) → C x)
∀-distrib-× = record 
    { to      = λ f → (λ x → proj₁ (f x)) , λ x → proj₂ (f x) 
    ; from    = λ (f , g) x → (f x) , (g x) 
    ; from∘to = λ x → refl 
    ; to∘from = λ y → refl 
    }

-- The function `→-distrib-×` is a special case of `∀-distrib-×`:

→-distrib-× : ∀ {A B C : Set} → (A → B × C) ≃ 
  (A → B) × (A → C)
→-distrib-× {A} {B} {C} = ∀-distrib-× {A = A} {B = λ _ → B} {C = λ _ → C}

-- Exercise ⊎∀-implies-∀⊎ (practice) -------------------------------------------

-- "Show that a disjunction of universals implies a universal of disjunctions.
--  Does the converse hold? If so, prove; if not, explain why."

⊎∀-implies-∀⊎ : ∀ {A : Set} {B C : A → Set} →
  (∀ (x : A) → B x) ⊎ (∀ (x : A) → C x)  →  (∀ (x : A) → B x ⊎ C x)
⊎∀-implies-∀⊎ (inj₁ ∀x-Bx) = λ x → inj₁ (∀x-Bx x)
⊎∀-implies-∀⊎ (inj₂ ∀x-Cx) = λ x → inj₂ (∀x-Cx x)

-- The converse
--
--   (∀ (x : A) → B x ⊎ C x)  →  (∀ (x : A) → B x) ⊎ (∀ (x : A) → C x)
--
-- does not hold: if we have
--
--   (∀ (x : A) → B x ⊎ C x)
--
-- then it could be the case, that for some `x : A` we have `B x`, while
-- for other ´x : A` we have `C x`, so it's neither the case that for all
-- `x : A` we have `B x` nor the case that for all `x : A` we have `C x`.

-- Exercise ∀-× (practice) -----------------------------------------------------

-- "Consider the following type.

data Tri : Set where
  aa : Tri
  bb : Tri
  cc : Tri

-- Let B be a type indexed by Tri, that is B : Tri → Set. Show that ∀
-- (x : Tri) → B x is isomorphic to B aa × B bb × B cc.
-- Hint: you will need to postulate a version of extensionality that
-- works for dependent functions."

postulate fun-ext : ∀ {A : Set} {B : A → Set} {f g : (x : A) → B x} →
                    (∀ x → f x ≡ g x) → f ≡ g

-- Alternative:
--
--  The definition of the Functional Extensionality Axiom can also be
--  imported from the standard-library. Note that the definition
--  provided there is more general as our definition, since it allows
--  `A` and `B x` to have type `Set ℓ` for an arbitrary `ℓ`.
--
--     open import Axiom.Extensionality.Propositional using (Extensionality)
--     postulate fun-ext : ∀ {ℓ₁ ℓ₂} → Extensionality ℓ₁ ℓ₂
--
--   where `Extensionality` is defined as
--
--     Extensionality : (a b : Level) → Set _
--     Extensionality a b =
--       {A : Set a} {B : A → Set b} {f g : (x : A) → B x} →
--       (∀ x → f x ≡ g x) → f ≡ g

∀-× : ∀ {P : Tri → Set} → (∀ (x : Tri) → P x) ≃ (P aa × P bb × P cc)
∀-× = record
  { to      = λ ∀x-Px → ∀x-Px aa , ∀x-Px bb , ∀x-Px cc
  ; from    = λ where (Paa , Pbb , Pcc) → λ where aa → Paa
                                                  bb → Pbb
                                                  cc → Pcc
  ; from∘to = λ ∀x-Px → fun-ext λ where aa → refl
                                        bb → refl
                                        cc → refl
  ; to∘from = λ where (Paa , Pbb , Pcc) → refl
  }

-- Exercise ∃-distrib-⊎ (recommended) ------------------------------------------

-- "Show that existentials distribute over disjunction"

∃-distrib-⊎ : ∀ {A : Set} {B C : A → Set} →
  ∃[ x ] (B x ⊎ C x) ≃ (∃[ x ] B x) ⊎ (∃[ x ] C x)
∃-distrib-⊎ = record
  { to      = λ where (x , inj₁ Bx) → inj₁ (x , Bx)
                      (x , inj₂ Cx) → inj₂ (x , Cx)
  ; from    = λ where (inj₁ (x , Bx)) → x , inj₁ Bx
                      (inj₂ (x , Cx)) → x , inj₂ Cx
  ; from∘to = λ where (x , inj₁ Bx) → refl
                      (x , inj₂ Cx) → refl
  ; to∘from = λ where (inj₁ (x , Bx)) → refl
                      (inj₂ (x , Cx)) → refl
  }

-- Exercise ∃×-implies-×∃ (practice) -------------------------------------------

-- "Show that an existential of conjunctions implies a conjunction of existentials.
--  Does the converse hold? If so, prove; if not, explain why."

∃×-implies-×∃ : ∀ {A : Set} {B C : A → Set} →
  ∃[ x ] (B x × C x) → (∃[ x ] B x) × (∃[ x ] C x)
∃×-implies-×∃ (x , (Bx , Cx)) = (x , Bx) , (x , Cx)

-- The converse
--
--   (∃[ x ] B x) × (∃[ x ] C x)  →  ∃[ x ] (B x × C x)
--
-- does not hold, due to a similar argument as in Exercise `⊎∀-implies-∀⊎`:
-- if we have an `x` such that `B x` holds and *another* `x` such that `C x` holds,
-- then we cannot conclude that there is an `x` such that `B x` and `C x` holds, since
-- the two `x` might be different, e.g.
--
--   (∃[ x ] x ≡ 2) × (∃[ x ] x ≡ 3)
--
-- is true, but
--
--   ∃[ x ] (x ≡ 2 × x ≡ 3)
--
-- is not.

-- We can also prove in Agda that the converse is not true, where the
-- proof is precisely our counter-example:

¬[×∃-implies-∃×] :
 ¬ (
   ∀ {A : Set} {B C : A → Set} →
   (∃[ x ] B x) × (∃[ x ] C x) →
   ∃[ x ] (B x × C x)
 )
¬[×∃-implies-∃×] ×∃-implies-∃×
 with ×∃-implies-∃× {A = ℕ} {B = λ x → x ≡ 2} {C = λ x → x ≡ 3} ((2 , refl) , (3 , refl))
... | .2 , (refl , ())
-- The previous line can be obtained by matching first on `x≡2` and then on `x≡3` in the following line:
-- ... | x , (x≡2 , x≡3) = {!x≡2!}

-- Exercise ∃-⊎ (practice) -----------------------------------------------------

-- "Let Tri and B be as in Exercise ∀-×. Show that ∃[ x ] B x is isomorphic to B aa ⊎ B bb ⊎ B cc."

∃-⊎ : ∀ {B : Tri → Set} → ∃[ x ] B x ≃ B aa ⊎ (B bb ⊎ B cc)
∃-⊎ = record
  { to      = λ where (aa , Bx) → inj₁ Bx
                      (bb , Bx) → inj₂ (inj₁ Bx)
                      (cc , Bx) → inj₂ (inj₂ Bx)
  ; from    = λ where (inj₁ Bx)        → (aa , Bx)
                      (inj₂ (inj₁ Bx)) → (bb , Bx)
                      (inj₂ (inj₂ Bx)) → (cc , Bx)
  ; from∘to = λ where (aa , Bx) → refl
                      (bb , Bx) → refl
                      (cc , Bx) → refl
  ; to∘from = λ where (inj₁ Bx)        → refl
                      (inj₂ (inj₁ Bx)) → refl
                      (inj₂ (inj₂ Bx)) → refl
  }

-- Exercise ∃-even-odd (practice) ----------------------------------------------

-- "How do the proofs become more difficult if we replace m * 2 and 1 +
--  m * 2 by 2 * m and 2 * m + 1? Rewrite the proofs of ∃-even and
--  ∃-odd when restated in this way."

-- TODO

-- Exercise ∃-|-≤ (practice) ---------------------------------------------------

-- "Show that `y ≤ z` holds if and only if there exists a `x` such that `x + y ≡ z`."

variable y x : ℕ 


--+-monoʳ-≤ : ∀ {n p q} → p ≤ q → n + p ≤ n + q
--+-monoʳ-≤ {zero} p≤q = p≤q
--+-monoʳ-≤ {suc n} p≤q = s≤s (+-monoʳ-≤ p≤q)

y≤sy : y ≤ suc y
y≤sy {zero} = z≤n
y≤sy {suc y} = s≤s y≤sy

lemma : y ≤ x + y
lemma {y} {zero}      = ≤-refl
lemma {zero} {suc x}  = z≤n
lemma {suc y} {suc x} = s≤s (≤-trans (lemma {y = y} {x = x}) (+-monoʳ-≤ x y≤sy))

∃-+→≤ : ∀ {y z} → ∃[ x ] (x + y ≡ z) → y ≤ z
∃-+→≤ (fst , refl) = lemma

∃-+←≤ : ∀ {y z} → y ≤ z → ∃[ x ] (x + y ≡ z)
∃-+←≤ {z = z} z≤n = z , +-identityʳ z
∃-+←≤ (s≤s y≤x) with x , eq ← ∃-+←≤ y≤x =
   x , trans (+-suc _ _) (cong suc eq)

-- Exercise ∃¬-implies-¬∀ (recommended) ----------------------------------------

-- "Show that existential of a negation implies negation of a universal.
--  Does the converse hold? If so, prove; if not, explain why."

∃¬-implies-¬∀ : ∀ {A : Set} {B : A → Set}
  → ∃[ x ] (¬ B x)
    --------------
  → ¬ (∀ x → B x)
∃¬-implies-¬∀ (x , ¬Bx) f = ¬Bx (f x)

-- The converse
--
--   ¬ (∀ x → B x) → ∃[ x ] (¬ B x)
--
-- does not hold.
--
-- In the special case with `B = λ _ → B` for some `B : Set` we get
--
--   ¬ (A → B)  →  (A × ¬ B)
--
-- which turns a proof by contradiction into a counter-example.
-- Not possible in intuitionistic logic; however, the classical
-- theorem can be encoded via double negation translation.

-- Exercise Bin-isomorphism (stretch) ------------------------------------------

-- Lots of Context from Chapter 2 and 3 including Solutions 2 and 3

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

data One : Bin → Set where
  one-I         : One (⟨⟩ I)
  one-left-of-O : ∀ {b : Bin} → One b → One (b O)
  one-left-of-I : ∀ {b : Bin} → One b → One (b I)

data Can : Bin → Set where
  can-zero : Can (⟨⟩ O)
  can-one  : ∀ {b : Bin} → One b → Can b

module ToCan where
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

open ToCan using (to-Can)

module FromToInverse where
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

  from∘to≡id : ∀ (n : ℕ) → from (to n) ≡ n
  from∘to≡id zero =
    from (to 0) ≡⟨⟩
    from (⟨⟩ O) ≡⟨⟩
    0           ∎
  from∘to≡id (suc n) =
    from (to (suc n)) ≡⟨ refl ⟩
    from (inc (to n)) ≡⟨ inc-is-suc (to n) ⟩
    suc (from (to n)) ≡⟨ cong suc (from∘to≡id n) ⟩
    suc n             ∎

open FromToInverse using (from∘to≡id)

module ToFromInverseCan where
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

  One→to∘from≡id : ∀ {b : Bin} → One b → to (from b) ≡ b
  One→to∘from≡id one-I                 = refl
  One→to∘from≡id {b O} (one-left-of-O one-b) =
    to (from (b O))       ≡⟨⟩
    to (2 * from b)       ≡⟨ 2*-is-shiftl (one→1≤ one-b) ⟩
    to (from b) O         ≡⟨ cong _O (One→to∘from≡id one-b) ⟩
    b O                   ∎
  One→to∘from≡id {b I} (one-left-of-I one-b) =
    to (from (b I))       ≡⟨⟩
    to (1 + 2 * from b)   ≡⟨⟩
    inc (to (2 * from b)) ≡⟨ cong inc (2*-is-shiftl (one→1≤ one-b)) ⟩
    inc (to (from b) O)   ≡⟨⟩
    to (from b) I         ≡⟨ cong _I (One→to∘from≡id one-b) ⟩
    b I                   ∎

  Can→to∘from≡id : ∀ {b : Bin} → Can b → to (from b) ≡ b
  Can→to∘from≡id can-zero        = refl
  Can→to∘from≡id (can-one one-b) = One→to∘from≡id one-b

open ToFromInverseCan using (Can→to∘from≡id)

-- Exercise

-- "[...] Using the above, establish that there is an isomorphism
--  between ℕ and ∃[ b ] Can b."

-- "We recommend proving the following lemmas which show that, for a
--  given binary number b, there is only one proof of One b and
--  similarly for Can b."

≡One : ∀ {b : Bin} (o o' : One b) → o ≡ o'
≡One one-I             one-I                                = refl
≡One (one-left-of-O o) (one-left-of-O o') rewrite ≡One o o' = refl
≡One (one-left-of-I o) (one-left-of-I o') rewrite ≡One o o' = refl

≡Can : ∀ {b : Bin} (c c' : Can b) → c ≡ c'
≡Can can-zero                     can-zero                        = refl
≡Can (can-one o₁)                 (can-one o₂) rewrite ≡One o₁ o₂ = refl
≡Can can-zero                     (can-one (one-left-of-O ()))
≡Can (can-one (one-left-of-O ())) can-zero

-- "Many of the alternatives for proving to∘from turn out to be
--  tricky. However, the proof can be straightforward if you use the
--  following lemma, which is a corollary of ≡Can."

proj₁≡→Can≡ : {c c' : ∃[ b ] Can b} → proj₁ c ≡ proj₁ c' → c ≡ c'
proj₁≡→Can≡ {b , can-b} {b' , can-b'} b≡b' rewrite b≡b' | ≡Can can-b can-b' = refl

-- Given the lemmas above, we're ready to prove the actual theorem:

ℕ≃Can : ℕ ≃ ∃[ b ] (Can b)
ℕ≃Can = record
  { to      = to'
  ; from    = from'
  ; from∘to = from'∘to'
  ; to∘from = to'∘from'
  }
  where
    to' : ℕ → ∃[ b ] (Can b)
    to' n = (to n , to-Can {n})

    from' : ∃[ b ] (Can b) → ℕ
    from' (b , can-b) = from b

    from'∘to' : ∀ n → from' (to' n) ≡ n
    from'∘to' n =
      begin
        from' (to' n)
      ≡⟨⟩
        from (to n)
      ≡⟨ from∘to≡id n ⟩
        n
      ∎

    to'∘from' : ∀ b → to' (from' b) ≡ b
    to'∘from' (b , can-b) =
      begin
        to' (from' (b , can-b))
      ≡⟨⟩
        to' (from b)
      ≡⟨⟩
        to (from b) , to-Can {from b}
      ≡⟨ proj₁≡→Can≡ (Can→to∘from≡id can-b) ⟩
        (b , can-b)
      ∎
