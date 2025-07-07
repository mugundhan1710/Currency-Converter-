import tkinter as tk
import requests
def convert():
    try:
        amount = float(entry_amount.get())
        from_currency = entry_from.get().upper()
        to_currency = entry_to.get().upper()
        
        url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"
        response = requests.get(url)
        data = response.json()

        if "rates" in data and to_currency in data["rates"]:
            result = data["rates"][to_currency]
            label_result.config(text=f"{from_currency} {amount} = {result} {to_currency}")
        else:
            label_result.config(text="Invalid currency code.")
    except Exception as e:
        label_result.config(text=f"Error: {e}")

root = tk.Tk()
root.title("CURRENCY CONVERTER")

tk.Label(root, text="Amount", font=("Comic Sans MS", 14)).pack(pady=5)
entry_amount = tk.Entry(root)
entry_amount.pack()

tk.Label(root, text="From (e.g. USD, EUR)", font=("Comic Sans MS", 13)).pack(pady=5)
entry_from = tk.Entry(root)
entry_from.pack()

tk.Label(root, text="To (e.g. INR)", font=("Comic Sans MS", 13)).pack(pady=5)
entry_to = tk.Entry(root)
entry_to.pack()

tk.Button(root, text="Convert", command=convert).pack(pady=10)
label_result = tk.Label(root, text="", font=("Comic Sans MS", 12))
label_result.pack()

root.mainloop()
