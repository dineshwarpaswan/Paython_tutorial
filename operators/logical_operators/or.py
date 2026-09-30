print()
print(True or True) # Print will be: True
print(True or False) # Print will be: True
print(False or False) # Print will be: False
print()

a= (20==20) or (25==25) 
print("Type1, If both correct, Print will be True: ",a) # If both correct, Print will be True
a= (20==20) or (20==50)
print("Type1, If both any one correct, Print will be True: ",a) # If both any one correct, print will be: True
a= (50==20) or (40==50)
print("Type1, If both not any one correct, Print will be False: ",a) # If both any one correct, print will be: False
print()

ram= "2GB"
nam = (ram=="3GB") or (ram=="2GB")
print("Type2, If both any one match , Result will be True: ",nam) # If both any one match, Result will be: True
ram= "5GB"
nam = (ram=="5GB") or (ram=="5GB")
print("Type2, If both  match , Result will be True: ",nam) # If both  match, Result will be: True
ram= "5GB"
nam = (ram=="10GB") or (ram=="6GB")
print("Type2, If both No any one match , Result will be False: ",nam) # If both no any one match , Result will be: False
print("")

b = (20 > 550) or (20 < 56)
print("Type3, If both one correct , Result will be True: ",b)  #If both any one correct, print will be: True
b = (200 > 50) or (200 < 500)
print("Type3, If both  correct , Result will be True: ",b)  #If both  correct, print will be: True
b = (500 > 550) or (2500 < 500)
print("Type3, If both no any one correct , Result will be False: ",b)  #If both no any one correct, print will be: False
print()

b =1000
b = (1000 > 550) or (2500 < 1000)
print("Type4, If both one correct , Result will be True: ",b)  #If both any one correct, print will be: True
b =1000
b = (1000 > 550) or (250 < 1000)
print("Type4, If both  correct , Result will be True: ",b)  #If both  correct, print will be: True
b =1000
b = (1000 > 5050) or (3050 < 1000)
print("Type4, If both no any one correct , Result will be False: ",b)  #If both no any one correct, print will be: False
print()

c = "Dineshwar"
c1 =(c=="Dineshwar") or (c=="paswan")
print("Type5, If both one Match , Result will be True: ",c1)  #If both any one Match, print will be: True
c = "Dineshwar"
c1 =(c=="Dineshwar") or (c=="Dineshwar")
print("Type5, If both  Match , Result will be False: ",c1)  #If both  Match, print will be: True
lp = "Del"
x1=(lp=="hp") or (lp=="sony") 
print("Type5, If both no any one Match , Result will be False: ",x1)  #If both no any one Match, print will be: False
print()

  
if lp=="hp" or lp=="sony":
     print("yes True")  #If both  Match, print will be: True
else:
    print("Type6, If both no any one Match , Result will be False")  #If both no any one Match, print will be: False
	
lap="sony"
if lap=="hp" or lap=="sony": 
    print("Type6, If both any one Match , Result will be True: ",lap)  #If both no any one Match, print will be: True

	
lp1="sony"
lp2 = (lp1=="sony") or (lp1=="sony") 
print("Type7, If both  Match , Result will be True: ",lp2)  #If both no any one Match, print will be: True
print()

y = 5
if y==5 or y==5:
    print("type8 If both any one correct",y) #If both any one Match, print will be: True
	
if 4==4 or 4==5:
    print("type9 If both any one correct,print will be True") #If both any one Match, print will be: True
	
if 4==4 or 5==5:
    print("type10 If both  correct, print will be True") #If both  Match, print will be: True
	
if 4==5 or 5==6:
    print("yess true,") #If both  Match, print will be: True
else:
    print("Type11, If both no any one Match , Result will be False")  #If both no any one Match, print will be: False
print()

dig="Engineer"
sal=85000
if dig=="Doctor" or sal==85000: 
    print("Type12 Right True ") # If both conditional any one  is correct, Result will be: True
else:
    print("Type12 Worng False ")
	
print()

if dig=="advocate" or sal== 50000:
    print("Type13, yess True")
else:
    print("Type 13, If both data not match ,Result will be False") #If both data not match ,Result will be: False
print()

if dig=="Engineer" or sal== 85000:
    print("Type14, If both data match ,Result will be True") #If both data match ,Result will be :True
else:
    print("Type 14, If both data not match ,Result will be False") #If both data not match ,Result will be: False