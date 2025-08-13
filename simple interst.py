def sml(p,t,r):
    print('principle value -:',p)
    print('time value -:',t)
    print('interest rate value -:',r)
    while True:
        user_input = input("Enter a command (type 'stop' to end): ")
        
        if user_input.lower() == 'stop':
            print("Stopping the loop.")
            break  # Exit the loop if the user enters 'stop'
        si = (p * t * r)/100
        return si
sml(p=int(input('Enter the principle amount')),t=int(input('Enter the time (year) -:')),r=float(input('Enter interset rat -:')))
    
