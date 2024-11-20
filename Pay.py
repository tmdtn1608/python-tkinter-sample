import tkinter as tk
import json

class Pay(tk.Frame):
    def __init__(self, controller):
        super().__init__(controller)
        self.controller = controller

        tk.Label(self, text="결제 정보 입력", font=("Arial", 20)).pack(pady=20)

        # 카드 번호
        tk.Label(self, text="카드 번호 입력").pack(pady=5)
        self.card_number = tk.Entry(self)
        self.card_number.pack(pady=5)

        # 카드 비밀번호
        tk.Label(self, text="카드 비밀번호 입력").pack(pady=5)
        self.card_password = tk.Entry(self, show="*")
        self.card_password.pack(pady=5)

        tk.Button(self, text="결제 완료", command=self.complete_payment).pack(pady=20)

    def complete_payment(self):
        card_number = self.card_number.get()
        card_password = self.card_password.get()
        self.controller.cart.set_card_info(card_number, card_password)
        
        # 결제 완료 메시지
        tk.Label(self, text="결제가 완료되었습니다!", fg="green").pack()
        
        # 장바구니 데이터 출력 (디버깅용)
        cart_data = self.controller.cart.get_cart()
        print(cart_data)
        self.save_cart_json(cart_data)

        # 장바구니 초기화
        self.controller.cart.clear()

    def save_cart_json(self, cart_data) :
        try:
            with open("cart_data.json", "w", encoding="utf-8") as json_file:
                json.dump(cart_data, json_file, ensure_ascii=False, indent=4)
            print("장바구니 데이터가 'cart_data.json' 파일로 저장되었습니다.")
        except Exception as e:
            print(f"장바구니 데이터를 저장하는 동안 오류가 발생했습니다: {e}")
