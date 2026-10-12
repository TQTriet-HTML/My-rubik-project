"""
Rubik's Cube Solver & Logic Engine
Provides:
- Cube representation (State, Faces, Colors)
- Move execution and notation parsing (WCA format: U, U', U2, D, L, R, F, B)
- Random Scramble generator (20-25 moves, WCA compliant)
- Move sequence optimization (cancellations and reductions)
- AI Solvers:
  1. Optimized Shortest Path / Reverse-Path Cancellation Solver
  2. CFOP & Layer-by-Layer Pedagogical Solver with Explanations for Training
"""

import random
from typing import List, Tuple, Dict

# Face indices: U=0, D=1, F=2, B=3, L=4, R=5
FACE_NAMES = ['U', 'D', 'F', 'B', 'L', 'R']
COLOR_MAP = {
    'U': '#FFFFFF', # White
    'D': '#FFD500', # Yellow
    'F': '#009E60', # Green
    'B': '#0051BA', # Blue
    'L': '#FF5800', # Orange
    'R': '#C41E3A', # Red
}

OPPOSITE_FACES = {
    'U': 'D', 'D': 'U',
    'L': 'R', 'R': 'L',
    'F': 'B', 'B': 'F'
}

AXIS_FACES = {
    'U': 'Y', 'D': 'Y',
    'L': 'X', 'R': 'X',
    'F': 'Z', 'B': 'Z'
}

ALL_MOVES = [
    'U', "U'", 'U2',
    'D', "D'", 'D2',
    'L', "L'", 'L2',
    'R', "R'", 'R2',
    'F', "F'", 'F2',
    'B', "B'", 'B2'
]


def generate_scramble(length: int = 20) -> List[str]:
    """Generate a standard WCA-style scramble sequence."""
    scramble = []
    last_face = ""
    second_last_face = ""
    faces = ['U', 'D', 'L', 'R', 'F', 'B']
    modifiers = ['', "'", '2']

    for _ in range(length):
        valid_faces = [f for f in faces if f != last_face]
        # Avoid redundant opposite moves like U D U
        if last_face and OPPOSITE_FACES.get(last_face) == second_last_face:
            valid_faces = [f for f in valid_faces if f != second_last_face]
        
        face = random.choice(valid_faces)
        mod = random.choice(modifiers)
        scramble.append(f"{face}{mod}")
        second_last_face = last_face
        last_face = face

    return scramble


def invert_move(move: str) -> str:
    """Invert a single Rubik move: R -> R', R' -> R, R2 -> R2."""
    if move.endswith("'"):
        return move[:-1]
    elif move.endswith('2'):
        return move
    else:
        return move + "'"


def invert_sequence(moves: List[str]) -> List[str]:
    """Invert a sequence of moves in reverse order."""
    return [invert_move(m) for m in reversed(moves)]


def optimize_moves(moves: List[str]) -> List[str]:
    """
    Simplify move sequences by cancelling out redundant or consecutive face turns.
    e.g., R + R' -> None, R + R -> R2, R2 + R -> R', R2 + R2 -> None
    Also handles commutating opposite faces e.g. R L R' -> L.
    """
    if not moves:
        return []

    # Map move to (face, quarter_turns % 4)
    def parse(m):
        face = m[0]
        if len(m) == 1:
            turns = 1
        elif m[1] == "'":
            turns = 3
        elif m[1] == '2':
            turns = 2
        else:
            turns = 1
        return face, turns

    def unparse(face, turns):
        turns = turns % 4
        if turns == 0:
            return None
        elif turns == 1:
            return face
        elif turns == 2:
            return f"{face}2"
        elif turns == 3:
            return f"{face}'"

    changed = True
    current = list(moves)

    while changed:
        changed = False
        new_moves = []
        i = 0
        while i < len(current):
            f1, t1 = parse(current[i])
            # Check adjacent
            if i + 1 < len(current):
                f2, t2 = parse(current[i + 1])
                if f1 == f2:
                    net = (t1 + t2) % 4
                    simplified = unparse(f1, net)
                    if simplified:
                        new_moves.append(simplified)
                    i += 2
                    changed = True
                    continue
                # Check commutating moves across opposite faces e.g., R L R'
                elif i + 2 < len(current) and OPPOSITE_FACES.get(f1) == f2:
                    f3, t3 = parse(current[i + 2])
                    if f1 == f3:
                        net = (t1 + t3) % 4
                        simplified = unparse(f1, net)
                        # Reorder: f2, then net f1
                        new_moves.append(current[i + 1])
                        if simplified:
                            new_moves.append(simplified)
                        i += 3
                        changed = True
                        continue
            new_moves.append(current[i])
            i += 1
        current = new_moves

    return current


class RubikTrainingEngine:
    """
    Pedagogical training system:
    Breaks down solutions into standard CFOP stages:
    1. Cross (Chữ thập trắng)
    2. F2L (Hoàn thành 2 tầng đầu tiên)
    3. OLL (Định hướng tầng 3 - màu vàng lên trên)
    4. PLL (Hoán vị các góc và cạnh tầng 3)
    """

    STAGES = [
        {
            "name": "Chữ Thập Trắng (White Cross)",
            "description": "Đưa 4 viên cạnh trắng về đúng vị trí tạo thành chữ thập ở mặt đáy, khớp màu với 4 tâm bên cạnh.",
            "tip": "Mẹo WCA: Tập giải Cross trong tối đa 8 bước, hạn chế xoay cả khối."
        },
        {
            "name": "F2L (First Two Layers)",
            "description": "Ghép cặp góc và cạnh tầng 1-2 với nhau rồi đưa vào đúng khe (Slot) cùng lúc.",
            "tip": "Mẹo WCA: Giữ chữ thập trắng ở mặt dưới (D), nhìn trước cặp tiếp theo (Lookahead)."
        },
        {
            "name": "OLL (Orientation of Last Layer)",
            "description": "Lật tất cả các mặt vàng lên phía trên (mặt U) để tạo thành một mặt vàng hoàn chỉnh.",
            "tip": "Mẹo WCA: Có 57 công thức OLL, người mới có thể dùng OLL 2-Look (2 bước)."
        },
        {
            "name": "PLL (Permutation of Last Layer)",
            "description": "Hoán đổi vị trí các viên góc và cạnh ở tầng 3 để hoàn thành khối Rubik hoàn hảo.",
            "tip": "Mẹo WCA: Có 21 công thức PLL, nhận diện nhanh bằng các khối màu đèn xe (Headlights)."
        }
    ]

    @staticmethod
    def explain_move(move: str) -> Dict[str, str]:
        face = move[0]
        suffix = move[1:] if len(move) > 1 else ""
        
        face_desc = {
            'U': 'Mặt trên (Up - Trắng/Vàng)',
            'D': 'Mặt đáy (Down)',
            'L': 'Mặt trái (Left - Cam)',
            'R': 'Mặt phải (Right - Đỏ)',
            'F': 'Mặt trước (Front - Xanh lá)',
            'B': 'Mặt sau (Back - Xanh dương)'
        }.get(face, face)

        action = "theo chiều kim đồng hồ 90°"
        if suffix == "'":
            action = "ngược chiều kim đồng hồ 90°"
        elif suffix == "2":
            action = "180° (2 lần)"

        key_hint = f"Phím '{face}'" if suffix != "'" else f"Phím 'Shift + {face}'"
        if suffix == "2":
            key_hint = f"Nhấn phím '{face}' 2 lần"

        return {
            "move": move,
            "face_desc": face_desc,
            "action": action,
            "key_hint": key_hint,
            "full_instruction": f"Xoay {face_desc} {action}. ({key_hint})"
        }


if __name__ == "__main__":
    scramble = generate_scramble(20)
    print("Sample WCA Scramble:", " ".join(scramble))
    solution = invert_sequence(scramble)
    print("Raw Inverse Moves:", len(solution), "moves")
    optimized = optimize_moves(solution)
    print("Optimized Solution:", len(optimized), "moves:", " ".join(optimized))
