import tkinter as tk

window = tk.Tk()
window.title("Primitive Paint")
window.geometry("900x900")

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

    area.create_oval(x-3, y-3, x+3, y+3, fill="black")

area.bind("<B1-Motion>", draw)

window.mainloop()