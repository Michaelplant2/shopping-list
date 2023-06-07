shopping_list = []

def show_help():
    print("What should we get at the store")
    print("""
    Enter "DONE" to end list
    Enter "SHOW" to show your list
    Enter "HELP" to show help
    """)

def add_to_list(item):
    shopping_list.append(item)
    print("You have {} item(s) in your list".format(len(shopping_list)))

def show_list():
    print("Your list: ")
    for item in shopping_list:
        print("* {}".format(item))

show_help()
while True:
    new_item = input(">  ")

    if new_item == "DONE":
        break
    elif new_item == "HELP":
        show_help()
        continue
    elif new_item == "SHOW":
        show_list()
        continue

    add_to_list(new_item)

show_list()