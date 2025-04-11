#17.1 Code-Like Starter Code
name_id = {"Jim":23987, "Bob":29832, "Alice":98734, "Tim":18973, "James":87346, "Jimothy":36719}

#code here
while True:
    username = input("Enter a name or type 'quit' to exit: ")
    if username == "quit":
        break
    elif username in name_id:
        print(f"{username}'s ID is: {name_id[username]}")
    elif username not in name_id:
        print(f"{username} not found")
        add_id = input(f"Enter an ID for {username}: ")
        if add_id != "":
            name_id[username] = add_id


print("Code-Like Completed!")
