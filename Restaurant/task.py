for main, main_price in zip(main_courses, price_main_courses):
    for dessert, dessert_price in zip(desserts, price_desserts):
        for drink, drink_price in zip(drinks, price_drinks):
            cost = main_price + dessert_price + drink_price
            if cost <= 30:
                print(main, dessert, drink, cost)
