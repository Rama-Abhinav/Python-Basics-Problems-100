#Find quotient and remainder without using / or %.							

def Manual_Division(dividend: int, divisor: int) -> int:

    if divisor == 0:
        raise ValueError("Divisor Cannot be Zero!!")

    remainder = dividend                                #Initially Dividend is the divisor
    quotient = 0

    while remainder >= divisor:
        remainder -= divisor
        quotient += 1

    return remainder, quotient

try:

    Dividend, Divisor = (input("Enter The Dividend and Divisor(Seperated By Spaces): ")).split()
    rem, quo = Manual_Division(int(Dividend),int(Divisor))

    print(f"""\n
{Dividend} by {Divisor} gives
Quotient = {quo}
Remainder = {rem}
    """)

except ValueError as e:
    print("Error:",e)
