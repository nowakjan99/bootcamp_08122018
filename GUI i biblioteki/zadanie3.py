import tkinter

def oblicz_koszt_spalania():
    try:
        cena_paliwa = int(cena_paliwa.get())
        spalanie = int(spalanie.get())
        dystans = int(dystans.get())

        wynik = cena_paliwa * dystans * spalanie * 0.01
        wynik_label.configure(text=f"Wynik: {wynik}")
    except ValueError:
        messagebox.showerror("Bledne dane", "Popraw dane - powinny być liczbami")

root = tkinter.Tk()

a_label = tkinter.Label(master=root, text="cena paliwa")
a_label.grid(row=0, column=0)
a_entry = tkinter.Entry(master=root)
a_entry.grid(row=0, column=1)

b_label = tkinter.Label(master=root, text="spalanie")
b_label.grid(row=1, column=0)
b_entry = tkinter.Entry(master=root)
b_entry.grid(row=1, column=1)

b_label = tkinter.Label(master=root, text="dystans")
b_label.grid(row=2, column=0)
b_entry = tkinter.Entry(master=root)
b_entry.grid(row=2, column=1)

button = tkinter.Button(master=root, text="Oblicz", command=oblicz_koszt_spalania)
button.grid(row=3, column=1)

wynik_label = tkinter.Label(master=root, text=" - ")
wynik_label.grid(row=4, column=1)

root.mainloop()