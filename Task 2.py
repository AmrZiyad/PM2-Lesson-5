# 1) Take an integer input from the user
rows = int(input("Enter the number of rows: "))

# 2) Initialize number = 1
number = 1

# 3) Print a heading message
print("Floyd's Triangle")

# 4) Outer loop to handle each row from 1 to rows (inclusive)
for i in range(1, rows + 1):
    
    # 5) Inner loop to handle numbers in each row
    for j in range(1, i + 1):
        # b) Print the current value on the same line
        print(number, end=" ")
        # c) Increase number by 1
        number += 1
        
    # 6) Print a blank print() to move to the next line
    print()
