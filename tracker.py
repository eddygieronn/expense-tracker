# ==========================================
# Installment 4: The Tracker Makes Decisions
# ==========================================

def main():
    # Banner
    print("==========================================")
    print("             EXPENSE TRACKER              ")
    print("          Know where your money goes.     ")
    print("==========================================")

    # Main Menu
    print("MAIN MENU")
    print("  [1] Add an expense         (coming soon)")
    print("  [2] View all expenses      (coming soon)")
    print("  [3] Show total spent       (coming soon)")
    print("  [4] Exit                   (coming soon)\n")

    # Name Prompt
    name = input("What's your name? ")
    print(f"Welcome, {name}! Let's log two expenses.\n")

    # Expense 1 Input and Size Message
    item1 = input("First expense? ")
    amount1 = float(input("Amount? "))
    if amount1 > 200:
        print("  Huge expense - are you sure?")
    elif amount1 > 100:
        print("  Big expense.")
    elif amount1 > 50:
        print("  Moderate expense.")
    else:
        print("  Small expense.")

    # Expense 2 Input and Size Message
    item2 = input("Second expense? ")
    amount2 = float(input("Amount? "))
    if amount2 > 200:
        print("  Huge expense - are you sure?")
    elif amount2 > 100:
        print("  Big expense.")
    elif amount2 > 50:
        print("  Moderate expense.")
    else:
        print("  Small expense.")

    # Two-Big Warning
    if amount1 > 100 and amount2 > 100:
        print("  Two big expenses in a row - slow down!")

    # Tax & Budget Inputs
    tax_rate = float(input("Tax rate %? "))
    budget = float(input("Your budget? "))

    # Calculations
    subtotal = amount1 + amount2
    average = subtotal / 2
    tax = subtotal * (tax_rate / 100)
    grand_total = subtotal + tax
    over_budget = grand_total > budget
    left_in_budget = budget - grand_total

    # Summary
    print("\n----------------------------------------")
    print("SUMMARY")
    print(f"  - {item1 + ':':<10} ${amount1:.1f}")
    print(f"  - {item2 + ':':<10} ${amount2:.1f}")
    print(f"Subtotal:       ${subtotal:.1f}")
    print(f"Average:        ${average:.1f}")
    print(f"Tax ({tax_rate:.1f}%):     ${tax:.1f}")
    print(f"Grand total:    ${grand_total:.1f}")

    # Verdict Logic
    if over_budget:
        over_amount = grand_total - budget
        print(f"Over budget by ${over_amount:.1f}!")
    elif grand_total > (0.90 * budget):
        print(f"Careful: only ${left_in_budget:.1f} left.")
    else:
        print(f"Within budget. ${left_in_budget:.1f} left.")

    print("----------------------------------------")

    # Footer
    print(f"Made by: Eddy Gieronn P. Ugali  |   Installment 4\n")

if __name__ == "__main__":
    main()