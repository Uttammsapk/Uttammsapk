x= input("Please input your name: ")
print("Hello", x, "let's calculate the your monthly expenses")

#Writing all the months names
a = ["January", "Feb", "March","April", "May","June", "July", "August",
"September","October", "November","December"]
#Using the for loop to get the expenses 
c = 0
for i in a:
  month = i
  print("Month",month,)
  b = int(input("Enter the expenses: "))
  c = c+b
print("Your total expenses is: $",c)

print("Thankyou ",x,"Good Bye!!")

