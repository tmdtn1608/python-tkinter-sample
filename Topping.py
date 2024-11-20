import tkinter as tk

class Topping(tk.Frame):
    def __init__(self, controller):
        super().__init__(controller)
        self.controller = controller

        tk.Label(self, text="토핑 선택", font=("Arial", 20)).pack(pady=20)

        self.toppings = {}
        for topping in ["오레오", "땅콩가루", "시럽", "연유"]:
            var = tk.IntVar(value=0)
            self.toppings[topping] = var
            tk.Checkbutton(self, text=topping, variable=var).pack(anchor="w")

        tk.Button(self, text="다음", command=self.confirm_toppings).pack(pady=20)

    def confirm_toppings(self):
        for topping, var in self.toppings.items():
            count = var.get()
            if count > 0:
                self.controller.cart.add_topping(topping, count)
        self.controller.show_screen("Screen4")
