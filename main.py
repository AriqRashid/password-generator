import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '^', '@']

print('Password Generator')
char_count = int(input('How many characters do you want? A minimum of 12 is recommended: '))

user_let = input("Do you want letters? Enter 'Yes' or 'No': ").lower()
if user_let == str('yes'):
    let_check = True
elif user_let == str('no'):
    let_check = False

user_num = input("Do you want Numbers? Enter 'Yes' or 'No': ").lower()
if user_num == str('yes'):
    num_check = True
elif user_num == str('no'):
    num_check = False

user_sym = input("Do you want Special Characters? Enter 'Yes' or 'No': ").lower()
if user_sym == str('yes'):
    sym_check = True
elif user_sym == str('no'):
    sym_check = False

p_list = []
count = 0
def get_let():
    global count
    if let_check:
        p_list.append(random.choice(letters))
        count += 1
        return count

def get_num():
    global count
    if num_check:
        p_list.append(random.choice(numbers))
        count += 1
        return count

def get_sym():
    global count
    if sym_check:
        p_list.append(random.choice(symbols))
        count += 1
        return count

while count < char_count:
    choose = random.randrange(0,3)
    if choose == 0:
        get_let()
    elif choose == 1:
        get_num()
    elif choose == 2:
        get_sym()

password = ''.join(p_list)
print(f"You're password is: { password } ")
