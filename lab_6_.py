option_one = 0
option_two = 0


def Encoder(password):
    encoded_password = ""
    for char in password:
        encoded_password = encoded_password + str((int(char) + 3) % 10)
    return encoded_password


def Decoder(password):
   pass



if __name__ == "__main__":
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        option = int(input("Please enter an option: "))

        if option == 1:
            option_one += 1
            if option_two >= 1:
                print("The decoded password is", answer_one + ", and the original password is", password+ ".\n")
                option_two -= 1
            else:
                password = input("Please enter your password to encode: ")
                print("Your password has been encoded and stored!\n")
                answer = Encoder(password)


        if option == 2:
            option_two += 1
            if option_one >= 1:
                print("The encoded password is", answer + ", and the original password is", password+ ".\n")
                option_one -= 1
            else:
                password = input("Please enter your password to decode: ")
                print("Your password has been decoded and stored!\n")
                answer_one = Decoder(password)



        if option == 3:
            break