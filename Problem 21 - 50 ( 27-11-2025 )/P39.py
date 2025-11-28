#Get a day number (1–7) and print weekday name.			

day = int(input("""Enter Day Number of the Week: 
Monday -> 1
Tuesday -> 2
Wednesday -> 3
Thrusday -> 4
Friday -> 5
Saturday -> 6
Sunday -> 7
---->> """))

match (day):
    case 1: print("Monday")
    case 2: print("Tuesday")
    case 3: print("Wednesday")
    case 4: print("Thursday")
    case 5: print("Friday")
    case 6: print("Saturday")
    case 7: print("Sunday")
    case _: print("Invalid Day Number Entered !!!!")

