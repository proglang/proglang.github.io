open import Data.Nat using (ℕ; zero; suc; _+_)
open import Data.Nat.Properties using (+-comm; +-identityʳ; +-suc)
open import Relation.Binary.PropositionalEquality using (_≡_; refl; sym; trans; cong; cong-app; subst; module ≡-Reasoning)
open ≡-Reasoning

------------------------------------------------------

-- only use lambdas
_+′_ : ℕ → ℕ → ℕ
_+′_ = λ { m zero    → m
         ; m (suc n) → suc (m +′ n) }

postulate
  extensionality : ∀ {A B : Set} {f g : A → B}
    → (∀ (x : A) → f x ≡ g x)
      -----------------------
    → f ≡ g

un-extensionality : ∀ {A B : Set} {f g : A → B} → 
  f ≡ g → 
  -----------------------
  (∀ (x : A) → f x ≡ g x)
un-extensionality refl = λ x → refl

helper : ∀ m n → m + n ≡ m +′ n
helper m zero    = +-identityʳ m
helper m (suc n) = trans (+-suc m n) (cong suc (helper m n))

-- uses extensionality
same : _+_ ≡ _+′_
same = extensionality (λ m → extensionality 
  λ n → helper m n)

postulate
  ∀-extensionality : ∀ {A : Set} {B : A → Set} 
    {f g : ∀(x : A) → B x}
    → (∀ (x : A) → f x ≡ g x)
      -----------------------
    → f ≡ g
