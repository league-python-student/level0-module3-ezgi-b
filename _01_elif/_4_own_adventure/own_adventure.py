from tkinter import simpledialog, messagebox, Tk

# TODO Tell the user a story, but give them options so they can decide the
#  path of the plot.
#  Use pop-ups, if statements, and your imagination to make an interesting
#  story
if __name__ == "__main__":
    window = Tk()
    window.withdraw()
    messagebox.showinfo(None, "As you enter your room, you see a mysterious metal box with intricate carvings.")
    answer = simpledialog.askstring(None, "Do you open it? (y/n)")
    if answer == "y":
        messagebox.showinfo(None, "As you open the lid of the box, you see a sparkly gem. Then your vision goes blank. You open your eyes and see that you are standing in a grassy meadow surrounded by a circle of 10 trees.")
        answer = simpledialog.askstring(None, "Do you stay where you are and do nothing, or do you explore? (1/2)")
        if answer == "1":
            messagebox.showinfo(None, "You wait there and hope this is all a dream. You see another tree appear, so now the circle is made of 11 trees. You hear a growling voice that says 'It's nearly lunch time!'")
            answer = simpledialog.askstring(None, "Do you stay or explore (1/2)")
            if answer == "1":
                messagebox.showinfo(None, "You are too terrified to move. After some time, you see another tree appear, making the total tree count 12. A giant wolf jumps out, growls 'Lunch time,' and eats you")
            elif answer == "2":
                messagebox.showinfo(None, "You leave the meadow through a gap in the circle of trees, and encounter a humandoid creature with wings. You explain you situation, and the creature tells you that if you answer a riddle, you can leave.")
                answer = simpledialog.askstring("Riddle", "What day is two days before tomorrow?")
                if answer.lower() == "yesterday":
                    messagebox.showinfo(None, "You appear in you room. There is no box anywhere. You wonder if you have been hallucinating.")
                else:
                    messagebox.showinfo(None, "You are now stuck forever :(")
        elif answer == "2":
            messagebox.showinfo(None, "You leave the meadow through a gap in the trees. A badger with glasses pops out of the ground in front of you. It says 'answer my riddle, and you can leave.'")
            answer = simpledialog.askstring(None, "What word becomes shorter when you add two letters to it?")
            if answer.lower() == "short":
                messagebox.showinfo(None, "You appear in you room. There is no box anywhere. You wonder if you have been hallucinating.")
            else:
                messagebox.showinfo(None, "The badger eats you.")
    elif answer == "n":
        messagebox.showinfo(None, "The box disappears in a poof of smoke, and you are left, confused.")
