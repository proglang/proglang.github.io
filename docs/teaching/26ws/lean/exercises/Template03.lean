namespace Sheet03

-- Exercise 1: Overloading -----------------------------------------------------
-- Replace each `sorry` by a definition. Write the declarations that are only
-- listed as comments yourself, with the types from the exercise sheet.

-- def last' ...

structure V3 (α : Type) where
  x : α
  y : α
  z : α
  deriving Repr, BEq

-- instance ... : Inhabited (V3 α) ...

-- instance ... : Add (V3 α) ...

-- instance ... : Sub (V3 α) ...

-- instance ... : Neg (V3 α) ...

-- Exercise 2: Monoids ----------------------------------------------------------

class Monoid (α : Type) where
  op : α → α → α
  id : α

-- instance boolAnd ... : Monoid Bool ...

-- instance intAdd ... : Monoid Int ...

-- instance ... : Monoid (List α) ...

-- instance ... : Monoid (Option α) ...

-- instance ... : Monoid (α × β) ...

-- instance ... : Monoid (α → β) ...

-- def mconcat ...

-- instance (priority := low) boolOr ... : Monoid Bool ...

-- instance (priority := low) intMul ... : Monoid Int ...

-- Exercise 3: Foldable ---------------------------------------------------------

class Foldable (f : Type → Type) where
  foldr : (α → β → β) → β → f α → β

inductive BTree (α : Type) where
  | leaf
  | node (l : BTree α) (x : α) (r : BTree α)
  deriving Repr

def exampleTree : BTree Int :=
  .node (.node .leaf 1 .leaf) 2 (.node .leaf 3 (.node .leaf 4 .leaf))

instance : Foldable List where
  foldr := sorry

-- instance ... : Foldable Option ...

-- def BTree.foldr ...

-- instance ... : Foldable BTree ...

def fold [Foldable f] [Monoid α] (xs : f α) : α :=
  sorry

-- def toList ...

-- def length ...

-- def sum ...

-- Exercise 4: Lawful monoids --------------------------------------------------
-- Put the cursor after `by` and on each tactic to see the goal in the infoview.

class LawfulMonoid (α : Type) [Monoid α] : Prop where
  op_assoc : ∀ x y z : α, Monoid.op (Monoid.op x y) z = Monoid.op x (Monoid.op y z)
  id_op : ∀ x : α, Monoid.op Monoid.id x = x
  op_id : ∀ x : α, Monoid.op x Monoid.id = x

-- A worked example for the monoid (Nat, +, 0).

instance : Monoid Nat where
  op := (· + ·)
  id := 0

instance : LawfulMonoid Nat where
  op_assoc := by
    intro x y z
    show x + y + z = x + (y + z)
    omega
  id_op := by
    intro x
    show 0 + x = x
    omega
  op_id := by
    intro x
    show x + 0 = x
    omega

-- instance ... : LawfulMonoid Bool ...

-- instance ... : LawfulMonoid (Option α) ...

-- instance ... : LawfulMonoid (List α) ...

-- Bonus

-- instance ... : LawfulMonoid (α × β) ...

-- instance ... : LawfulMonoid (α → β) ...

-- theorem mconcat_append ...

-- Examples from the exercise sheet --------------------------------------------
-- `#eval e` shows the value of `e`. `#guard b` evaluates the `Bool` expression
-- `b` and reports an error if it is `false`, like `assert` in other languages.
-- Uncomment each line once the function is defined.

-- #guard last' [1, 2, 3] == 3
-- #guard (⟨1, 2, 3⟩ + ⟨10, 20, 30⟩ : V3 Int) == ⟨11, 22, 33⟩
-- #guard (⟨1, 2, 3⟩ - ⟨10, 20, 30⟩ : V3 Int) == ⟨-9, -18, -27⟩
-- #guard (-⟨1, -2, 3⟩ : V3 Int) == ⟨-1, 2, -3⟩
-- #guard Monoid.op true false == false
-- #guard Monoid.op (3 : Int) 4 == 7
-- #guard Monoid.op [1, 2] [3] == [1, 2, 3]
-- #guard Monoid.op (none : Option Nat) (some 1) == some 1
-- #guard Monoid.op (some 1) (some 2) == some 1
-- #guard Monoid.op (true, (100 : Int)) (false, 20) == (false, 120)
-- #guard (Monoid.op (fun x : Int => decide (x > 5)) (fun x => decide (x < 10))) 7 == true
-- #guard mconcat ([1, 5, 2] : List Int) == 8
-- #guard mconcat [true, false, true] == false
-- #guard mconcat (m := boolOr) [true, false, true] == true
-- #guard mconcat (m := intMul) [1, 5, 2] == 10
-- #guard (let _ : Monoid Bool := boolOr; mconcat [true, false, true]) == true
-- #guard toList exampleTree == [1, 2, 3, 4]
-- #guard toList (some 5) == [5]
-- #guard length exampleTree == 4
-- #guard length [10, 20, 30] == 3
-- #guard sum exampleTree == 10
-- #guard sum (some (7 : Int)) == 7
-- #guard fold [[1, 2], [3], [4, 5]] == [1, 2, 3, 4, 5]

end Sheet03
