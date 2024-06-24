import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk

tile_types = {
            "Wall": "orange",
            "Floor": "black",
            "Spawn": "blue",
        }

color_codes = {
    "black": "0",
    "orange": "1",
    "blue": "2",
}


class Map:
    def __init__(self, canvas, width=None, height=None, file_path=None):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.file_path = file_path
        self.tiles = []
        self.load()

    def load(self):
        if self.file_path:
            with open(self.file_path, "r") as file:
                lines = file.readlines()
                self.width, self.height = map(int, lines[0].strip().split(","))
                for i, line in enumerate(lines[1:]):
                    for j, code in enumerate(line.strip().split()):
                        color = None
                        for key, value in color_codes.items():
                            if value == code:
                                color = key
                                break
                        if color is None:
                            messagebox.showerror("Error", f"Invalid code: {code}")
                            return
                        self.create_tile(j * 20, i * 20, color)

        elif self.width and self.height:
            for x in range(0, self.width * 20, 20):
                for y in range(0, self.height * 20, 20):
                    self.create_tile(x, y, "white")

    def save(self, file_path):
        with open(file_path, "w") as file:
            file.write(f"{self.width},{self.height}\n")
            for i in range(self.width):
                for j in range(self.height):
                    tile = self.get_tile_at(i * 20, j * 20)
                    color = self.get_tile_color(tile)
                    # print(color)
                    try:
                        code = color_codes[color]
                    except KeyError:
                        messagebox.showerror("Error", f"Invalid color: {color}")
                        return
                    file.write(f"{code} ")
                file.write("\n")

    def create_tile(self, x, y, color):
        tile = self.canvas.create_rectangle(x, y, x + 20, y + 20, fill=color)
        self.tiles.append(tile)

    def delete_tile(self, tile):
        self.canvas.delete(tile)

    def move_tile(self, tile, x, y):
        self.canvas.coords(tile, x, y, x + 20, y + 20)

    def change_color(self, tile, color):
        self.canvas.itemconfig(tile, fill=color)

    def get_tile_color(self, tile):
        return self.canvas.itemcget(tile, "fill")

    def get_tile_coords(self, tile):
        return self.canvas.coords(tile)

    def get_tile_at(self, x, y):
        for tile in self.tiles:
            x1, y1, x2, y2 = self.canvas.coords(tile)
            if x1 <= x < x2 and y1 <= y < y2:
                return tile
        return None

    def get_tile_color_at(self, x, y):
        tile = self.get_tile_at(x, y)
        if tile:
            return self.canvas.itemcget(tile, "fill")
        return None

    def get_tile_coords_at(self, x, y):
        tile = self.get_tile_at(x, y)
        if tile:
            return self.canvas.coords(tile)
        return None

    def get_tile_center(self, tile):
        x1, y1, x2, y2 = self.canvas.coords(tile)
        return (x1 + x2) // 2, (y1 + y2) // 2


class MapBuilderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Map Builder")
        self.master.geometry("1000x600")
        self.master.resizable(False, False)

        self.canvas = tk.Canvas(self.master, width=800, height=600, bg="white")
        self.canvas.grid(row=0, column=0)

        self.controls = ttk.Frame(self.master)
        self.controls.grid(row=0, column=1)

        self.tile_types_frame = ttk.LabelFrame(self.controls, text="Tile Types")
        self.tile_types_frame.grid(row=0, column=0)

        for i, (tile_type, color) in enumerate(tile_types.items()):
            tile_frame = ttk.Frame(self.tile_types_frame)

            ttk.Button(tile_frame, text=tile_type, command=lambda color=color: self.set_color(color)).grid(row=0, column=0)
            tk.Frame(tile_frame, width=20, height=20, relief="solid", borderwidth=1, bg=color).grid(row=0, column=1)

            tile_frame.grid(row=i, column=0)

        self.fill_map_button = ttk.Button(self.controls, text="Fill Map", command=self.fill_map)
        self.fill_map_button.grid(row=1, column=0)

        self.menu = tk.Menu(self.master)
        self.master.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_map)
        self.file_menu.add_command(label="Open", command=self.open_map)
        self.file_menu.add_command(label="Save", command=self.save_map)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.master.quit)

        self.size_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Size", menu=self.size_menu)
        self.size_menu.add_command(label="10x10", command=lambda: self.set_size(10, 10))
        self.size_menu.add_command(label="20x20", command=lambda: self.set_size(20, 20))
        self.size_menu.add_command(label="30x30", command=lambda: self.set_size(30, 30))
        self.size_menu.add_command(label="40x40", command=lambda: self.set_size(40, 40))
        self.size_menu.add_command(label="50x50", command=lambda: self.set_size(50, 50))
        self.size_menu.add_command(label="custom", command=self.ask_custom_size)

        self.map_size = None
        self.current_color = "black"
        self.map = None

        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_click)  # Bind the drag event to on_click method

    def on_click(self, event):
        if self.map is not None:
            x, y = event.x, event.y
            tile = self.map.get_tile_at(x, y)
            if tile:
                current_color = self.map.get_tile_color(tile)
                if current_color != self.current_color:
                    self.map.change_color(tile, self.current_color)
            else:
                pass

    def fill_map(self):
        if self.map is None:
            messagebox.showerror("Error", "No map to fill")
        else:
            for tile in self.map.tiles:
                self.map.change_color(tile, self.current_color)

    def set_color(self, color):
        self.current_color = color

    def set_size(self, width, height):
        self.map_size = (width, height)
        self.new_map(width, height)

    def ask_custom_size(self):
        dialog = tk.Toplevel(self.master)
        dialog.title("Custom Size")
        dialog.geometry("200x100")
        dialog.resizable(False, False)

        width_label = ttk.Label(dialog, text="Width:")
        width_label.pack()
        width_entry = ttk.Entry(dialog)
        width_entry.pack()

        height_label = ttk.Label(dialog, text="Height:")
        height_label.pack()
        height_entry = ttk.Entry(dialog)
        height_entry.pack()

        ok_button = ttk.Button(dialog, text="OK", command=lambda: self.set_custom_size(dialog, width_entry, height_entry))
        ok_button.pack()

    def set_custom_size(self, dialog, width_entry, height_entry):
        width = int(width_entry.get())
        height = int(height_entry.get())
        self.map_size = (width, height)
        self.new_map(width, height)
        dialog.destroy()

    def new_map(self, width, height):
        self.map = Map(self.canvas, width, height)

    def open_map(self):
        file_path = filedialog.askopenfilename(filetypes=[("text files", "*.txt")])
        if file_path:
            self.map = Map(self.canvas, file_path=file_path)

    def save_map(self):
        if self.map is None:
            messagebox.showerror("Error", "No map to save")
        else:
            file_path = filedialog.asksaveasfilename()
            if file_path:
                file_path = file_path if file_path.endswith(".txt") else file_path + ".txt"
                self.map.save(file_path)


if __name__ == "__main__":
    root = tk.Tk()
    app = MapBuilderApp(root)
    root.mainloop()
