# Discount Calculator

import tkinter as tk

def calculate_discount_percentage(total):
    if total >= 100:
        discount = 20
    elif total > 0 and total < 100:
        discount = 10
    return discount

def calculate_discount(total):
    discount_per=calculate_discount_percentage(total)
    discount = total-total/100 * discount_per

def get_bill():

    bill_amount = entry_box.get()

    try:
        bill_total = float(bill_amount)
    except ValueError as e:
        # textbox["text"] = "Incorrect Value"
        return