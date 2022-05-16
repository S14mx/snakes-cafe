new_line = "\n"

intro_start = "*" * 38

intro_body = """ 
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" ** """

intro_end = new_line + intro_start

menu = {
    "Appetizers": ["Wings", "Cookies", "Spring Rolls"],
    "Entrees": ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"],
    "Deserts": ["Ice Cream", "Cake", "Pie"],
    "Drinks": ["Coffee", "Tea", "Unicorn Tears"]
}

order = {}

print(intro_start, intro_body, intro_end)

for section in menu.keys():
    print(new_line + section + new_line + "-" * len(section))
    for item in menu[section]:
        print(item)

print(new_line + "*" * 35, new_line + "** What would you like to order? **" + new_line + "*" * 35)

user_input = input("> ").title()


def add_to_order(user_input):
    for section in menu:
        if user_input in menu[section]:
            if user_input in order:
                order[user_input] += 1
            else:
                order[user_input] = 1
            print(f"** {order[user_input]} {'order' if order[user_input] == 1 else 'orders'} of {user_input} {'has' if order[user_input] == 1 else 'have' } been added to your meal **")
            break
    else:
        if user_input in order:
            order[user_input] += 1
        else:
            order[user_input] = 1
        print(f"** We dont have {user_input} on the menu but we will make it happen! **")


while user_input != "quit":
    add_to_order(user_input)
    print("Your total order is:")
    for item in order:
        print(f" {item}" + f" {order[item]}")
    user_input = input("> ").title()
