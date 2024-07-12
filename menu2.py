from module2 import Bank

bank = Bank()

while True:
    serv = int(input("Service Provided:\n1. Acc Creation\n2. Deposit\n3. Withdraw\n4. Fixed Deposit\n5. Transaction Details\n6. Check Credit Card Eligibility\n7. Exit\n"))
    if serv == 1:
        name = input("Enter Name: ")
        bal = int(input("Enter Deposit Amt: "))
        fd = int(input("Enter FD Amt: "))
        bank.create(name, bal, fd)
    elif serv == 2:
        accno = int(input("Enter Accno: "))
        isacc = False
        for i in bank.data:
            if i[1] == accno:
                isacc = True
                break
        if isacc:
            depamt = int(input("Enter Deposit amt: "))
            bank.deposit(accno, depamt)
        else:
            print("Invalid Account No.")
    elif serv == 3:
        accno = int(input("Enter Accno: "))
        isacc = False
        for i in bank.data:
            if i[1] == accno:
                isacc = True
                break
        if isacc:
            witamt = int(input("Enter Withdraw Amount: "))
            bank.withdraw(accno, witamt)
        else:
            print("Invalid Account No.")
    elif serv == 4:
        accno = int(input("Enter Accno: "))
        isacc = False
        for i in bank.data:
            if i[1] == accno:
                isacc = True
                break
        if isacc:
            fdamt = int(input("Enter FD Amount: "))
            yrs = int(input("Enter FD Years: "))
            bank.fd(accno, fdamt, yrs)
        else:
            print("Invalid Account No.")
    elif serv == 5:
        accno = int(input("Enter Accno: "))
        bank.transaction(accno)
    elif serv == 6:
        accno = int(input("Enter Accno: "))
        bank.credit_card(accno)
    elif serv == 7:
        break
    else:
        print("Invalid option. Please try again.")

        #error
        