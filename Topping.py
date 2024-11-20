import tkinter as tk
from Const import icecream_topping

class Topping(tk.Frame):
    def __init__(self, controller):
        super().__init__(controller)
        self.controller = controller

        tk.Label(self, text="토핑 선택", font=("Arial", 20)).pack(pady=20)

        self.toppings = {}
        self.topping_cnt = {} # 갯수
        self.topping_check = {} # 체크상태
        
        for topping in icecream_topping:
            # 토핑 체크박스와 숫자 입력 필드를 함께 배치
            var = tk.IntVar(value=0)
            self.topping_check[topping] = var

            frame = tk.Frame(self)
            frame.pack(pady=5)

            # 체크박스
            checkbox = tk.Checkbutton(frame, text=topping, variable=var, command=lambda t=topping: self.toggle_topping(t))
            checkbox.pack(side="left")

            # 숫자 입력 필드 (기본값 0, 초기에는 비활성화)
            entry = tk.Entry(frame, width=5)
            entry.insert(0, "0")
            entry.config(state="disabled")
            entry.pack(side="left", padx=5)
            self.topping_cnt[topping] = entry


        tk.Button(self, text="다음", command=self.confirm_toppings).pack(pady=20)

    def toggle_topping(self, topping):
        entry = self.topping_cnt[topping]
        # 체크상태 확인
        if self.topping_check[topping].get() == 1:  # 체크박스가 선택된 경우
            entry.config(state="normal")  # 텍스트박스 활성화
        else:
            entry.config(state="disabled")  # 텍스트박스 비활성화
            entry.delete(0, "end")  # 텍스트박스 내용 삭제
            entry.insert(0, "0")  # 텍스트박스 초기값 0
            self.controller.cart.data["toppings"][topping] = 0  # 장바구니의 토핑 설정을 0으로 초기화


    def confirm_toppings(self):
        for topping, var in self.toppings.items():
            count = int(self.topping_cnt[topping].get())  
            if count > 0: 
                self.controller.cart.add_topping(topping, count)
        self.controller.show_screen("Pay")
