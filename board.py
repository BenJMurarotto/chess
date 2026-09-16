import tkinter as tk


class app(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chess")
        self.geometry("1200x900")

        self.frames = {}
        for F in (startScreen, gameScreen):
            frame = F(self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(startScreen)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class startScreen(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Button(self, anchor="ne", text="quit", command=parent.destroy).grid(
            row=1, column=1
        )
        tk.Button(
            self, text="play", command=lambda: parent.show_frame(gameScreen)
        ).grid(row=0, column=0)


class gameScreen(tk.Frame):
    square_size = 80
    row_map = {1: "H", 2: "G", 3: "F", 4: "E", 5: "D", 6: "C", 7: "B", 8: "A"}

    def __init__(self, parent):
        super().__init__(parent)
        tk.Button(self, text="quit", command=parent.destroy).grid(row=1, column=0)
        self.create_board()
        self.board_square_tags = []

    def create_board(self):
        board_size = gameScreen.square_size * 8

        canvas = tk.Canvas(self, width=board_size, height=board_size)
        canvas.grid(
            row=0, column=0, padx=(1200 - board_size) / 2, pady=(900 - board_size) / 2
        )
        for row in range(8):
            for col in range(8):
                color = "#f0d9b5" if (row + col) % 2 == 0 else "#b58863"
                tag = f"{gameScreen.row_map.get(row + 1)}{col + 1}"
                print(tag)
                canvas.create_rectangle(
                    col * gameScreen.square_size,
                    row * gameScreen.square_size,
                    (col + 1) * gameScreen.square_size,
                    (row + 1) * gameScreen.square_size,
                    fill=color,
                    tags=tag,
                    outline="",
                )

        canvas.bind("<Button-1>", self.square_listener)
        canvas.bindtags(
            self.board_square_tags,
        )

    def square_listener(self, event):
        col = event.x // gameScreen.square_size
        row = event.y // gameScreen.square_size

        return print(f"Square clicked: {gameScreen.row_map.get(row + 1)}{col + 1}")

    def square_listener_two(self, event):
        event
