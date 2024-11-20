import tkinter as tk

class Flavor(tk.Frame):
    def __init__(self, controller):
        super().__init__(controller)
        self.controller = controller

        tk.Label(self, text="맛 선택", font=("Arial", 20)).pack(pady=20)
        
        for flavor in ["초코", "베리", "두부", "흑임자"]:
            tk.Button(
                self,
                text=flavor,
                command=lambda f=flavor: self.select_flavor(f)
            ).pack(pady=10)

    def select_flavor(self, flavor):
        self.controller.cart.set_flavor(flavor)
        self.controller.show_screen("Screen3")
