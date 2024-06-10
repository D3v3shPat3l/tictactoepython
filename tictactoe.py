import tkinter
from tkinter import simpledialog, messagebox

def set_tile(row, column):
    global curr_player

    if game_over:
        return

    if board[row][column]["text"] != "":
        return
    
    board[row][column]["text"] = curr_player

    if curr_player == playerO:
        curr_player = playerX
    else:
        curr_player = playerO
    
    label["text"] = curr_player + "'s turn"
    check_winner()

def check_winner():
    global turns, game_over, playerX_score, playerO_score
    turns += 1

    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
            and board[row][0]["text"] != ""):
            winner = board[row][0]["text"]
            label.config(text=winner + " is the winner!", foreground=colour2)
            for column in range(3):
                board[row][column].config(foreground=colour2, background=colour4)
            game_over = True
            update_scores(winner)
            return
    
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
            and board[0][column]["text"] != ""):
            winner = board[0][column]["text"]
            label.config(text=winner + " is the winner!", foreground=colour2)
            for row in range(3):
                board[row][column].config(foreground=colour2, background=colour4)
            game_over = True
            update_scores(winner)
            return
    
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
        and board[0][0]["text"] != ""):
        winner = board[0][0]["text"]
        label.config(text=winner + " is the winner!", foreground=colour2)
        for i in range(3):
            board[i][i].config(foreground=colour2, background=colour4)
        game_over = True
        update_scores(winner)
        return

    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
        and board[0][2]["text"] != ""):
        winner = board[0][2]["text"]
        label.config(text=winner + " is the winner!", foreground=colour2)
        board[0][2].config(foreground=colour2, background=colour4)
        board[1][1].config(foreground=colour2, background=colour4)
        board[2][0].config(foreground=colour2, background=colour4)
        game_over = True
        update_scores(winner)
        return
    
    if turns == 9:
        game_over = True
        label.config(text="Tie!", foreground=colour2)

def update_scores(winner):
    global playerX_score, playerO_score

    if winner == playerX:
        playerX_score += 1
    elif winner == playerO:
        playerO_score += 1
    update_highscores()

def new_game():
    global turns, game_over

    turns = 0
    game_over = False

    label.config(text=curr_player + "'s turn", foreground="white")

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=colour1, background=colour3)

def set_theme(theme):
    global colour1, colour2, colour3, colour4

    if theme == "Theme 1":
        colour1 = "#4584b6"
        colour2 = "#ffde57"
        colour3 = "#343434"
        colour4 = "#646464"
    elif theme == "Theme 2":
        colour1 = "#ff6347"
        colour2 = "#ffd700"
        colour3 = "#4b0082"
        colour4 = "#dda0dd"
    elif theme == "Theme 3":
        colour1 = "#8a2be2"
        colour2 = "#7fff00"
        colour3 = "#2f4f4f"
        colour4 = "#00ced1"
    
    label.config(background=colour3, foreground="white")
    for row in range(3):
        for column in range(3):
            board[row][column].config(foreground=colour1, background=colour3)
    button.config(background=colour3, foreground="white")

def update_highscores():
    highscore_text = f"{playerX_name}: {playerX_score}  {playerO_name}: {playerO_score}"
    highscore_label.config(text=highscore_text)

def get_player_names():
    global playerX_name, playerO_name
    playerX_name = simpledialog.askstring("Player X", "Enter the name of Player X:")
    playerO_name = simpledialog.askstring("Player O", "Enter the name of Player O:")
    if not playerX_name:
        playerX_name = "Player X"
    if not playerO_name:
        playerO_name = "Player O"
    update_highscores()

playerX = "X"
playerO = "O"
curr_player = playerX
board = [[0, 0, 0], 
         [0, 0, 0], 
         [0, 0, 0]]

colour1 = "#4584b6"
colour2 = "#ffde57"
colour3 = "#343434"
colour4 = "#646464"

turns = 0
game_over = False

playerX_score = 0
playerO_score = 0

window = tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=curr_player + "'s turn", font=("Consolas", 20), background=colour3,
                      foreground="white")
label.grid(row=0, column=0, columnspan=3, sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Consolas", 50, "bold"),
                                            background=colour3, foreground=colour1, width=4, height=1,
                                            command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row + 1, column=column)

button = tkinter.Button(frame, text="restart", font=("Consolas", 20), background=colour3,
                        foreground="white", command=new_game)
button.grid(row=4, column=0, columnspan=3, sticky="we")

frame.pack()

menu = tkinter.Menu(window)
window.config(menu=menu)

theme_menu = tkinter.Menu(menu, tearoff=0)
menu.add_cascade(label="Themes", menu=theme_menu)
theme_menu.add_command(label="Theme 1", command=lambda: set_theme("Theme 1"))
theme_menu.add_command(label="Theme 2", command=lambda: set_theme("Theme 2"))
theme_menu.add_command(label="Theme 3", command=lambda: set_theme("Theme 3"))

highscore_label = tkinter.Label(window, text="", font=("Consolas", 15), background=colour3, foreground="white")
highscore_label.pack(pady=10)

get_player_names()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()
