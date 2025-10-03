def online_store():
    apple = 200
    banana = 400
    orange = 600
    combo1 = apple + banana - (0.10 * (apple + banana))
    combo2 = banana + orange - (0.10 * (banana + orange))
    combo3 = apple + orange - (0.10 * (apple + orange))
    Gift_Pack = apple + banana + orange - (0.25 * (apple + banana + orange))

    print("Output: ")
    print("Online Store")
    print("----------------------")
    print("Product(S)                           Price")
    print(f"Apple                                {apple:.2f}")
    print(f"Banana                               {banana:.2f}")
    print(f"Orange                               {orange:.2f}")
    print(f"Combo 1 (apple + banana)             {combo1:.2f}")
    print(f"Combo 2 (banana + orange)            {combo2:.2f}")
    print(f"Combo 3 (apple + orange)             {combo3:.2f}")
    print(f"Gift Pack (apple + banana + orange)  {Gift_Pack:.2f}")
    print("_________________________________")
    print("For delivery Contact: 1234567890")


online_store()

# The function online_store() defines individual product prices, then calculates discounted prices for combos. Discounts are computed using arithmetic operations, applying either 10% or 25% off depending on the combo. The function uses formatted printing (f-strings) to show the product catalog neatly, demonstrating basic procedural programming with function structure and formatted output. No external sources were used to create this function.
