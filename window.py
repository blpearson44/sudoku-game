import tkinter as tk
from solve import create_puzzle, solve
HEIGHT = 800
WIDTH = 800


puzzle = []

root = tk.Tk()

root.geometry(str(HEIGHT) + 'x' + str(WIDTH))

entry_frame = tk.Frame(root, height=HEIGHT, width=WIDTH)
entry_frame.pack(side='top')

# create entries
entries = []
for row in range(9):
    r = []
    for col in range(9):
        temp = tk.Entry(entry_frame, font="Helvetica 44 bold", width=3)
        r.append(temp)
    entries.append(r)

# place entries
for row in range(9):
    for col in range(9):
        entries[row][col].grid(row=row, column=col)

check_solution = tk.Button(root, text="Check solution")
check_solution.pack(side='bottom')


# puzzle key widgets

# key_button function
def key():
    """Function only to be used by key_button"""
    global key_entry
    global puzzle
    puzzle_string = key_entry.get()

    puzzle = create_puzzle(puzzle_string)
    for row in range(9):
        for col in range(9):
            entries[row][col].delete(0, len(entries[row][col].get()))
            entries[row][col].insert(0, str(puzzle[row][col]))

key_frame = tk.Frame(root)
key_frame.pack()

key_entry = tk.Entry(key_frame)
key_entry.pack(fill='x')

key_button = tk.Button(key_frame, text="Enter Puzzle Key", command=key)
key_button.pack(side='bottom')





    








root.mainloop()
