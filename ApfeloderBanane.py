import tkinter as tk
from tkinter import filedialog
import os

def bild_auswaehlen():
    datei = filedialog.askopenfilename(
        title="Bild auswählen",
        filetypes=[("Bilder", "*.jpg *.png *.jpeg")]
    )

    if not datei:
        return

    name = os.path.basename(datei).lower()

    if "apfel" in name:
        ergebnis_label.config(text="🍎 Das ist ein Apfel!")
    elif "banane" in name:
        ergebnis_label.config(text="🍌 Das ist eine Banane!")
    else:
        ergebnis_label.config(text="❓ Unbekanntes Obst")

# Fenster
root = tk.Tk()
root.title("Apfel oder Banane?")
root.geometry("400x300")
root.configure(bg="#ff69b4")  # pink 💗

# Titel
titel = tk.Label(
    root,
    text="Apfel 🍎 oder Banane 🍌",
    bg="#ff69b4",
    fg="white",
    font=("Arial", 18, "bold")
)
titel.pack(pady=20)

# Button
button = tk.Button(
    root,
    text="Bild auswählen",
    command=bild_auswaehlen,
    font=("Arial", 12)
)
button.pack(pady=20)

# Ergebnis
ergebnis_label = tk.Label(
    root,
    text="Noch kein Bild ausgewählt",
    bg="#ff69b4",
    fg="white",
    font=("Arial", 14)
)
ergebnis_label.pack(pady=20)

root.mainloop()
