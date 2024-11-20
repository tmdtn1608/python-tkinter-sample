import tkinter as tk
from Category import Category
from Flavor import Flavor
from Topping import Topping
from Pay import Pay
from Cart import Cart
from Const import ( 
    screen_category, 
    screen_topping, 
    screen_flavor, 
    screen_pay
)

"""메인클래스"""
# tkinter를 사용하기 위해 
class Kiosk(tk.Tk):
    '''
    __init__(self) 는 생성자.
    클래스가 만들어질때 실행될 함수.
    클래스의 초기화를 위해 사용한다.
    python에서 생성자는 자기자신(self)를 파라미터로 전달해줘야 한다.
    '''
    def __init__(self):
        ''' 부모클래스(tk.TK)의 생성자를 실행시킨다.  '''
        super().__init__()
        # Window 설정
        self.title("키오스크")
        self.geometry("400x300")
        
        # 장바구니 인스턴스 생성, 나중에 공통적으로 사용하게 된다.
        self.cart = Cart()
        
        # 화면 관리설정
        self.screens = {}
        self.current_screen = None
        
        # 필요한 화면 추가 
        self.add_screen(screen_category, Category)
        self.add_screen(screen_flavor, Flavor)
        self.add_screen(screen_topping, Topping)
        self.add_screen(screen_pay, Pay)
        
        # 최초 화면 표시
        self.show_screen("Category")
    
    """새 화면 추가"""
    def add_screen(self, name, screen_name):
        '''
        자기자신(메인클래스)을 각 화면클래스에게 넘겨준다(상속)
        각 화면클래스는 상속받은 메인클래스의 기능을 사용할수 있다.
        '''
        screen = screen_name(self) 
        self.screens[name] = screen
    
    """화면 전환"""
    def show_screen(self, name):
        # 현재 내 화면은
        if self.current_screen:
            # 감추고,(pack()으로 표시한 요소)
            # windows에서는 
            self.current_screen.pack_forget()
            # macOS에서는
            # self.current_screen.destroy()
        # 파라미터로 받은 값을 설정했던 화면중에 찾아서
        screen = self.screens.get(name)
        if screen:
            # 지금 화면으로 바꿔준다.
            self.current_screen = screen
            '''
            pack()은 화면에 표시해주겠다는 의미.
            fill="both", expand=True -> 화면을 window의 크기만큼 가득 채움
            '''
            self.current_screen.pack(fill="both", expand=True)

# tkinter 실행
if __name__ == "__main__":
    app = Kiosk()
    app.mainloop()
