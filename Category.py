import tkinter as tk
from Const import category_list,screen_flavor

# 첫번째 카테고리 화면
class Category(tk.Frame):
    def __init__(self, controller):
        '''controller는 메인클래스(Kiosk)를 의미'''
        super().__init__(controller)
        self.controller = controller

        # 화면설명 타이틀
        tk.Label(
            self, 
            text="카테고리 선택", 
            font=("Arial", 20)
        ).pack(pady=20)
        
        # 카테고리 리스트로부터 반복하여
        for category in category_list:
            """
            버튼을 만든다
            tk.Button(만들 장소, text=버튼에 들어갈 문자, 버튼 클릭시 실행할 행동)
            .pack() -> 화면에 배치하겠다.
            ()안에는 배열할때 위치나 크기 등 각종 설정을 추가할수 있다.
            pady는 y방향으로 여백을 주겠다라는 의미
            """
            
            tk.Button(
                self,
                text=category,
                command=lambda c=category: self.select_category(c)
            ).pack(pady=10)

    """버튼선택했을때 동작"""
    def select_category(self, category):
        # 부모클래스에서 선언한 카트에 선택한 카테고리를 담는다.
        self.controller.cart.set_category(category)
        # 부모클래스의 함수를 호출하여 화면을 전환시킬 수 있다.
        self.controller.show_screen(screen_flavor)
