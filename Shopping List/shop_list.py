shopping_list = []

def show_help():
    print("This is on going grocery list that you can add to the list.")
    print("""
    Enter 'DONE' to stop adding items.
    'HELP for this help message.
     SHOW to show your list.
""")

    
def add_to_list(item):
    shopping_list.append(item)
    print("Added! There are {} currently on your list".format(len(shopping_list)))


def show_list():
    print("Here is your list: ") 
    for item in shopping_list:
        print(item)
    
show_help()
while True:
    new_item = input("> ")
    
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue
    
    add_to_list(new_item)
show_list()