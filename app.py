def calculate_npv(initial_investment, discount_rate, cash_flows):
    npv = -initial_investment  # Start with the initial investment (outflow)
    for t, cash_flow in enumerate(cash_flows, start=1):
        npv += cash_flow / (1 + discount_rate) ** t
    return npv

def main():
    print("Welcome to the NPV Calculator")
    attempts_left = 2

    while attempts_left > 0:
        try:
            initial_investment = float(input("Enter the initial investment: "))
            discount_rate = float(input("Enter the discount rate (as a decimal): "))
            num_periods = int(input("Enter the number of periods: "))

            cash_flows = []
            i = 0
            while i < num_periods:
                user_input = input(f"Enter the cash flow for period {i + 1} (or type 'go back' to re-enter previous cash flow): ")
                if user_input.lower() == 'go back':
                    if i > 0:
                        i -= 1
                        print(f"Re-enter the cash flow for period {i + 1}")
                    else:
                        print("Cannot go back from the first period.")
                else:
                    try:
                        cash_flow = float(user_input)
                        if len(cash_flows) > i:
                            cash_flows[i] = cash_flow
                        else:
                            cash_flows.append(cash_flow)
                        i += 1
                    except ValueError:
                        print("Invalid input. Please enter a numeric value.")

            npv = calculate_npv(initial_investment, discount_rate, cash_flows)
            print(f"The Net Present Value (NPV) is: {npv:.2f}")
            
            while True:
                decision = input("Would you like to start over or confirm your results? (type 'start over' or 'confirm'): ").lower()
                if decision == 'start over':
                    attempts_left -= 1
                    print(f"You have {attempts_left} start over attempt(s) left.")
                    break
                elif decision == 'confirm':
                    print("Results confirmed. Exiting the program.")
                    return
                else:
                    print("Invalid input. Please type 'start over' or 'confirm'.")
        
        except ValueError:
            print("Invalid input. Please enter numeric values.")
    
    print("No start over attempts left. Exiting the program.")

if __name__ == "__main__":
    main()