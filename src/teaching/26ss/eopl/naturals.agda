open import Relation.Binary.PropositionalEquality using (_≡_; refl; module ≡-Reasoning)
open ≡-Reasoning

-- Definition of natural numbers
data ℕ : Set where
  zero : ℕ
  suc  : ℕ → ℕ

-- Allows us to write `1`, `2`, `3`, ... as syntactic sugar for `zero`,
-- `suc zero`, and `suc (suc zero)`, ...
{-# BUILTIN NATURAL ℕ #-}

--------------------------------------------------------------------------------
-- #### Exercise `seven` (practice) {#seven}

-- Write out `7` in longhand.

seven : ℕ
seven = suc (suc (suc (suc (suc (suc (suc zero))))))
--------------------------------------------------------------------------------

infixl 6 _+_

_+_ : ℕ → ℕ → ℕ
zero + n = n               -- equation (1)
(suc m) + n = suc (m + n)  -- equation (2)

--------------------------------------------------------------------------------
-- #### Exercise `+-example` (practice) {#plus-example}

-- Compute `3 + 4`, writing out your reasoning as a chain of
-- equations, using the equations for `+`.

+-example : 3 + 4 ≡ 7
+-example =
  begin
    3 + 4
  ≡⟨⟩ -- 3 is just syntactic sugar for a combination of `suc` and `zero`
    (suc (suc (suc zero))) + 4
  ≡⟨⟩ -- according to definition of _+_, equation (2)
    suc ((suc (suc zero)) + 4)
  ≡⟨⟩ -- according to definition of _+_, equation (2)
    suc (suc ((suc zero) + 4))
  ≡⟨⟩ -- according to definition of _+_, equation (2)
    suc (suc (suc (zero + 4)))
  ≡⟨⟩ -- according to definition of _+_, equation (1)
    suc (suc (suc 4))
  ≡⟨⟩ -- 4 and 7 are just syntactic sugar for a combination of `suc` and `zero`
    7
  ∎

--------------------------------------------------------------------------------

infixl 7 _*_

_*_ : ℕ → ℕ → ℕ
zero    * n  =  zero
(suc m) * n  =  n + (m * n)

--------------------------------------------------------------------------------
-- #### Exercise `*-example` (practice) {#times-example}

-- Compute `3 * 4`, writing out your reasoning as a chain of equations, using the equations for `*`.
-- (You do not need to step through the evaluation of `+`.)

*-example : 3 * 4 ≡ 12
*-example =
  begin
    3 * 4
  ≡⟨⟩
    4 + (2 * 4)
  ≡⟨⟩
    4 + (4 + (1 * 4))
  ≡⟨⟩
    4 + (4 + (4 + (0 * 4)))
  ≡⟨⟩
    4 + (4 + (4 + 0))
  ≡⟨⟩
    4 + (4 + 4)
  ≡⟨⟩
    4 + 8
  ≡⟨⟩
    12
  ∎

--------------------------------------------------------------------------------
-- #### Exercise `_^_` (recommended) {#power}

-- Define exponentiation, which is given by the following equations:

--    m ^ 0        =  1
--    m ^ (1 + n)  =  m * (m ^ n)

-- Check that `3 ^ 4` is `81`.

infix 8 _^_

_^_ : ℕ → ℕ → ℕ
n ^ zero = 1
n ^ suc m = n * (n ^ m)

^-example : 3 ^ 4 ≡ 81
^-example =
  begin
    3 ^ 4
  ≡⟨⟩
    3 * (3 ^ 3)
  ≡⟨⟩
    3 * (3 * (3 ^ 2))
  ≡⟨⟩
    3 * (3 * (3 * (3 ^ 1)))
  ≡⟨⟩
    3 * (3 * (3 * (3 * (3 ^ 0))))
  ≡⟨⟩
    3 * (3 * (3 * (3 * 1)))
  ≡⟨⟩
    3 * (3 * (3 * 3))
  ≡⟨⟩
    3 * (3 * 9)
  ≡⟨⟩
    3 * 27
  ≡⟨⟩
    81
  ∎

--------------------------------------------------------------------------------

infixl 6  _∸_

_∸_ : ℕ → ℕ → ℕ
m     ∸ zero   =  m
zero  ∸ suc n  =  zero
suc m ∸ suc n  =  m ∸ n

--------------------------------------------------------------------------------
-- #### Exercise `∸-example₁` and `∸-example₂` (recommended) {#monus-examples}

-- Compute `5 ∸ 3` and `3 ∸ 5`, writing out your reasoning as a chain of equations.

∸-example₁ : 5 ∸ 3 ≡ 2
∸-example₁ =
  begin
    5 ∸ 3
  ≡⟨⟩
    4 ∸ 2
  ≡⟨⟩
    3 ∸ 1
  ≡⟨⟩
    2 ∸ 0
  ≡⟨⟩
    2
  ∎

∸-example₂ : 3 ∸ 5 ≡ 0
∸-example₂ =
  begin
    3 ∸ 5
  ≡⟨⟩
    2 ∸ 4
  ≡⟨⟩
    1 ∸ 3
  ≡⟨⟩
    0 ∸ 2
  ≡⟨⟩
    0
  ∎

--------------------------------------------------------------------------------
-- #### Exercise `Bin` (stretch) {#Bin}

-- A more efficient representation of natural numbers uses a binary
-- rather than a unary system.  We represent a number as a bitstring:

data Bin : Set where
  ⟨⟩ : Bin
  _O : Bin → Bin
  _I : Bin → Bin

-- For instance, the bitstring
-- 
--     1011
-- 
-- standing for the number eleven is encoded as
-- 
--     ⟨⟩ I O I I
-- 
-- Representations are not unique due to leading zeros.
-- Hence, eleven is also represented by `001011`, encoded as:
-- 
--     ⟨⟩ O O I O I I
-- 
-- Define a function
-- 
--     inc : Bin → Bin
-- 
-- that converts a bitstring to the bitstring for the next higher
-- number.  For example, since `1100` encodes twelve, we should have:
-- 
--     inc (⟨⟩ I O I I) ≡ ⟨⟩ I I O O
-- 
-- Confirm that this gives the correct answer for the bitstrings
-- encoding zero through four.
-- 
-- Using the above, define a pair of functions to convert
-- between the two representations.
-- 
--     to   : ℕ → Bin
--     from : Bin → ℕ
-- 
-- For the former, choose the bitstring to have no leading zeros if it
-- represents a positive natural, and represent zero by `⟨⟩ O`.
-- Confirm that these both give the correct answer for zero through four.

-- Note: This is an _easier_ version of the function, that we defined in the tutorial.
-- Put 15 computer scientists in a room, and they can't increment a binary number correctly!

inc : Bin → Bin
inc ⟨⟩    = ⟨⟩ I
inc (b O) = b I
inc (b I) = (inc b) O

inc-example₀ : inc (⟨⟩ O) ≡ ⟨⟩ I
inc-example₀ = refl

inc-example₁ : inc (⟨⟩ I) ≡ ⟨⟩ I O
inc-example₁ = refl

inc-example₂ : inc (⟨⟩ I O) ≡ ⟨⟩ I I
inc-example₂ = refl

inc-example₃ : inc (⟨⟩ I I) ≡ ⟨⟩ I O O
inc-example₃ = refl

inc-example₄ : inc (⟨⟩ I O O) ≡ ⟨⟩ I O I
inc-example₄ = refl

to : ℕ → Bin
to zero    = ⟨⟩ O
to (suc n) = inc (to n)

to-example₀ : to 0 ≡ ⟨⟩ O
to-example₀ = refl

to-example₁ : to 1 ≡ ⟨⟩ I
to-example₁ = refl

to-example₂ : to 2 ≡ ⟨⟩ I O
to-example₂ = refl

to-example₃ : to 3 ≡ ⟨⟩ I I
to-example₃ = refl

to-example₄ : to 4 ≡ ⟨⟩ I O O
to-example₄ = refl

from : Bin → ℕ
from ⟨⟩    = zero
from (b O) = 0 + (2 * from b)
from (b I) = 1 + (2 * from b)

from-example₀ : from (⟨⟩ O) ≡ 0
from-example₀ = refl

from-example₁ : from (⟨⟩ I) ≡ 1
from-example₁ = refl

from-example₂ : from (⟨⟩ I O) ≡ 2
from-example₂ = refl

from-example₃ : from (⟨⟩ I I) ≡ 3
from-example₃ = refl

from-example₄ : from (⟨⟩ I O O) ≡ 4
from-example₄ = refl

--------------------------------------------------------------------------------
