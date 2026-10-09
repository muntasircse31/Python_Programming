#take input and print middle 3 characters , last 2 character#quetion slicing
#Anik 4/2 = 2 (0 1 2 3) 2-1 = 1 and 2+1 = 3 (middle 3 characters = 1 to 3)
str = input("Enter a string: ")
mid = len(str) // 2
output1= str[mid-1:mid+2] #middle 3 characters
output2= str[-2:] #last 2 characters
print("Middle 3 characters:", output1)
print("Last 2 characters:", output2)