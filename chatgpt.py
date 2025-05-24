# Example 1: Check if P/E is reasonable
pe = 18
is_pe_good = pe < 20

# Example 2: Is dividend yield attractive?
div_yield = 3.2
if div_yield >= 3.0:
    print("Good dividend yield")

# Example 3: EPS growth check
eps_2024 = 30
eps_2023 = 25
print(eps_2024 > eps_2023)  # True
