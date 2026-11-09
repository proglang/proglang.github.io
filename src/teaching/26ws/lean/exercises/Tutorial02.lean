import Lean

namespace Sheet02

-- Exercise 1: Map, filter, and fold --------------------------------------------

def map' (f : α → β) : List α → List β
  | [] => []
  | x :: xs => f x :: map' f xs

def filter' (p : α → Bool) : List α → List α
  | [] => []
  | x :: xs => if p x then x :: filter' p xs else filter' p xs

def foldr' (f : α → β → β) (init : β) : List α → β
  | [] => init
  | x :: xs => f x (foldr' f init xs)

def incRec : List Int → List Int
  | [] => []
  | x :: xs => (x + 1) :: incRec xs

def inc : List Int → List Int := map' (· + 1)

def evenListRec : List Int → List Int
  | [] => []
  | x :: xs => if x % 2 == 0 then x :: evenListRec xs else evenListRec xs

def evenList : List Int → List Int :=  filter' (· % 2 == 0)

def shortStrsRec : List Int → List String
  | [] => []
  | x :: xs =>
    if (toString x).length ≤ 2 then toString x :: shortStrsRec xs else shortStrsRec xs

def shortStrs : List Int → List String :=
  filter' (·.length <= 2) ∘ (map' toString)

def andRec : List Bool → Bool
  | [] => true
  | b :: bs => b && andRec bs

def and' : List Bool → Bool :=
  foldr' and true

def orRec : List Bool → Bool
  | [] => false
  | b :: bs => b || orRec bs

def or' : List Bool → Bool :=
  foldr' or false

def allRec : (α → Bool) → List α → Bool
  | _, [] => true
  | p, x :: xs => p x && allRec p xs

def all' : (α → Bool) → List α → Bool :=
  (and' ∘ map' ·)

def anyRec : (α → Bool) → List α → Bool
  | _, [] => false
  | p, x :: xs => p x || anyRec p xs

def any' :  (α → Bool) → List α → Bool :=
  (or' ∘ map' ·)

def lengthRec : List α → Nat
  | [] => 0
  | _ :: xs => 1 + lengthRec xs

def length' : List α → Nat :=
  foldr' (λ _ => (1 + ·)) 0

def idMap : List α → List α :=
  map' id

def idFilter : List α → List α :=
  filter' (fun _ => true)
open List

def idFold : List α → List α :=
  foldr' cons []

def mapFold (f : α → β) : List α → List β :=
  foldr' (cons ∘ f) []

def filterFold (p : α → Bool) : List α → List α :=
  foldr' (fun x acc => if p x then x :: acc else acc) []

-- Exercise 2: Three-dimensional vectors ----------------------------------------

structure V3 (α : Type) where
  x : α
  y : α
  z : α
  deriving Repr, BEq

def exampleV3 : V3 Int := ⟨5, 3, 8⟩

def mapV3 (f : α → β) : V3 α → V3 β
  | ⟨ x, y, z ⟩ => { y := f y, x := f x, z := f z }

def liftV3 (f : α → β → γ) : V3 α → V3 β → V3 γ
  | ⟨ x₁, y₁, z₁ ⟩, ⟨ x₂, y₂, z₂ ⟩ => ⟨ f x₁ x₂, f y₁ y₂, f z₁ z₂ ⟩

def negV3 := mapV3 (- ·)

def addV3 : V3 Int → V3 Int → V3 Int := liftV3 (· + ·)

def subV3 : V3 Int → V3 Int → V3 Int := liftV3 (· - ·)

def mulV3 : V3 Int → V3 Int → V3 Int := liftV3 (· * ·)

def divV3 : V3 Int → V3 Int → V3 Int := liftV3 (· / ·)

-- Exercise 3: Tic-tac-toe ------------------------------------------------------

inductive Token where
  | X | O | E
  deriving Repr, BEq

-- Lets us write `X` instead of `Token.X`.
open Token

abbrev Board := List (List Token)

def showToken : Token → String
  | X => "X"
  | O => "O"
  | E => "_"

def showBoard (b : Board) : String :=
  "\n".intercalate (map' (fun row => " ".intercalate (map' showToken row)) b)

def exampleBoard : Board :=
  [ [X, O, E],
    [X, O, E],
    [X, E, E] ]

def emptyBoard (n : Nat) : Board :=
  List.replicate n (List.replicate n E)

def isFull (b : Board) : Bool :=
  all' (all' (· != E)) b

def mapAtM : Nat → (α → Option α) → List α → Option (List α)
  | _, _, [] => none
  | 0, f, x :: xs => Option.map (· :: xs) (f x)
  | n + 1, f, x :: xs => Option.map (x :: ·) (mapAtM n f xs)

def setToken : Nat × Nat → Token → Board → Option Board
  | (x, y), t => mapAtM y (mapAtM x (fun old => if old == E then some t else none))

def column (b : Board) (i : Nat) : List Token :=
  map' (fun row => row.getD i E) b

def diagonal (b : Board) : List Token :=
  map' (fun i => (b.getD i []).getD i E) (List.range b.length)

-- All rows, columns, and diagonals of the board.
def lines (b : Board) : List (List Token) :=
  b ++ map' (column b) (List.range b.length) ++ [diagonal b, diagonal b.reverse]

-- Whether player `p` fills one of the lines.
def wins (p : Token) (b : Board) : Bool :=
  any' (all' (· == p)) (lines b)

def winner (b : Board) : Token :=
  if wins X b then X else if wins O b then O else E

-- Examples from the exercise sheet --------------------------------------------
-- `#eval e` shows the value of `e`. `#guard b` evaluates the `Bool` expression
-- `b` and reports an error if it is `false`, like `assert` in other languages.
-- Uncomment each line once the function is defined.

#guard map' (fun x => x * 2) [1, 2, 3, 4] == [2, 4, 6, 8]
#guard filter' (fun x => x > 2) [1, 2, 3, 4] == [3, 4]
#guard foldr' (fun x acc => x + acc) 0 [1, 2, 3, 4] == 10
#guard inc [1, 2, 3] == [2, 3, 4]
#guard incRec [1, 2, 3] == [2, 3, 4]
#guard evenList [1, 2, 3, 4] == [2, 4]
#guard evenListRec [1, 2, 3, 4] == [2, 4]
#guard shortStrs [1, 10, 100, 1000, -1, -10] == ["1", "10", "-1"]
#guard shortStrsRec [1, 10, 100, 1000, -1, -10] == ["1", "10", "-1"]
#guard and' [true, true, true] == true
#guard and' [true, false, true] == false
#guard andRec [true, false, true] == false
#guard or' [false, false, false] == false
#guard or' [false, true, false] == true
#guard orRec [false, true, false] == true
#guard all' (fun x => x < 10) [1, 20, 3] == false
#guard allRec (fun x => x < 10) [1, 20, 3]  == false
#guard any' (fun x => x < 10) [1, 20, 3] == true
#guard anyRec (fun x => x < 10) [1, 20, 3]  == true
#guard length' [10, 20, 30] == 3
#guard lengthRec [10, 20, 30] == 3
#guard idMap [1, 2, 3] == [1, 2, 3]
#guard idFilter [1, 2, 3] == [1, 2, 3]
#guard idFold [1, 2, 3] == [1, 2, 3]
#guard mapFold (fun x => x * 2) [1, 2, 3, 4] == [2, 4, 6, 8]
#guard filterFold (fun x => x > 2) [1, 2, 3, 4] == [3, 4]
#guard negV3 ⟨2, -4, 8⟩ == ⟨-2, 4, -8⟩
#guard addV3 ⟨1, 2, 3⟩ ⟨10, 20, 30⟩ == ⟨11, 22, 33⟩
#guard subV3 ⟨1, 2, 3⟩ ⟨10, 20, 30⟩ == ⟨-9, -18, -27⟩
#guard mulV3 ⟨1, 2, 3⟩ ⟨10, 20, 30⟩ == ⟨10, 40, 90⟩
#guard divV3 ⟨10, 20, 30⟩ ⟨3, 4, 7⟩ == ⟨3, 5, 4⟩
#guard emptyBoard 2 == [[E, E], [E, E]]
#guard isFull exampleBoard == false
#guard isFull [[X, O], [O, X]] == true
#guard showBoard exampleBoard == "X O _\nX O _\nX _ _"
#guard mapAtM 1 (fun x => if x > 1 then some (x * 100) else none) [1, 2, 3, 4] == some [1, 200, 3, 4]
#guard mapAtM 0 (fun x => if x > 1 then some (x * 100) else none) [1, 2, 3, 4] == none
#guard setToken (1, 0) X (emptyBoard 3) == some [[E, X, E], [E, E, E], [E, E, E]]
#guard setToken (1, 0) O [[E, X, E], [E, E, E], [E, E, E]] == none
#guard setToken (55, 32) X (emptyBoard 3) == none
#guard winner (emptyBoard 3) == E
#guard winner exampleBoard == X
#guard winner [[X, X, X], [E, E, E], [O, O, E]] == X
#guard winner [[O, E, E], [E, O, E], [X, X, O]] == O

-- Graphical interface ----------------------------------------------------------
-- You do not need to understand the code below. Once your functions work, put
-- the cursor on the `#widget` line at the end of this file. The infoview then
-- shows a board, and a click on a cell places the token of the current player.

section GUI
open Lean Server

def tokenToString : Token → String
  | X => "X"
  | O => "O"
  | E => ""

def tokenOfString : String → Token
  | "X" => X
  | "O" => O
  | _ => E

def encodeBoard (b : Board) : List (List String) :=
  b.map (fun row => row.map tokenToString)

def decodeBoard (rows : List (List String)) : Board :=
  rows.map (fun row => row.map tokenOfString)

structure GameState where
  board : List (List String)
  player : String
  status : String
  over : Bool
  deriving ToJson, FromJson

structure NewGameParams where
  size : Nat
  deriving ToJson, FromJson

structure MoveParams where
  board : List (List String)
  player : String
  row : Nat
  col : Nat
  deriving ToJson, FromJson

def gameState (b : Board) (player : Token) : GameState :=
  let board := encodeBoard b
  match winner b with
  | X => ⟨board, "X", "X wins!", true⟩
  | O => ⟨board, "O", "O wins!", true⟩
  | E =>
    if isFull b then ⟨board, tokenToString player, "Draw.", true⟩
    else ⟨board, tokenToString player, s!"{tokenToString player} to move", false⟩

@[server_rpc_method]
def ticTacToeNew (p : NewGameParams) : RequestM (RequestTask GameState) :=
  RequestM.pureTask (pure (gameState (emptyBoard p.size) X))

@[server_rpc_method]
def ticTacToeMove (p : MoveParams) : RequestM (RequestTask GameState) :=
  RequestM.pureTask do
    let player := tokenOfString p.player
    let next := if player == X then O else X
    match setToken (p.col, p.row) player (decodeBoard p.board) with
    | some b => pure (gameState b next)
    | none => pure { gameState (decodeBoard p.board) player with
                     status := "Invalid move, try again." }

@[widget_module]
def ticTacToeWidget : Widget.Module where
  javascript := r#"
import * as React from 'react'
import { useRpcSession } from '@leanprover/infoview'
const e = React.createElement

export default function TicTacToe(props) {
  const rs = useRpcSession()
  const [size, setSize] = React.useState(props.size ?? 3)
  const [game, setGame] = React.useState(null)
  const [error, setError] = React.useState(null)

  const run = (method, params) =>
    rs.call(method, params)
      .then(g => { setGame(g); setError(null) })
      .catch(err => setError(err?.message ?? String(err)))

  const newGame = () => run('Sheet02.ticTacToeNew', { size })
  React.useEffect(() => { newGame() }, [size])

  const move = (row, col) => {
    if (!game || game.over) return
    run('Sheet02.ticTacToeMove', { board: game.board, player: game.player, row, col })
  }

  const colors = { X: '#e5534b', O: '#539bf5' }
  const cell = (t, row, col) => e('button', {
    key: col,
    onClick: () => move(row, col),
    style: {
      width: '3.5rem', height: '3.5rem', margin: '2px', fontSize: '2rem',
      fontWeight: 'bold', cursor: game?.over ? 'default' : 'pointer',
      color: colors[t] ?? 'inherit',
      background: 'var(--vscode-editor-background)',
      border: '1px solid var(--vscode-editorWidget-border, #888)', borderRadius: '6px'
    }
  }, t)

  const board = game && e('div', { style: { margin: '0.5rem 0' } },
    game.board.map((cells, row) =>
      e('div', { key: row, style: { display: 'flex' } },
        cells.map((t, col) => cell(t, row, col)))))

  const controls = e('div', { style: { display: 'flex', gap: '0.75rem', alignItems: 'center' } },
    e('button', { onClick: newGame }, 'New game'),
    e('label', { style: { display: 'flex', gap: '0.5rem', alignItems: 'center' } },
      'Size',
      e('input', {
        type: 'range', min: 2, max: 9, value: size,
        onChange: ev => setSize(Number(ev.target.value))
      }),
      `${size} × ${size}`))

  return e('div', { style: { fontFamily: 'var(--vscode-font-family)' } },
    e('div', { style: { fontWeight: 'bold', margin: '0.25rem 0' } },
      error ? 'Your functions are not finished yet.' : (game?.status ?? '')),
    error && e('pre', { style: { whiteSpace: 'pre-wrap', fontSize: '0.8rem' } }, error),
    board,
    controls)
}
"#

#widget ticTacToeWidget with Json.mkObj [("size", 3)]

end GUI

end Sheet02
