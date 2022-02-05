# nested loops


Rows = int(input("How many rows: "))
Columns = int(input("How many columns: "))
Symbol = input("Enter symbol: ")


for i in range(Rows):
    for j in range(Columns):
        print(Symbol, end="")
    print()

