def show_help():
    print("What should we get at the store")
    print("""
    Enter "DONE" to end list
    Enter "HELP" to show help
    """)

show_help()
while True:
    new_item = input("> ")

    if new_item == "DONE":
        break
    elif new_item == "HELP":
        show_help()
        continue
