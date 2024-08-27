from praktikum.burger import Burger


class TestBurger:
    def test_burger_initialization(self):
        burger = Burger()
        assert burger.ingredients == []
        assert burger.bun is None

    def test_burger_set_buns_to_burger(self, black_bun):
        burger = Burger()
        burger.set_buns(black_bun)
        assert burger.bun == black_bun

    def test_burger_add_ingredient(self, hot_sauce):
        burger = Burger()
        burger.add_ingredient(hot_sauce)
        assert hot_sauce in burger.ingredients

    def test_burger_remove_ingredient(self, hot_sauce):
        burger = Burger()
        burger.add_ingredient(hot_sauce)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_burger_move_ingredient(self, sour_cream, hot_sauce):
        burger = Burger()
        burger.add_ingredient(sour_cream)
        burger.add_ingredient(hot_sauce)
        burger.move_ingredient(1, 0)
        assert burger.ingredients == [hot_sauce, sour_cream]

    def test_burger_get_price(self, black_bun, sour_cream, hot_sauce):
        burger = Burger()
        burger.set_buns(black_bun)
        burger.add_ingredient(sour_cream)
        burger.add_ingredient(hot_sauce)
        expected_price = black_bun.get_price() * 2 + sour_cream.get_price() + hot_sauce.get_price()
        assert burger.get_price() == expected_price

    def test_burger_get_receipt(self, black_bun, hot_sauce):
        burger = Burger()
        burger.set_buns(black_bun)
        burger.add_ingredient(hot_sauce)
        receipt = burger.get_receipt()
        expected_receipt = (f'(==== {black_bun.get_name()} ====)\n'
                            f'= sauce {hot_sauce.get_name()} =\n'
                            f'(==== {black_bun.get_name()} ====)\n'
                            '\n'
                            f'Price: {burger.get_price()}')
        assert receipt == expected_receipt
