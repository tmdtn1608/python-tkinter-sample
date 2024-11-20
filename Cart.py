class Cart:
    def __init__(self):
        # 초기 장바구니 데이터 구조
        self.data = {
            "category": "",
            "flavor": "",
            "toppings": {},  # 토핑과 개수
            "card_number": "",
            "card_password": ""
        }

    def set_category(self, category):
        """카테고리 설정"""
        self.data["category"] = category

    def set_flavor(self, flavor):
        """맛 설정"""
        self.data["flavor"] = flavor

    def add_topping(self, topping, count=1):
        """토핑 추가"""
        if topping in self.data["toppings"]:
            self.data["toppings"][topping] += count
        else:
            self.data["toppings"][topping] = count

    def set_card_info(self, card_number, card_password):
        """카드 정보 설정"""
        self.data["card_number"] = card_number
        self.data["card_password"] = card_password

    def get_cart(self):
        """전체 장바구니 데이터 반환"""
        return self.data

    def clear(self):
        """장바구니 초기화"""
        self.__init__()  # 초기화 시 다시 기본값으로 설정
