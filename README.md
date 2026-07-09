###How to Use
Just download the .exe file and run it and practice winning with only one key

# 🕹️ Tic-Tac-Toe (Space-Only Edition)

A minimalist, web-based Tic-Tac-Toe game designed specifically for the **Hack Club OneKey** hardware jam. 
The core philosophy of this project is extreme simplicity: rejecting the matrix of standard keyboard buttons and playing a classic grid game using **only a single key**.

## 🕹️ How It Works (The OneKey Mechanic)

Since you only have one button, the game uses an **automatic scanning system**:
1. Every **1 second**, a red highlight indicator moves automatically from cell to cell across the 3x3 board.
2. When the indicator lands on the cell where you want to place your mark (`X` or `O`), you press the **Spacebar** (or tap your OneKey macropad).
3. If a player wins or the game ends in a tie, pressing the **Spacebar** automatically resets the board and starts a new game.

## 💡 Why This Fits OneKey

* **Zero Mouse Input:** You don't need to click anything to play.
* **Single Key Control:** The entire game loop (navigation, placement, and restarting) is mapped exclusively to the `Space` key event.
* **Accessible Hardware Design:** Perfectly optimized for a 1-key custom macropad.

Made with ❤️ for Hack Club.
