from typing import Optional
import time

type Pos   = tuple[int,int]
type Board = dict[Pos,frozenset[int]]

def read_board_from_file(filename : str) -> Board:
    with open (filename, 'r') as bfile:
        board = dict()
        empty = frozenset(range(1,10))
        row = 1
        for line in bfile:
            for col, x in zip(range(1,10), line):
                if x in "123456789":
                    board[ (row, col) ] = frozenset({int(x)})
                else:
                    board[ (row, col) ] = empty
            row += 1
        return board

def print_single(s : frozenset[int]) -> str:
    if len(s) == 1:
        return str(*s)
    else:
        return '-'

def print_board(board : Board):
    for row in range(1,10):
        line = ""
        for col in range(1,10):
            line += print_single(board[(row, col)])
        print (line)

def next_pos (p : Optional[Pos]) -> Optional[Pos]:
    match p:
        case None:
            return (1,1)
        case (px, py) if px < 9:
            return (px+1, py)
        case (px, py) if py < 9:
            return (1, py+1)
    return None

def update(b: Board, p: Pos, c: int) -> bool:
    bxy = b[ p ]
    if c in bxy:
        bxy = bxy.difference([c])
        b[ p ] = bxy
    return bool(bxy)

def propagate_x(b : Board, p : Pos, c : int) -> bool:
    (px, py) = p
    for ix in range(1,10):
        if px == ix: continue
        if not update(b, (ix, py), c): return False
    return True

def propagate_y(b : Board, p : Pos, c : int) -> bool:
    (px, py) = p
    for iy in range(1,10):
        if py == iy: continue
        if not update(b, (px, iy), c): return False
    return True

def propagate_o(b : Board, p : Pos, c : int) -> bool:
    (px, py) = p
    qx = (px - 1) // 3
    qy = (py - 1) // 3
    for ix in range(3 * qx + 1, 3 * qx + 3):
        for iy in range(3 * qy + 1, 3 * qy + 3):
            if p == (ix, iy): continue
            if not update(b, (ix, iy), c): return False
    return True

def try_from(b : Board, p : Optional[Pos] = None):
    np = next_pos(p)
    if np is None:
        print_board(b)
        return
    candidates = b[ np ]
    for c in candidates:
        next_b = b.copy()
        next_b[ np ] = frozenset({ c })
        if (propagate_x(next_b, np, c) and
            propagate_y(next_b, np, c) and
            propagate_o(next_b, np, c)):
            try_from(next_b, np)

def all_positions() -> list[Pos]:
    return [(x,y) for x in range(1,10) for y in range(1,10)]

def solve(b: Board, positions: list[Pos]):
    sorted_positions = positions.copy()
    sorted_positions.sort(key= lambda p: len(b[ p ]))
    try_again = False
    while sorted_positions:
        np = sorted_positions[0]
        if len(b[np]) == 1:
            c = next(iter(b[np])) # set(b[p]).pop()
            if not propagate_x(b, np, c): return
            if not propagate_y(b, np, c): return
            if not propagate_o(b, np, c): return
            sorted_positions = sorted_positions[1:]
            try_again = True
        elif try_again:
            sorted_positions.sort(key= lambda p: len(b[ p ]))
            try_again = False
        else: # len>1
            candidates = b[np]
            for c in candidates:
                next_b = b.copy()
                next_b[ np ] = frozenset([c])
                solve(next_b, sorted_positions)
            return
    print_board(b)


def solve_timed(b : Board):
    start_time = time.time()
    solve(b, all_positions())
    stop_time = time.time()
    print("Run time:", stop_time - start_time, "sec")

b1 = read_board_from_file("text/sudoku-wikipedia.txt") #1.588s / 0.151s / 0.007
b2 = read_board_from_file("text/sudoku-onslide.txt")
b3 = read_board_from_file("text/sudoku-20220118.txt") # 70+ / 22s / 0.5
b4 = read_board_from_file("text/sudoku-20220202.txt")
### https://sudoku.com.au/tough.aspx

solve_timed(b4)

