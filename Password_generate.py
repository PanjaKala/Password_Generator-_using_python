#!/usr/bin/env python
# coding: utf-8

# In[8]:


import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','(',')']
print("Welcome to Password Generator:")
n_letters=int(input("Enter the number of letters you want in the password:"))
n_numbers=int(input("Enter the number of numbers you want in the password:"))
n_symbols=int(input("Enter the number of symbols you want in the password:"))
l=[]
for i in range(n_letters):
    char=random.choice(letters)
    l+=char
for i in range(n_numbers):
    char=random.choice(numbers)
    l+=char
for i in range(n_symbols):
    char=random.choice(symbols)
    l+=char
random.shuffle(l)
result=""
for i in l:
    result+=i
print(result)


# 
