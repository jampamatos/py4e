#Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
# Once 'done' is entered, print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate 
# message and ignore the number. 
# Enter 7, 2, bob, 10, and 4 and match the output below. 

largest = 0
smallest = 0

while True:
    num = input("Enter a number: ")
    
    try:
        if num != "done":
            val = int(num)        
    except:
        print("Invalid input")
        
    if smallest == 0 or val <= smallest:
        smallest = val
        
    if num == "done":
        break
    elif val > largest:
        largest = val
    elif val <= smallest:
        smallest = val
        

print("Maximum is", largest)
print("Minimum is", smallest)