def calculate_simple_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    return simple_interest

def calculate_compound_interest(principal, rate, time, frequency):
    compound_interest = principal * ((1 + rate / (frequency * 100)) ** (frequency * time) - 1)
    return compound_interest

def main():
    business_name = "Yusuf and Sons"
    print(f"Welcome to Yusuf and Sons Interest Calculator!")
    
    principal = float(input("Enter the initial principal amount: $"))
    rate = float(input("Enter the annual interest rate (in percentage): "))
    time = float(input("Enter the number of years: "))
    frequency = int(input("Enter the number of times interest is applied per time period: "))
    
    simple_interest = calculate_simple_interest(principal, rate, time)
    compound_interest = calculate_compound_interest(principal, rate, time, frequency)
    
    print(f"\nBusiness Name: {business_name}")
    print(f"Simple Interest: ${simple_interest:.2f}")
    print(f"Compound Interest: ${compound_interest:.2f}")

if __name__ == "__main__":
    main()
