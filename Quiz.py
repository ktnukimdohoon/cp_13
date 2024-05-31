class 음료:
    def __init__(self, 이름, 수량):
        self.이름 = 이름
        self.수량 = 수량
        self.메뉴 = {"커피": 3000,"녹차": 2500,"아이스티": 3000 }
        self.가격 = self.메뉴.get(이름, 0)

    def 계산(self):

        if self.이름 in self.메뉴:
            return self.가격 * self.수량
        else:
            return "해당 음료는 메뉴에 없습니다."

음료_이름 = input("주문할 음료를 선택하세요 (커피, 녹차, 아이스티): ")
수량 = int(input("주문할 수량을 입력하세요: "))

주문한_음료 = 음료(음료_이름, 수량)

총_가격 = 주문한_음료.계산()
print(f"총 가격은 {총_가격}원입니다." if isinstance(총_가격, int) else 총_가격)