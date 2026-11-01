-- lecture01: all Lean code from the slides, in slide order.

/- Functional vs Imperative Programming: Variables ----------------------- -/

def x : Nat := 5

def y : Unit :=
  let x := 5
  let x := x + 1   -- a new x that hides the old one
  ()

/- Functional vs Imperative Programming: Functions ----------------------- -/

def f (x y : Nat) : Nat := 2 * x + y
#eval f 42 16   -- always 100

/- Equational Reasoning and Referential Transparency --------------------- -/

theorem f_zero (y : Nat) : f 0 y = y := by simp [f]

/- Setting up Lean ------------------------------------------------------- -/

#eval 1 + 1

/- A first definition ---------------------------------------------------- -/

def double (n : Nat) : Nat := n + n

/- Using the definition: #eval and #check -------------------------------- -/

#eval double 7

#check double
#check double 7

/- A conditional expression ---------------------------------------------- -/

def larger (x y : Nat) : Nat := if x < y then y else x

#eval larger 12 9
#eval larger 9 12
#eval larger (double 3) 5

/- Every value has a type ------------------------------------------------ -/

#check 7
#check "seven"
#check true
#check 7.5
#check double 7

/- Reading a type error -------------------------------------------------- -/

-- deliberate error on the slide; uncomment to see it
-- #eval double "seven"

/- Types matter ---------------------------------------------------------- -/

#eval 7 - 9
#eval (7 - 9 : Int)

#eval 123456789 * 123456789
#eval (123456789 * 123456789 : Float)

/- Type inference -------------------------------------------------------- -/

def price := 79          -- no type given
def answer := double 21  -- result type of double

#check price
#check answer

/- Anonymous functions --------------------------------------------------- -/

#check fun n : Nat => n + 1
#eval (fun n : Nat => n + 1) 41

/- A first theorem (preview) --------------------------------------------- -/

theorem double_zero : double 0 = 0 := by
  rfl
