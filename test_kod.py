todos = []
answer = ""

while answer.lower() != "klar":
    answer = input("Vad vill du göra?\n").strip().lower()

    if answer != "klar" and answer != "visa":
        todos.append(answer)
    elif answer == "visa":
        print("---Todo-lista---")
        for i, todo in enumerate(todos):
            print(f"{i+1}: {todo}")
    
print(todos)

