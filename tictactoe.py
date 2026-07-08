import tkinter as tk


def set_tile(row, col):
    global curr_player

    if (game_over):
        return

    if board[row][col]["text"] != "":
        return

    board[row][col]["text"] = curr_player

    if curr_player == playerO:
        curr_player = playerX
    else:
        curr_player = playerO

    label["text"] = curr_player+"'s turn"
    
    #check for winner
    check_winner()

def on_spacebar(event):
    global highlighted_row, highlighted_col
    if game_over:
        new_game()
    else:
        set_tile(highlighted_row, highlighted_col)

def highlight_next():
    global highlighted_row, highlighted_col
    
    # Don't update highlights if game is over
    if game_over:
        window.after(1000, highlight_next)
        return
    
    # Move to next position
    highlighted_col += 1
    if highlighted_col >= 3:
        highlighted_col = 0
        highlighted_row += 1
        if highlighted_row >= 3:
            highlighted_row = 0
    
    # Skip occupied squares
    while board[highlighted_row][highlighted_col]["text"] != "":
        highlighted_col += 1
        if highlighted_col >= 3:
            highlighted_col = 0
            highlighted_row += 1
            if highlighted_row >= 3:
                highlighted_row = 0
    
    # Update all button highlights
    for row in range(3):
        for col in range(3):
            if row == highlighted_row and col == highlighted_col:
                board[row][col].config(background=color_red)
            else:
                if board[row][col]["text"] == "":
                    board[row][col].config(background=color_gray)
                else:
                    board[row][col].config(background=color_dark_gray)
    
    # Schedule next highlight
    window.after(1000, highlight_next)

def check_winner():
    global turns, game_over
    turns += 1

    # horizontal win 
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
            and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"]+" is the winner!", foreground=color_yellow)
            for col in range(3):
                board[row][col].config(foreground=color_yellow, background=color_light_gray)
            game_over = True
            return
    
    #vertical win
    for col in range(3):
        if (board[0][col]["text"] == board[1][col]["text"] == board[2][col]["text"]
            and board[0][col]["text"] != ""):
            label.config(text=board[0][col]["text"]+" is the winner!", foreground=color_yellow)
            for row in range(3):
                board[row][col].config(foreground=color_yellow, background=color_light_gray)
            game_over = True
            return
    
    #diagonal win
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
        and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"]+" is the winner!", foreground=color_yellow)
        for i in range(3):
            board[i][i].config(foreground=color_yellow, background=color_light_gray)
        game_over = True
        return

    #anti-diagonal win
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
        and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"]+" is the winner!", foreground=color_yellow)
        board[0][2].config(foreground=color_yellow, background=color_light_gray)
        board[1][1].config(foreground=color_yellow, background=color_light_gray)
        board[2][0].config(foreground=color_yellow, background=color_light_gray)
        game_over = True
        return

    #tie
    if turns == 9:
        label.config(text="It's a tie!", foreground=color_yellow)
        game_over = True
        return
    
def new_game():
    global turns, game_over, highlighted_row, highlighted_col

    turns = 0
    game_over = False
    highlighted_row = 0
    highlighted_col = 0

    label.config(text=curr_player+"'s turn", foreground="white")

    for row in range(3):
        for col in range(3):
            if row == 0 and col == 0:
                board[row][col].config(text="", foreground=color_blue, background=color_red)
            else:
                board[row][col].config(text="", foreground=color_blue, background=color_gray)

#game setup
playerX = "X"
playerO = "O"
curr_player = playerX
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

color_blue = "#4584b6"
color_yellow = "#ffde57"
color_gray = "#343434"
color_light_gray = "#646464"
color_red = "#ff0000"
color_dark_gray = "#1a1a1a"

turns = 0
game_over = False
highlighted_row = 0
highlighted_col = 0

#window setup
window = tk.Tk() #game window 
window.title("Tic Tac Toe")
window.resizable(False, False) 

frame =tk.Frame(window)
label = tk.Label(frame, text=curr_player+"'s turn", font=("Arial", 20), background=color_gray, 
                 foreground="white")

label.grid(row=0, column=0, columnspan=3, sticky="we")

for row in range(3):
    for col in range(3):
        board[row][col] = tk.Button(frame, text="", font=("Arial", 50), 
                                    background=color_gray, foreground=color_blue, width=4, height=1)
        board[row][col].grid(row=row + 1, column=col)

#button = tk.Button(frame, text="restart", font=("Arial", 20), background=color_gray, 
#                   foreground="white", command=new_game)
#button.grid(row=4, column=0, columnspan=3, sticky="we")

frame.pack()

#bind spacebar
window.bind('<space>', on_spacebar)

#start highlighting loop
window.after(1000, highlight_next)

#widow centering
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))

#format "(w)x(h)x(x)+y"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()