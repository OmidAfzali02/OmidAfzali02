code_d = "abcdefghijklmnopqrstuvwxyz .@!0123456789"
code_e = code_d[-1] + code_d[0:-1]

dict_code_e = dict(zip(code_d, code_e))
dict_code_d = dict(zip(code_e, code_d))


def Crypto():
    mode = input("Encrypt (e), Decrypt (d) or exit(exit):  ")
    msg = input("Type message:  ")
    while mode != "exit":

        if mode == "e":
            print("".join([dict_code_e[letter] for letter in msg.lower()]))
            mode = input("Encrypt (e), Decrypt (d) or exit(exit):  ")
            msg = input("Type message:  ")
        elif mode == "d":
            print("".join([dict_code_d[letter] for letter in msg.lower()]))
            mode = input("Encrypt (e), Decrypt (d) or exit(exit):  ")
            msg = input("Type message:  ")
        else:
            break


Crypto()