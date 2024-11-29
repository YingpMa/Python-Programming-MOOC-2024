# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents
        self.__money = self.__euros + self.__cents * 0.01


    def __str__(self):
        return f"{self.__money:.2f} eur"

    def __eq__(self, another):
        return self.__money == another.__money

    def __lt__(self, another):
        return self.__money < another.__money

    def __gt__(self, another):
        return self.__money > another.__money

    def __ne__(self, another):
        return self.__money != another.__money

    def __sub__(self, another):
        if self.__money - another.__money < 0:
            raise ValueError
        else:
            money = self.__money * 100 - another.__money * 100
            integer = money // 100
            decimal = money % 100
            new_money = Money(integer, decimal)
            return new_money

    def __add__(self, another):
        money = self.__money * 100 + another.__money * 100
        integer = money // 100
        decimal = money % 100
        new_money = Money(integer, decimal)
        return new_money

if __name__ == "__main__":
    e1 = Money(4, 5)
    e2 = Money(2, 95)
    print(e1)
    e1.euros = 1000
    print(e1)

