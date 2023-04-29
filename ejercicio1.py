import tkinter as tk

def count_even_numbers(start, end):
    count = 0
    for num in range(start, end+1):
        if num % 2 == 0:
            count += 1
    return count

def get_numbers():
    start = entry_start.get()
    end = entry_end.get()

    if not start.isdigit() or not end.isdigit():
        label_result.config(text="Solo ingresar números")
    else:
        start = int(start)
        end = int(end)
        count = count_even_numbers(start, end)
        label_result.config(text=f"La cantidad de números pares es {count}")

window = tk.Tk()
window.title("Contador de números pares")

label_start = tk.Label(text="numero inicial: ")
label_start.pack()
entry_start = tk.Entry()
entry_start.pack()

label_end = tk.Label(text="numero final: ")
label_end.pack()
entry_end = tk.Entry()
entry_end.pack()

button_count = tk.Button(text=" Contar números pares ", bg="#009186", command=get_numbers)
button_count.pack()

label_result = tk.Label()
label_result.pack()

window.mainloop()
