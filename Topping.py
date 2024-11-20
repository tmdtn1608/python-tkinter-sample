import tkinter as tk
from Const import icecream_topping, screen_pay

class Topping(tk.Frame):
    def __init__(self, controller):
        super().__init__(controller)
        self.controller = controller

        # 화면 제목
        tk.Label(self, text="토핑 선택", font=("Arial", 20)).pack(pady=20)

        # 토핑 수량 입력 필드 저장
        self.topping_cnt = {}

        # 토핑 목록 생성
        for topping in icecream_topping:
            frame = tk.Frame(self)
            frame.pack(pady=5, padx=10, fill="x")

            # 토핑 이름 레이블
            tk.Label(frame, text=topping, font=("Arial", 12), width=10, anchor="w").pack(side="left", padx=5)

            # 수량 입력 Entry
            entry = tk.Entry(frame, width=5, justify="center")
            entry.insert(0, "0")  # 초기값 0
            entry.pack(side="left", padx=5)

            # 값 변경 이벤트 등록
            entry.bind("<FocusOut>", lambda event, t=topping: self.update_topping(t, event.widget))
            entry.bind("<KeyRelease>", lambda event, t=topping: self.update_topping(t, event.widget))

            # 입력 필드 저장
            self.topping_cnt[topping] = entry

        # 다음 버튼
        tk.Button(self, text="다음", command=self.confirm_toppings).pack(pady=20)

    def update_topping(self, topping, widget):
        """토핑 수량 검증 및 업데이트"""
        value = widget.get()
        try:
            value = int(value)
            if 0 <= value <= 99:  # 유효한 값
                self.topping_cnt[topping] = value
            else:  # 유효하지 않은 값은 초기화
                self.reset_topping(widget)
        except ValueError:  # 숫자가 아닌 값은 초기화
            self.reset_topping(widget)

    def reset_topping(self, widget):
        """잘못된 입력을 초기화"""
        widget.delete(0, tk.END)
        widget.insert(0, "0")

    def confirm_toppings(self):
        """토핑 정보를 장바구니에 저장하고 다음 화면으로 이동"""
        for topping, entry in self.topping_cnt.items():
            try:
                if isinstance(entry, int) and entry > 0 :
                    self.controller.cart.add_topping(topping, entry)
            except ValueError:
                pass  # 숫자가 아니면 무시
        # 결제페이지를 들어가기 앞서 가격을 계산한다.
        self.controller.cart.calculate_total()
        self.controller.show_screen(screen_pay)
