class PriceCalculator:
    def calculate_discount(self, original_price, discount_percentage):
        discount_amount = original_price * (discount_percentage / 100)
        final_price = original_price - discount_amount
        return final_price

calculator = PriceCalculator()
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))
final_price = calculator.calculate_discount(original_price, discount_percentage)
print("The final price after discount is:", final_price)
