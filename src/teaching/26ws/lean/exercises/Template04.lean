namespace Sheet04

-- Exercise 1: Do-notation and IO ----------------------------------------------
-- Replace each `sorry` by a definition. Write the declarations that are only
-- listed as comments yourself, with the types from the exercise sheet.

/-- Reads one line from standard input, without the trailing newline. -/
def readLine : IO String := do
  let stdin ← IO.getStdin
  let line ← stdin.getLine
  pure line.trimAscii.toString

/-- Runs `act` with `input` as standard input, so that IO functions that read
input can be tried with `#eval`. -/
def withInput (input : String) (act : IO α) : IO α := do
  let buffer ← IO.mkRef { data := input.toUTF8 : IO.FS.Stream.Buffer }
  let _ ← IO.setStdin (IO.FS.Stream.ofBuffer buffer)
  act

def greetFormal : IO Unit := do
  IO.println "What's your first name?"
  let first ← readLine
  IO.println "What's your surname?"
  let last ← readLine
  let greeting := "Hello, " ++ first ++ " " ++ last ++ "!"
  IO.println greeting

-- def greetFormal' ...

def outside : IO Unit := do
  IO.println "Do you want to go outside?"
  let answer ← readLine
  if answer == "yes" then do
    IO.println "It rains!"
    IO.println "Too bad!"
  else
    IO.println "It still rains! Not so bad!"

-- def outside' ...

-- partial def ask ...

-- partial def run ...

def todo : IO Unit := sorry

/-- Run the todo list in a terminal with `lake env lean --run Template04.lean`. -/
def _root_.main : IO Unit := todo

-- Exercise 2: Option and Except -----------------------------------------------

def getCell (table : List (List α)) (x y : Nat) : Option α :=
  sorry

inductive MatrixError where
  | invalidRow
  | invalidCol
  deriving Repr

-- def orThrow ...

-- def getCell' ...

def exampleTable : List (List Nat) :=
  [[1, 2, 3],
   [4, 5, 6]]

-- Exercise 3: Nondeterminism --------------------------------------------------

structure ND (α : Type) where
  run : List α

-- instance : Monad ND ...

-- def choose ...

-- def abort ...

abbrev Graph (n : Type) := List (n × List n)
abbrev Coloring (n c : Type) := List (n × c)

def solve [BEq n] [BEq c] (g : Graph n) (colors : List c) : ND (Coloring n c) :=
  sorry

--   1
--  / \
-- 0   3
--  \ /
--   2
def exampleGraph : Graph Nat :=
  [(0, [1, 2]), (1, [3, 0]), (2, [3, 0]), (3, [1, 2])]

-- Exercise 4: State -----------------------------------------------------------

structure State (σ : Type) (α : Type) where
  state ::
  run : σ → σ × α

-- instance : Monad (State σ) ...

-- def get ...

-- def put ...

-- def modify ...

-- The While language

abbrev Var := String

inductive Val where
  | int (n : Int)
  | bool (b : Bool)
  | unit
  | error (msg : String)
  deriving Repr, BEq, Inhabited

inductive Op where
  | add
  | sub
  | less
  deriving Repr

inductive Expr where
  | var (x : Var)
  | val (v : Val)
  | bin (e1 : Expr) (op : Op) (e2 : Expr)
  | assign (x : Var) (e : Expr)
  | loop (cond : Expr) (body : Expr)
  | seq (e1 : Expr) (e2 : Expr)
  deriving Repr

abbrev Env := List (Var × Val)

def opEval : Op → Val → Val → Val
  | .add, .int x, .int y => .int (x + y)
  | .sub, .int x, .int y => .int (x - y)
  | .less, .int x, .int y => .bool (x < y)
  | _, .error e, _ => .error e
  | _, _, .error e => .error e
  | _, _, _ => .error "operator cannot handle those arguments"

def update (x : Var) (v : Val) : Env → Env
  | [] => [(x, v)]
  | (y, w) :: env => if x == y then (x, v) :: env else (y, w) :: update x v env

partial def eval : Expr → Env → Env × Val
  | .var x, env =>
    match env.lookup x with
    | some v => (env, v)
    | none => (env, .error s!"variable {x} is not defined")
  | .val v, env => (env, v)
  | .bin e1 op e2, env =>
    let (env1, v1) := eval e1 env
    let (env2, v2) := eval e2 env1
    (env2, opEval op v1 v2)
  | .assign x e, env =>
    let (env1, v) := eval e env
    (update x v env1, .unit)
  | .loop cond body, env =>
    let (env1, v) := eval cond env
    match v with
    | .bool false => (env1, .unit)
    | .bool true => eval (.seq body (.loop cond body)) env1
    | .error e => (env1, .error e)
    | _ => (env1, .error "loop condition is not a bool")
  | .seq e1 e2, env =>
    let (env1, _) := eval e1 env
    eval e2 env1

-- x := 0; while x < 10 do x := x + 1; x + 5
def exampleExpr : Expr :=
  .seq (.assign "x" (.val (.int 0)))
    (.seq (.loop (.bin (.var "x") .less (.val (.int 10)))
                 (.assign "x" (.bin (.var "x") .add (.val (.int 1)))))
          (.bin (.var "x") .add (.val (.int 5))))

-- partial def eval' ...

-- Bonus: Reader and Output

structure Reader (ρ : Type) (α : Type) where
  reader ::
  run : ρ → α

-- instance : Monad (Reader ρ) ...

-- def ask' ...

class Monoid (α : Type) where
  op : α → α → α
  id : α

instance : Monoid String where
  op := (· ++ ·)
  id := ""

structure Output (β : Type) (α : Type) where
  out ::
  log : β
  val : α

-- instance [Monoid β] : Monad (Output β) ...

-- def tell ...

-- Examples from the exercise sheet --------------------------------------------
-- `#eval e` shows the value of `e`. `#guard b` evaluates the `Bool` expression
-- `b` and reports an error if it is `false`, like `assert` in other languages.
-- `e matches p` checks whether `e` matches the pattern `p`.
-- Uncomment each line once the function is defined.

-- #eval withInput "Ada\nLovelace\n" greetFormal'
-- #eval withInput "yes\n" outside'
-- #eval withInput "maybe\nyes\n" (ask "Do you want to quit?" ["yes", "no"])
-- #eval withInput "add\nFeed the fish\nadd\nSleep\ndisplay\nremove\n1\ndisplay\nquit\n" todo

-- #guard getCell exampleTable 2 1 == some 6
-- #guard getCell exampleTable 3 1 == none
-- #guard getCell' exampleTable 2 1 matches .ok 6
-- #guard getCell' exampleTable 0 2 matches .error .invalidRow
-- #guard getCell' exampleTable 3 0 matches .error .invalidCol

-- #guard (do let x ← choose [1, 2]; let y ← choose [10, 20]; pure (x + y) : ND Nat).run
--   == [11, 21, 12, 22]
-- #guard (do let x ← choose (List.range 10); if x % 2 == 0 then pure x else abort : ND Nat).run
--   == [0, 2, 4, 6, 8]
-- #guard (solve exampleGraph ["red", "blue"]).run ==
--   [[(3, "red"), (2, "blue"), (1, "blue"), (0, "red")],
--    [(3, "blue"), (2, "red"), (1, "red"), (0, "blue")]]
-- #guard (solve exampleGraph ["red"]).run == []

-- #guard (modify (· + 1) : State Nat Unit).run 5 == (6, ())
-- #guard (do let n ← get; put (n * 2); pure n : State Nat Nat).run 5 == (10, 5)
-- #guard eval exampleExpr [] == ([("x", .int 10)], .int 15)
-- #guard (eval' exampleExpr).run [] == ([("x", .int 10)], .int 15)
-- #guard (eval' (.bin (.var "y") .add (.val (.int 1)))).run []
--   == ([], .error "variable y is not defined")

-- #guard (do let r ← ask'; pure (r + 1) : Reader Nat Nat).run 41 == 42
-- #guard (do tell "a"; tell "b"; pure 3 : Output String Nat).log == "ab"

-- For interested provers: the monad laws ------------------------------------
-- Uncomment the instances once your Monad instances are defined, and fill in
-- the `sorry`s if you like.

class LawfulMonad (m : Type → Type) [Monad m] : Prop where
  pure_bind : ∀ {α β : Type} (x : α) (f : α → m β), pure x >>= f = f x
  bind_pure : ∀ {α : Type} (x : m α), x >>= pure = x
  bind_assoc : ∀ {α β γ : Type} (x : m α) (f : α → m β) (g : β → m γ),
    x >>= f >>= g = x >>= fun a => f a >>= g

class LawfulMonoid (α : Type) [Monoid α] : Prop where
  op_assoc : ∀ x y z : α, Monoid.op (Monoid.op x y) z = Monoid.op x (Monoid.op y z)
  id_op : ∀ x : α, Monoid.op Monoid.id x = x
  op_id : ∀ x : α, Monoid.op x Monoid.id = x

-- theorem State.pure_bind (x : α) (f : α → State σ β) :
--     pure x >>= f = f x :=
--   calc pure x >>= f
--     _ = ⟨fun s => let (s', a) := (s, x); (f a).run s'⟩ := rfl
--     _ = ⟨fun s => (f x).run s⟩ := rfl
--     _ = f x := rfl

-- theorem State.bind_pure (m : State σ α) :
--     m >>= pure = m :=
--   calc m >>= pure
--     _ = ⟨fun s => let (s', a) := m.run s; (s', a)⟩ := rfl
--     _ = ⟨fun s => m.run s⟩ := rfl
--     _ = m := rfl

-- theorem State.bind_assoc (m : State σ α) (f : α → State σ β) (g : β → State σ γ) :
--     m >>= f >>= g = m >>= fun x => f x >>= g :=
--   calc m >>= f >>= g
--     _ = ⟨fun s =>
--           let (s₁, a) := m.run s
--           let (s₂, b) := (f a).run s₁
--           (g b).run s₂⟩ := rfl
--     _ = m >>= fun x => f x >>= g := rfl

-- instance : LawfulMonad (State σ) where
--   pure_bind := State.pure_bind
--   bind_pure := State.bind_pure
--   bind_assoc := State.bind_assoc

-- instance : LawfulMonad (Reader ρ) where
--   pure_bind := sorry
--   bind_pure := sorry
--   bind_assoc := sorry

-- instance [Monoid β] [LawfulMonoid β] : LawfulMonad (Output β) where
--   pure_bind := sorry
--   bind_pure := sorry
--   bind_assoc := sorry

-- instance : LawfulMonad ND where
--   pure_bind := sorry
--   bind_pure := sorry
--   bind_assoc := sorry

end Sheet04
