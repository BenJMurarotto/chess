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
    select_flag = False
    raised_green_square = None
    selected_piece = None

    def __init__(self, parent):
        super().__init__(parent)
        tk.Button(self, text="quit", command=parent.destroy).grid(row=1, column=0)
        self.create_board()
        self.board_square_tags = []

    def create_board(self):
        board_size = gameScreen.square_size * 8
        piece_selected = False

        canvas = tk.Canvas(self, width=board_size, height=board_size)
        canvas.grid(
            row=0, column=0, padx=(1200 - board_size) / 2, pady=(900 - board_size) / 2
        )
        for row in range(8):
            for col in range(8):
                color = "#f0d9b5" if (row + col) % 2 == 0 else "#b58863"
                tag = f"{gameScreen.row_map.get(col + 1)}{row + 1}"
                print(tag)
                canvas.create_rectangle(
                    col * gameScreen.square_size,
                    row * gameScreen.square_size,
                    (col + 1) * gameScreen.square_size,
                    (row + 1) * gameScreen.square_size,
                    fill="green",
                    tags=(tag, "greensquare"),
                    outline="",
                )
                canvas.create_rectangle(
                    col * gameScreen.square_size,
                    row * gameScreen.square_size,
                    (col + 1) * gameScreen.square_size,
                    (row + 1) * gameScreen.square_size,
                    fill=color,
                    tags=tag,
                    outline="",
                )
        self.set_pieces(canvas=canvas)
        canvas.bind("<Button-1>", self.is_selected)

    def get_coords(self, square, canvas):
        floating_points = canvas.coords(
            square
        )  # coords returns floating_points we want xy for piece obj
        print(floating_points)
        coords = (
            (floating_points[0] + floating_points[2]) / 2,
            (floating_points[1] + floating_points[3]) / 2,
        )
        return coords

    # def square_listener_two(self, event):
    # set pieces with hard coded dicts containing piece types and starting square values
    def set_pieces(self, canvas):
        white_pieces = {
            "P": ("A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2"),
            "B": ("C1", "F1"),
            "Kn": ("B1", "G1"),
            "R": ("A1", "H1"),
            "Q": ("D1",),
            "K": ("E1",),
        }
        black_pieces = {
            "P": ("A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7"),
            "B": ("C8", "F8"),
            "Kn": ("B8", "G8"),
            "R": ("A8", "H8"),
            "Q": ("D8",),
            "K": ("E8",),
        }

        for piece_type in white_pieces:
            start_squares = white_pieces[piece_type]
            for square in start_squares:
                canvas.create_text(
                    self.get_coords(square=square, canvas=canvas),
                    text=piece_type,
                    activefill="white",
                    tags=("white", piece_type, square),
                )

        for piece_type in black_pieces:
            start_squares = black_pieces[piece_type]
            for square in start_squares:
                canvas.create_text(
                    self.get_coords(square=square, canvas=canvas),
                    text=piece_type,
                    activefill="black",
                    tags=("black", piece_type, square),
                )

    def is_selected(self, event):
        canvas = event.widget
        item = canvas.find_withtag("current")[0]
        tags = canvas.gettags(item)

        if canvas.type(item) == "text":
            self.green_square_lower(canvas)
            square = tags[2]
            canvas.tag_raise(f"greensquare && {square}")
            gameScreen.raised_green_square = square
            gameScreen.select_flag = True
            gameScreen.selected_piece = (square, tags[1])
            print(tags)
        else:  ## on click we check if a piece is already selected then we move said piece to destination
            if gameScreen.select_flag:
                canvas.move(gameScreen.selected_piece)
            square = tags[0]
            print(f"{square}: empty")

        return item, square

    def move_piece(self, event):
        canvas = event.widget
        x_new_square = canvas.x() // 8
        y_new_square = canvas.y() // 8
        print(f"New square intent {x_new_square}, {y_new_square}")

    def green_square_lower(self, canvas):
        if gameScreen.select_flag:
            canvas.tag_lower(f"greensquare && {gameScreen.raised_green_square}")
