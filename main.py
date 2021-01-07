print("Welcome to the Bond Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()

t_in_name1 = int(name1.count('t'))
t_in_name2 = int(name2.count('t'))

r_in_name1 = int(name1.count('r'))
r_in_name2 = int(name2.count('r'))

u_in_name1 = int(name1.count('u'))
u_in_name2 = int(name2.count('u'))

e_in_name1 = int(name1.count('e'))
e_in_name2 = int(name2.count('e'))

total_true = t_in_name1+t_in_name2+r_in_name1+r_in_name2+u_in_name1+u_in_name2+e_in_name1+e_in_name2

l_in_name1 = int(name1.count('l'))
l_in_name2 = int(name2.count('l'))

o_in_name1 = int(name1.count('o'))
o_in_name2 = int(name2.count('o'))

v_in_name1 = int(name1.count('v'))
v_in_name2 = int(name2.count('v'))

e_in_name1 = int(name1.count('e'))
e_in_name2 = int(name2.count('e'))

total_love = l_in_name1+l_in_name2+o_in_name1+o_in_name2+v_in_name1+v_in_name2+e_in_name1+e_in_name2

bond_percentage = str(total_true)+str(total_love)
bond_percentage = int(bond_percentage)

if bond_percentage<10 or bond_percentage>90:
  print(f"Your score is {bond_percentage} , you go together like coke and mentos.")
elif bond_percentage>=40 or bond_percentage<=50:
  print(f"Your score is {bond_percentage} , you are alright together.")
else:
  print(f"Your score is {bond_percentage}.")