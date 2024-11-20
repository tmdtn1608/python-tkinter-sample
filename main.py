import tkinter as tk
from Category import Category
from Flavor import Flavor
from Topping import Topping
from Pay import Pay
from Cart import Cart

class Kiosk(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("키오스크")
        self.geometry("400x300")
        
        # 장바구니 인스턴스 생성
        self.cart = Cart()
        
        # 화면 관리
        self.screens = {}
        self.current_screen = None
        
        # 화면 추가
        self.add_screen("Category", Category)
        self.add_screen("Flavor", Flavor)
        self.add_screen("Topping", Topping)
        self.add_screen("Pay", Pay)
        
        # 초기 화면 표시
        self.show_screen("Category")
    
    def add_screen(self, name, screen_class):
        """새 화면 추가"""
        screen = screen_class(self)
        self.screens[name] = screen
    
    def show_screen(self, name):
        """화면 전환"""
        if self.current_screen:
            self.current_screen.pack_forget()
        screen = self.screens.get(name)
        if screen:
            self.current_screen = screen
            self.current_screen.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = Kiosk()
    app.mainloop()
