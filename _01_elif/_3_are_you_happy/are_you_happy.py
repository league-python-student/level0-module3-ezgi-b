from tkinter import Tk, simpledialog, messagebox


if __name__ == '__main__':
    # TODO: Look at the AreYouHappy.png image
    #       Use pop-ups to recreate the chart using if and elif statements
    window = Tk()
    window.withdraw()
    happy = simpledialog.askstring(None, "Are you happy?")
    if happy == "yes":
        messagebox.showinfo(None, "Keep doing whatever you're doing.")
    elif happy == "no":
        want = simpledialog.askstring(None, "Do you want to be happy?")
        if want == "yes":
            messagebox.showinfo(None, "Change something.")
        elif want == "no":
            messagebox.showinfo(None, "Keep doing whatever you're doing.")

    pass
