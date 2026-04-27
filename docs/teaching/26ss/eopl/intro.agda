module intro where

-- What is (dependent) Type Theory (TT)?
-- - TT is functional programming language
--   with a very powerful static type system
-- - TT is a logical system using propositions as types
--   (Prop = Type, Proof = program) also Curry-Howard equivalence
-- - TT is an alternative foundation of Mathematics
--   alternative ZFC a ∈ A , a : A

-- Def. Bool (explain Set!)
data Bool : Set where 
  true  : Bool
  false : Bool

-- Def. neg (cmp. Rust | Haskell | Python?)

-- def neg(b: bool) -> bool:
--   match b:
--     case True: return False
--     case False: return True

-- Exc. Spacing & Mixfix
¬_ : Bool → Bool 
¬ true  = false
¬ false = true

-- Def. if_then_else_
if_then_else_ : ∀ {ℓ} {A : Set ℓ} → Bool → A → A → A
if true  then left else right = left
if false then left else right = right

-- Ex.  Compute something
foo : Bool
foo = if true then false else true
 
open import Data.Nat using (ℕ)

-- Def. A dependent function (uses ∀!)

-- def magic(b: bool) -> if b: bool else: int:
--   if b: 
--     return True
--   else:
--     return 5 


magic : (b : Bool) → if b then Bool else ℕ
magic true  = true
magic false = 5

-- Def. Unit, Empty, Pair
data ⊤ : Set where
  tt : ⊤

data ⊥ : Set where

data Pair (A : Set) (B : Set) : Set where
  _,_ : A → B → Pair A B 

_ : Pair Bool Bool
_ = true , false

-- WE DID NOT GET HERE
-- Curry Howard equivalence
-- Logic   | Type Theory
-- -----------------------------
-- A ∧ B   | ?
-- A ∨ B   | ?
-- ⊥       | ?
-- ⊤       | ? 
-- ¬ A     | ?
-- ∀x. A   | ?
-- ∃x. A   | ?
-- R A B   | ?