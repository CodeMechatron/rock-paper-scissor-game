import random
import tkinter as tk
from tkinter import font as tkfont

# ------------------- ORIGINAL GAME LOGIC (unchanged) -------------------
choices = ['paper', "rock", 'scissors']

winner = lambda user, comp: (
    'DRAW' if user == comp else
    'You Win' if (user == 'scissors' and comp == "paper") or
                 (user == 'paper' and comp == "rock") or
                 (user == 'rock' and comp == "scissors")
    else "Computer Wins"
)
# -------------------------------------------------------------------------

EMOJI = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}

BG = "#0f0f1a"
CARD = "#1a1a2e"
ACCENT = "#7c3aed"
ACCENT2 = "#22d3ee"
WIN_COLOR = "#22c55e"
LOSE_COLOR = "#ef4444"
DRAW_COLOR = "#eab308"
TEXT = "#f4f4f5"
SUBTEXT = "#a1a1aa"


class RPSApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rock · Paper · Scissors")
        self.geometry("480x640")
        self.configure(bg=BG)
        self.resizable(False, False)

        self.score_user = 0
        self.score_comp = 0

        self.title_font = tkfont.Font(family="Segoe UI", size=26, weight="bold")
        self.big_emoji_font = tkfont.Font(family="Segoe UI Emoji", size=54)
        self.label_font = tkfont.Font(family="Segoe UI", size=11)
        self.result_font = tkfont.Font(family="Segoe UI", size=20, weight="bold")
        self.score_font = tkfont.Font(family="Segoe UI", size=13, weight="bold")
        self.btn_font = tkfont.Font(family="Segoe UI Emoji", size=22)

        self._build_ui()

    # ---------------- UI construction ----------------
    def _build_ui(self):
        header = tk.Frame(self, bg=BG)
        header.pack(pady=(28, 6))
        tk.Label(header, text="ROCK · PAPER · SCISSORS", font=self.title_font,
                  bg=BG, fg=TEXT).pack()
        tk.Label(header, text="Pick your move below", font=self.label_font,
                  bg=BG, fg=SUBTEXT).pack(pady=(4, 0))

        # Score bar
        score_frame = tk.Frame(self, bg=BG)
        score_frame.pack(pady=10)
        self.score_label = tk.Label(
            score_frame,
            text=f"You  {self.score_user}   —   {self.score_comp}  Computer",
            font=self.score_font, bg=BG, fg=ACCENT2
        )
        self.score_label.pack()

        # Battle card
        card = tk.Frame(self, bg=CARD, highlightbackground=ACCENT,
                         highlightthickness=2)
        card.pack(pady=18, padx=30, fill="x")

        vs_row = tk.Frame(card, bg=CARD)
        vs_row.pack(pady=24)

        user_col = tk.Frame(vs_row, bg=CARD)
        user_col.grid(row=0, column=0, padx=20)
        tk.Label(user_col, text="YOU", font=self.label_font, bg=CARD,
                  fg=SUBTEXT).pack()
        self.user_emoji = tk.Label(user_col, text="❔", font=self.big_emoji_font,
                                    bg=CARD, fg=TEXT)
        self.user_emoji.pack()

        tk.Label(vs_row, text="VS", font=self.score_font, bg=CARD,
                  fg=ACCENT).grid(row=0, column=1, padx=10)

        comp_col = tk.Frame(vs_row, bg=CARD)
        comp_col.grid(row=0, column=2, padx=20)
        tk.Label(comp_col, text="COMPUTER", font=self.label_font, bg=CARD,
                  fg=SUBTEXT).pack()
        self.comp_emoji = tk.Label(comp_col, text="❔", font=self.big_emoji_font,
                                    bg=CARD, fg=TEXT)
        self.comp_emoji.pack()

        self.result_label = tk.Label(card, text="Make your move!",
                                      font=self.result_font, bg=CARD, fg=TEXT)
        self.result_label.pack(pady=(0, 24))

        # Choice buttons
        btn_frame = tk.Frame(self, bg=BG)
        btn_frame.pack(pady=20)

        for choice in choices:
            btn = tk.Button(
                btn_frame, text=EMOJI[choice], font=self.btn_font,
                width=4, height=2, bg=ACCENT, fg="white",
                activebackground=ACCENT2, relief="flat", cursor="hand2",
                command=lambda c=choice: self.play(c)
            )
            btn.grid(row=0, column=choices.index(choice), padx=10)
            label = tk.Label(btn_frame, text=choice.capitalize(),
                              font=self.label_font, bg=BG, fg=SUBTEXT)
            label.grid(row=1, column=choices.index(choice), pady=(6, 0))

        # Reset
        reset_btn = tk.Button(self, text="Reset Score", font=self.label_font,
                               bg=BG, fg=SUBTEXT, relief="flat",
                               cursor="hand2", command=self.reset_score)
        reset_btn.pack(pady=10)

    # ---------------- Game flow ----------------
    def play(self, user_choice):
        comp_choice = random.choice(choices)
        result = winner(user_choice, comp_choice)

        self.user_emoji.config(text=EMOJI[user_choice])
        self.comp_emoji.config(text=EMOJI[comp_choice])

        if result == "You Win":
            self.score_user += 1
            color = WIN_COLOR
            text = "🎉 You Win!"
        elif result == "Computer Wins":
            self.score_comp += 1
            color = LOSE_COLOR
            text = "💻 Computer Wins!"
        else:
            color = DRAW_COLOR
            text = "🤝 Draw!"

        self.result_label.config(text=text, fg=color)
        self.score_label.config(
            text=f"You  {self.score_user}   —   {self.score_comp}  Computer"
        )

    def reset_score(self):
        self.score_user = 0
        self.score_comp = 0
        self.score_label.config(
            text=f"You  {self.score_user}   —   {self.score_comp}  Computer"
        )
        self.result_label.config(text="Make your move!", fg=TEXT)
        self.user_emoji.config(text="❔")
        self.comp_emoji.config(text="❔")


if __name__ == "__main__":
    app = RPSApp()
    app.mainloop()