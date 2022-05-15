new_line = "\n"

intro_start = "*" * 38

intro_body = """ 
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" ** """

intro_end = new_line + intro_start

menu = {
    "Appetizers": {"Wings": 0, "Cookies": 0, "Spring Rolls": 0},
    "Entrees": {"Salmon": 0, "Steak": 0, "Meat Tornado": 0, "A Literal Garden": 0},
    "Deserts": {"Ice Cream": 0, "Cake": 0, "Pie": 0},
    "Drinks": {"Coffee": 0, "Tea": 0, "Unicorn Tears": 0}
}

print(intro_start, intro_body, intro_end)

for section in menu.keys():
    print(new_line + section + new_line + "-" * len(section))
    for item in menu[section].keys():
        print(item)

print(new_line + "*" * 35, new_line + "** What would you like to order? **" + new_line + "*" * 35)

user_input = input("> ").title()


def add_to_order(user_input):
    for section in menu:
        if user_input in menu[section]:
            menu[section][user_input] += 1
            print(f"** {menu[section][user_input]} {'order' if menu[section][user_input] == 1 else 'orders'} of {user_input} {'has' if menu[section][user_input] == 1 else 'have' } been added to your meal **")
            break
    else:
        print(f"Sorry, we dont have {user_input} on the menu")

while user_input != "quit":
    add_to_order(user_input)
    user_input = input("> ").title()
