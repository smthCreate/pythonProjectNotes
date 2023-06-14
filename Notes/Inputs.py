def inputing_str(messege):
    move = input(messege)
    return move

def inputing_int(messege):
    print(messege)
    while True:
        try:
            move = int(input("Input your choice: "))

        except ValueError:
            print("Please! Input correct number!")
            continue
        break
    return move