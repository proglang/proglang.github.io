namespace Sheet01

-- Exercise 1: Warming up ------------------------------------------------------

def mini (x y : Int) : Int :=
  if x < y then x else y

def maxi (x y : Int) : Int :=
  if x < y then y else x

def max3 (x y z : Int) : Int :=
  maxi x (maxi y z)

def max3Tupled : Int × Int × Int → Int
  | (x, y, z) => max3 x y z

def med (x y z : Int) : Int :=
  max3 (mini x y) (mini x z) (mini y z)

-- Exercise 2: List functions --------------------------------------------------
-- Replace each `sorry` by a definition. Choose the types yourself where they
-- are missing, and make them reasonably polymorphic.

def null' : List α → Bool
  | _ :: _ => false
  | [] => true

def sum' : List Int → Int
  | []      => 0
  | x :: xs => x + sum' xs

def flatten' : List (List α) -> List α
  | [] => []
  | xs :: xss => xs ++ flatten' xss

def elem' : Int -> List Int -> Bool
  | _, [] => false
  | y, x :: xs =>
    if x == y then true else elem' y xs

def take' : Nat -> List α -> List α
  | n + 1, x :: xs => x :: (take' n xs)
  | _, _ => []

def drop' : Nat -> List α -> List α
  | n + 1, _ :: xs => drop' n xs
  | _, xs => xs

def zip' : List α -> List β -> List (α × β)
  | x :: xs, y :: ys => (x, y) :: zip' xs ys
  | _, _ => []

def reverse' : List α -> List α
  | [] => []
  | x :: xs => reverse' xs ++ [x]

def intersperse' : α -> List α -> List α
  | _, [] => []
  | _, [x] => [x]
  | y, x :: xs => x :: y :: intersperse' y xs

-- Exercise 3: Empty lists -----------------------------------------------------

def initSafe : List α -> Option (List α)
  | [] => none
  | [_] => some []
  | x :: xs => match initSafe xs with
    | some xs => some (x :: xs)
    | _ => none

def init' : List α -> List α
  | [] => panic! "the list was empty!"
  | [_] => []
  | x :: xs => x :: init' xs

def lastSafe : List α -> Option α
  | [] => none
  | [x] => some x
  | _ :: xs => lastSafe xs


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
