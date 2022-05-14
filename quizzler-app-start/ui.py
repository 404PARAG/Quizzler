THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas_text= self.canvas.create_text(150,125,
                                                  width=280,
                                                  text="Some texts are here",
                                                  font=("Arial", 20, "italic"),
                                                  fill=THEME_COLOR)
        self.canvas.grid(pady=20, padx=20, row=1, column=0, columnspan=2)

        self.score_label = Label(text = "Score:",fg = "white", bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)

        self.true_image_path = PhotoImage(file="images/true.png")
        self.wrong_image_path = PhotoImage(file="images/false.png")

        self.right_button = Button(image=self.true_image_path, highlightthickness=0,
                                   command=self.right_fun)
        self.right_button.grid(row=2, column=0, padx=20, pady=20)
        self.wrong_button = Button(image=self.wrong_image_path, highlightthickness=0,
                                   command= self.wrong_fun)
        self.wrong_button.grid(row=2, column=1, padx=20, pady=20)
        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text = q_text)
        else:
            self.canvas.itemconfig(self.canvas_text,text="You have reached the end of the quiz.")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def right_fun(self):
        is_right=self.quiz.check_answer("True")
        self.give_feedback(is_right)


    def wrong_fun(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)

