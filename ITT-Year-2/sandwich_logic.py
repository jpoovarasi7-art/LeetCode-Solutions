test_cases = int(input("Enter the number of test cases: "))

for _ in range(test_cases):
    while True:
        bun = int(input("Enter the number of buns: "))
        if bun % 2 == 0:
            break
        print("Sorry, Number of buns must be even. Try again.")

    # A sandwich needs 2 buns. Total sandwiches possible = bun // 2
    # If sandwiches is odd, Arun's friend can buy at least one.
    if (bun // 2) % 2 != 0:
        print("Yes, Arun's friend can buy at least one sandwich")
    else:
        print("No, Arun's friend can't buy the sandwich")
