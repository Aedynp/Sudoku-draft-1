import tkinter as tk

root = tk.Tk()

# Create the puzzle
puzzle = tk.Frame(root, bg='white')
puzzle.pack()



        

class new_game():
    btn_cells = [[None for x in range(9)] for x in range(9)]
    def colour_change():
        btn_cells = [[None for x in range(9)] for x in range(9)]
        btn_cells[1][1] = tk.Button( relief='ridge', bg='blue')
        print("hi")

    blocks = [] 
    for r in range(3):  # r is for rowsd
        row = []
        for c in range(3):  # c is for column
            frame = tk.Frame(puzzle, bd=1, highlightbackground='light blue',
                                    highlightcolor='light blue', highlightthickness=1)
            frame.grid(row=r, column=c, sticky='nsew')
            row.append(frame)
        blocks.append(row)

    # creates the 9 x 9 grid which fits into the 3 x 3 grid
   
    for i in range(9):
        for j in range(9):
            # creates a i and j row and column format
            # creates a frame for the grid to fit into
            frm_cell = tk.Frame(blocks[i // 3][j // 3])
            frm_cell.grid(row=(i % 3), column=(j % 3), sticky='nsew')
            frm_cell.rowconfigure(0, minsize=50, weight=1)
            frm_cell.columnconfigure(0, minsize=50, weight=1)
            var = tk.StringVar()
            btn_cells[i][j] = tk.Button(frm_cell, relief='ridge', bg='white', command = colour_change())
            btn_cells[i][j].grid(sticky='nsew')
    


# creates a larger 3 x 3 grid for the 9 x 9 grid to fit into

        
root.mainloop()