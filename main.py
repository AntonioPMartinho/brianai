

def menu():
    print("[1] English female voice assistant ")
    print("[2] Portuguese female voice assistant")

menu()
option= int(input("Choose the desired assistant: "))

while option != 0 :
    if option == 1:
        import va_en_female 


    elif option == 2:
      import va_pt_female 

    else:
        print("Invalid Option")