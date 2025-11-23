from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messagebox

tk = Tk()
tk.title("Braking Distance Calculator")
tk.geometry("512x200")
tk.resizable(False, False)


tk.columnconfigure(0, weight=0, minsize=150)  
tk.columnconfigure(1, weight=1)               


label_FSpeed = ttk.Label(tk, text="Initial speed (V₀):")
label_FSpeed.grid(row=0, column=0, padx=10, pady=10, sticky="w")
FirstSpeed_i = ttk.Entry(tk)
FirstSpeed_i.grid(row=0, column=1, padx=(0, 10), pady=10, sticky="ew")


label_LSpeed = ttk.Label(tk, text="Final speed (V):")
label_LSpeed.grid(row=1, column=0, padx=10, pady=10, sticky="w")
LastSpeed_i = ttk.Entry(tk)
LastSpeed_i.grid(row=1, column=1, padx=(0, 10), pady=10, sticky="ew")


label_acceleration = ttk.Label(tk, text="Deceleration magnitude (a > 0):")
label_acceleration.grid(row=2, column=0, padx=10, pady=10, sticky="w")
Acceleration_i = ttk.Entry(tk)
Acceleration_i.grid(row=2, column=1, padx=(0, 10), pady=10, sticky="ew")


btnForResult = ttk.Button(tk, text="Get result...", command=lambda: Result())
btnForResult.grid(row=3, column=0, columnspan=2, pady=10)


def Result():
    try:
        V0 = float(FirstSpeed_i.get())
        V = float(LastSpeed_i.get())
        a = float(Acceleration_i.get())

        if a <= 0:
            messagebox.showerror("Error", "Acceleration must be > 0 (deceleration magnitude)!")
            return
        if V0 < 0 or V < 0:
            messagebox.showerror("Error", "Speed cannot be negative!")
            return
        if V > V0:
            messagebox.showwarning("Warning", "Final speed > Initial speed - the car accelerates!")
        

        # V² = V0² - 2*a*S  →  S = (V0² - V²) / (2*a)
        S = (V0**2 - V**2) / (2 * a)

        if S < 0:
            S = 0  

        res = Toplevel(tk)
        res.title("Result")
        res.geometry("400x220")
        res.resizable(False, False)
        res.transient(tk)  
        res.grab_set()     

        ttk.Label(res, text="Data of operation:", font=("Arial", 10, "bold")).pack(anchor=W, padx=10, pady=(10, 5))
        ttk.Label(res, text=f"V₀ (initial speed): {V0} м/с").pack(anchor=W, padx=20)
        ttk.Label(res, text=f"V (final speed): {V} м/с").pack(anchor=W, padx=20)
        ttk.Label(res, text=f"a (deceleration magnitude): {a} м/с²").pack(anchor=W, padx=20)
        ttk.Label(res, text=f"Braking distance: {S:.3f} м", font=("Arial", 11, "bold"), foreground="blue").pack(anchor=W, padx=20, pady=(10, 5))

        ttk.Button(res, text="Close", command=res.destroy).pack(pady=10)

    except ValueError:
        messagebox.showerror("Error", "Will input correct nums (you can use float nums)")


tk.mainloop()
