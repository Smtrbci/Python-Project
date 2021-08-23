from time import strftime
from tkinter import Label, Tk

window = Tk()
window.title("Saat")
window.geometry("500x230")
window.configure(bg="light blue")
window.resizable(False, False)

clock_lable = Label(
    window, bg="black", fg="white", font=("Arial", 60, "bold"), relief="flat"
)
clock_lable.place(x=20, y=20)


def update_label():
    current_time = strftime("%H:%M:%S\n %d-%m-%Y ")
    clock_lable.configure(text=current_time)
    clock_lable.after(160, update_label)


update_label()
window.mainloop()
