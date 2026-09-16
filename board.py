import tkinter as tk


# class app()
class startScreen:
    def __init__(self):
        root = tk.Tk()
        frm = tk.Frame(root, padx=20, pady=20)
        frm.grid()
        tk.Button(frm, anchor="ne", text="quit", command=root.destroy).grid(
            row=0, column=1
        )
        # tk.Button(frm, text="play", frame)
        tk.mainloop()
