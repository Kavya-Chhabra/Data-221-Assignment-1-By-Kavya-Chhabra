#Write a Python program that multiplies consecutive integers starting from 1 until the product first becomes greater than a given threshold value.
#Your program should:
#Store the threshold value in a variable
#Keep track of the current multiplier.
#Print the final product and the integer that caused the product to exceed the threshold.

threshold_Value = 100 # store the threshold value
current_Product = 1 #initialize the product to 1
current_Multiplier = 1 #initialize the multiplier starting from 1

#loop will run until the product value is less than the threshold
while current_Product<= threshold_Value:
  
  #multiply current product by current multiplier
    current_Product *= current_Multiplier
  
  #check if the product has exceeded the theshold
    if current_Product > threshold_Value:
        break #exit loop once the threshold has been exceeded
   
  #increase the multiplier for the next loop
    current_Multiplier += 1

#print the final product after exceeding the threshold
print("Final Product:", current_Product)

#print the number that caused the product to exceed the threshold
print("Number that executed threshold:", current_Multiplier)
