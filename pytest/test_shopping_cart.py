from shopping_cart import ShoppingCart


def test_can_add_item_to_cart():
    my_cart = ShoppingCart()
    my_cart.add("milk")
    my_cart.add("eggs")
    my_cart.add("almonds")

    assert my_cart.size() == 3

