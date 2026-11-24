import tkinter as tk

window = tk.Tk()
window.title("Primitive Paint")
window.geometry("900x900")

color = "black"

area = tk.Canvas(
    window,
    bg="#FCF7F0",
    width=800,
    height=800,
)

area.pack(pady=50)

def draw(event):
    x = event.x
    y = event.y

    area.create_oval(x-3, y-3, x+3, y+3, fill=color, outline=color)

def erase(event):
    x = event.x
    y = event.y
    area.create_oval(x-8, y-8, x+8, y+8, fill="#FCF7F0", outline="#FCF7F0")

def black():
    global color
    color = "black"

def red():
    global color
    color = "red"

def blue():
    global color
    color = "blue"

def green():
    global color
    color = "green"

def yellow():
    global color
    color = "yellow"

def wipe():
    area.delete("all")

bttn_row = tk.Frame(window)

bttn_row.place(y=15, x=350)

tk.Button(bttn_row, text="Blk", command=black).pack(side="left", padx=10)
tk.Button(bttn_row, text = "Blu", command=blue).pack(side="left", padx=10)
tk.Button(bttn_row, text = "Red", command=red).pack(side="left", padx=10)
tk.Button(bttn_row, text = "Grn", command=green).pack(side="left", padx=10)
tk.Button(bttn_row, text = "Ylw", command=yellow).pack(side="left",padx=10)


tk.Button(window, text="Wipe Canvas", command=wipe).place(x=425, y=850)

area.bind("<B1-Motion>", draw)
area.bind("<B3-Motion>", erase)

window.mainloop()