# ProductDiscount
A simple Python script that calculates the final price of a product by applying different discounts based on the payment method selected by the user.

# 🛒 Product Discount Calculator

This is a command-line program written in Python that calculates the final price of a product based on one of four available payment options.

The script prompts the user for the product's original price and then asks them to choose a payment method. Based on the choice, a specific discount is applied (or not), and the final price is displayed.

## How to Use

1.  Make sure you have Python installed on your system.
2.  Save the code as a `.py` file (e.g., `ProductDiscount.py`).
3.  Open your terminal or command prompt.
4.  Navigate to the directory where the file is located and run the script:
    ```sh
    python ProductDiscount.py
    ```
5.  Enter the original price of the product and press Enter.
6.  Enter the number corresponding to your desired payment method (1-4) and press Enter to see the final price.

## Payment Options Logic

The final price is determined by the payment method selected:
* **Option 1 (Cash):** A **10% discount** is applied.
* **Option 2 (Cash by Card):** A **5% discount** is applied.
* **Option 3 (2 Installments):** The price remains unchanged (normal price).
* **Option 4 (3 Installments):** A **20% discount** is applied. *(Note: The script currently applies a 20% discount, not interest, for this option).*

If an invalid option is entered, the program displays an error message.
