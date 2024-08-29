from src.burger import Burger


class TestBurger:
    def test_burger_initialization(self):
        burger = Burger()
        assert burger.ingredients == []
        assert burger.bun is None

    def test_burger_set_buns_to_burger(self, black_bun):
        burger = Burger()
        burger.set_buns(black_bun)
        assert burger.bun == black_bun

    def test_burger_add_ingredient(self, hot_sauce_ingredient):
        burger = Burger()
        burger.add_ingredient(hot_sauce_ingredient)
        assert hot_sauce_ingredient in burger.ingredients

    def test_burger_remove_ingredient(self, hot_sauce_ingredient):
        burger = Burger()
        burger.add_ingredient(hot_sauce_ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_burger_move_ingredient(self, sour_cream_ingredient, hot_sauce_ingredient):
        burger = Burger()
        burger.add_ingredient(sour_cream_ingredient)
        burger.add_ingredient(hot_sauce_ingredient)
        burger.move_ingredient(1, 0)
        assert burger.ingredients == [hot_sauce_ingredient, sour_cream_ingredient]

    def test_burger_get_price(self, black_bun, sour_cream_ingredient, hot_sauce_ingredient):
        burger = Burger()
        burger.set_buns(black_bun)
        burger.add_ingredient(sour_cream_ingredient)
        burger.add_ingredient(hot_sauce_ingredient)
        expected_price = black_bun.get_price() * 2 + sour_cream_ingredient.get_price() + hot_sauce_ingredient.get_price()
        assert burger.get_price() == expected_price

    def test_burger_get_receipt(self, black_bun, hot_sauce_ingredient):
        burger = Burger()
        burger.set_buns(black_bun)
        burger.add_ingredient(hot_sauce_ingredient)
        receipt = burger.get_receipt()
        expected_receipt = (f'(==== {black_bun.get_name()} ====)\n'
                            f'= sauce {hot_sauce_ingredient.get_name()} =\n'
                            f'(==== {black_bun.get_name()} ====)\n'
                            '\n'
                            f'Price: {burger.get_price()}')
        assert receipt == expected_receipt
