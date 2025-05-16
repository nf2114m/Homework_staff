def invest(amount, rate, years):
    current_amount=amount
    for i in range(1, years+1):
        increased_amount=(current_amount/100)*rate
        current_amount=current_amount+increased_amount
        print(f"year {i}: ${current_amount:.2f}")
        
    

amount, rate, years = map(int,input("Enter 'amount, rate, years' : ").split())
invest(amount, rate, years)
