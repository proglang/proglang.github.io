namespace Sheet01

-- Exercise 1: Warming up ------------------------------------------------------

def mini (x y : Int) : Int :=
  sorry

def maxi (x y : Int) : Int :=
  sorry

def max3 (x y z : Int) : Int :=
  sorry

def max3Tupled : Int × Int × Int → Int :=
  sorry

def med (x y z : Int) : Int :=
  sorry

-- Exercise 2: List functions --------------------------------------------------
-- Replace each `sorry` by a definition. Choose the types yourself where they
-- are missing, and make them reasonably polymorphic.

def null' : List α → Bool :=
  sorry

def sum' : List Int → Int :=
  sorry

-- def flatten' ...

-- def elem' ...

-- def take' ...

-- def drop' ...

-- def zip' ...

-- def reverse' ...

-- def intersperse' ...

-- Exercise 3: Empty lists -----------------------------------------------------

-- def initSafe ...

-- def init' ...

-- def lastSafe ...

-- Examples from the exercise sheet --------------------------------------------
-- `#eval e` shows the value of `e`. `#guard b` evaluates the `Bool` expression
-- `b` and reports an error if it is `false`, like `assert` in other languages.
-- Uncomment each line once the function is defined.

-- #guard null' ([] : List Nat) == true
-- #guard null' [1, 2] == false
-- #guard sum' [1, 2, 3] == 6
-- #guard flatten' [[1, 2, 3], [4], [5, 6]] == [1, 2, 3, 4, 5, 6]
-- #guard elem' 3 [1, 2, 3, 4] == true
-- #guard elem' 9 [1, 2, 3, 4] == false
-- #guard take' 3 [1, 2, 3, 4, 5] == [1, 2, 3]
-- #guard drop' 3 [1, 2, 3, 4, 5] == [4, 5]
-- #guard zip' [1, 2, 3] [true, false, true] == [(1, true), (2, false), (3, true)]
-- #guard zip' [1, 2, 3, 4] [10, 20] == [(1, 10), (2, 20)]
-- #guard reverse' [1, 2, 3] == [3, 2, 1]
-- #guard intersperse' 666 [1, 2, 3, 4] == [1, 666, 2, 666, 3, 666, 4]
-- #guard String.ofList (intersperse' ',' "abcde".toList) == "a,b,c,d,e"
-- #guard initSafe [1, 2, 3] == some [1, 2]
-- #guard initSafe ([] : List Nat) == none
-- #guard init' [1, 2, 3] == [1, 2]
-- #guard lastSafe [1, 2, 3] == some 3
-- #guard lastSafe ([] : List Nat) == none

end Sheet01
