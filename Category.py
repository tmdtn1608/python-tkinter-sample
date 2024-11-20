import tkinter as tk
from Const import category_list

class Category(tk.Frame):
    def __init__(self, controller):
        # controller = Kiosk Class
        super().__init__(controller)
        self.controller = controller

        tk.Label(self, text="카테고리 선택", font=("Arial", 20)).pack(pady=20)
        
        for category in category_list:
            tk.Button(
                self,
                text=category,
                command=lambda c=category: self.select_category(c)
            ).pack(pady=10)

    def select_category(self, category):
        self.controller.cart.set_category(category)
        self.controller.show_screen("Flavor")
