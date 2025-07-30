# 8-puzzle-Artificial-Intelligence-
python game importing pygame
# 🧠 8 Puzzle Problem Solver with AI (A* Search + Pygame)

This project is a graphical Python implementation of the classic **8-puzzle problem**, combining an interactive GUI (using **Pygame**) with an AI solver using **A\* (A-star) Search Algorithm**.

---

## 📌 What is the 8 Puzzle Problem?

The 8 Puzzle is a sliding puzzle consisting of a 3x3 grid with 8 numbered tiles and one empty space. The objective is to **rearrange the tiles** to match the goal state by sliding them one at a time into the empty space.

Example:

Start State Goal State

| 1 | 2 | 3 | | 1 | 2 | 3 |
| 4 | 5 | 6 | --> | 4 | 5 | 6 |
| 7 | 8 | | | 7 | 8 | |

---

## 🚀 Features

✅ **Interactive GUI** using Pygame  
✅ Manual tile movement with arrow keys  
✅ **"Solve" button** to run AI-based solution  
✅ Uses **A\* algorithm with Manhattan distance** heuristic  
✅ Shows each move with animation  
✅ Displays number of moves and victory message  

---

## 🛠️ Project Structure

8_puzzle_ai/

├── puzzle.py # Main game loop

├── game/

│ ├── button.py # Custom button class

│ ├── generate_puzzle.py # Random puzzle generator

│ ├── highlight_digit.py # Handles tile highlighting and moves

├── sol/

│ └── solution.py # A* Search Algorithm implementation

├── assets/ # (Optional) images, sounds, fonts

├── README.md # Project documentation


---
## 💡 AI Approach (A* Search Algorithm)

- **State Representation**: 2D list for board tiles  
- **Heuristic**: Manhattan Distance  
- **Goal**: Find the shortest path to reach the target configuration  
- **Open List**: Priority queue sorted by `f(n) = g(n) + h(n)`  
- **Closed List**: Stores visited states to avoid loops

---
## 🎮 How to Run

### ✅ Prerequisites:
- Python 3.10 or later (3.12 supported)
- Pygame installed

```bash
pip install pygame
```
Use:
🔼 🔽 ◀️ ▶️ keys to move the empty tile
🟨 Click "Solve" to let the AI find and show the optimal path

# 📚 Concepts Used :
Artificial Intelligence
Heuristic Search (A*)
Graph Search
Game Development using Pygame
Object-Oriented Programming in Python
