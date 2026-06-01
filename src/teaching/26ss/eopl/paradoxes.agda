{-# OPTIONS --type-in-type --no-positivity-check --no-termination-check #-}
module paradoxes where
 
data ⊥ : Set where
 
⊥-elim : {A : Set} → ⊥ → A
⊥-elim ()  
 
module type-in-type where
 
  -- set theory analog: the collection of all sets V.
  -- why can't V be a set? cantor's theorem says every set is strictly smaller
  -- than its power set. but each subset of V is itself a set, hence an element
  -- of V, so P(V) ⊆ V — i.e. V is as big as P(V). contradiction. so V is too
  -- big to be a set; it is a proper *class* (describable, but never V ∈ V).
  -- --type-in-type makes Set : Set, which is exactly this V ∈ V (the universe
  -- as one of its own elements) — so it breaks in the same way.
  -- the fix is to stratify: Set₀ : Set₁ : Set₂ ... in type theory ≈ the
  -- set/class distinction in set theory; the universe always sits one level up.
  -- (this is girard's paradox, the cousin of burali-forti.)
 
  data D : Set where
    c : (f : (A : Set) → A → A) → D
 
  empty : D → ⊥
  empty (c f) = empty (f D (c f))
 
  absurd : ⊥
  absurd = empty (c λ A x → x)
 
module stricht-positivity where
 
  -- set theory analog: russell's paradox.
  -- "Bad → ⊥" reads as "Bad is false" / "not Bad". so the constructor c says:
  -- to have a Bad is exactly to have a proof that Bad is false. i.e. Bad holds
  -- iff Bad does not hold.
  -- in sets: russell forms R = { x | x ∉ x }, the set of all sets that do not
  -- contain themselves, and asks "is R ∈ R?"
  --   if R ∈ R then by its own definition R ∉ R,
  --   if R ∉ R then by its own definition R ∈ R.   contradiction either way.
  -- the culprit is the *negative* self-reference: Bad appears to the LEFT of
  -- an arrow (Bad → ⊥), just like x appears inside "x ∉ x".
  -- in the code: "unwrap x x" is x applied to itself = the test "x ∈ x",
  -- "c omega" is russell's set R, and "omega (c omega)" is the question R ∈ R.
  -- agda's strict-positivity check normally bans left-of-arrow occurrences;
  -- zfc bans it via the separation axiom (you may only carve subsets out of an
  -- already-existing set, never the set of all non-self-members).
 
  data Bad : Set where
    c : (Bad → ⊥) → Bad
 
  unwrap : Bad → (Bad → ⊥)
  unwrap (c f) = f
 
  omega : Bad → ⊥
  omega x = unwrap x x
 
  absurd : ⊥
  absurd = omega (c omega)
 
module non-termination where 
 
  -- set theory analog: a circular / non-well-founded "definition".
  -- this "proof" of ⊥ just cites itself: to prove ⊥, use absurd... which is a
  -- proof of ⊥. it never reaches an axiom or base case, so it justifies nothing.
  -- in sets this is what the axiom of foundation (regularity) forbids: there is
  -- no infinite descending chain ... ∈ x₂ ∈ x₁ ∈ x₀, and in particular no set
  -- with x ∈ x. every set is built up from ∅ in well-founded steps.
  -- agda's termination checker plays the role of foundation here.
 
  absurd : ⊥
  absurd = absurd
