from tkinter import *
from tkinter import ttk

movies = {
    "Action": [
        "John Wick",
        "Avengers",
        "Mission Impossible",
        "Mad Max"
    ],
    "Comedy": [
        "3 Idiots",
        "Golmaal",
        "Dhamaal",
        "Hera Pheri"
    ],
    "Drama": [
        "The Pursuit of Happyness",
        "Forrest Gump",
        "Taare Zameen Par",
        "Dangal"
    ],
    "Sci-Fi": [
        "Interstellar",
        "Inception",
        "The Matrix",
        "Avatar"
    ]
}

def recommend():
    genre = genre_var.get()

    result_box.delete("1.0", END)

    result_box.insert(
        END,
        f"Recommended {genre} Movies:\n\n"
    )

    for movie in movies[genre]:
        result_box.insert(END, f"• {movie}\n")

root = Tk()
root.title("Movie Recommendation System")
root.geometry("600x450")

Label(
    root,
    text="Movie Recommendation System",
    font=("Arial", 18, "bold")
).pack(pady=10)

Label(
    root,
    text="Select Genre:"
).pack()

genre_var = StringVar()
genre_var.set("Action")

genres = ["Action", "Comedy", "Drama", "Sci-Fi"]

ttk.Combobox(
    root,
    textvariable=genre_var,
    values=genres,
    state="readonly"
).pack(pady=5)

Button(
    root,
    text="Get Recommendations",
    command=recommend,
    font=("Arial", 12, "bold")
).pack(pady=10)

result_box = Text(root, height=12, width=50)
result_box.pack(pady=10)

root.mainloop()