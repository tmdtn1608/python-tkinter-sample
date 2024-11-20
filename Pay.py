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

        self.price_label = tk.Label(self, font=("Arial", 16), fg="blue")
        self.price_label.pack(pady=10)

        tk.Button(self, text="결제 완료", command=self.complete_payment).pack(pady=10)

    """가격 동적으로 업데이트"""
    '''
    가격을 동적으로 표기하는 이유.
    tk main에서 먼저 클래스를 생성했기 때문에, 생성시점에서의 가격이 화면에 그대로 고정된다.
    따라서 계산결과를 다시 출력해주기 위해서는 화면 전환시 장바구니에서 가격을 가지고 설정해줘야 한다.
    만약 화면 생성시점이 토핑을 다 고르고, 계산한 이후에 한다면 구현이 필요없을지도?
    '''
    def update_price(self):
        price = self.controller.cart.data.get("prices", 0)
        self.price_label.config(text=f"총 가격: {price}원")

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
