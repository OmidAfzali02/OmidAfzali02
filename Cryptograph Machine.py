# First we create the keys and the encrypted keys. it is better to use the a string:
code_d = "abcdefghijklmnopqrstuvwxyz .@!0123456789"
# We use string slice so we don't need to type these twice
code_e = code_d[-1] + code_d[0:-1]

# Then we need to make two dictionaries for encryption and decryption using zip() function:
dict_code_e = dict(zip(code_d, code_e))
dict_code_d = dict(zip(code_e, code_d))


# Now we create the whole program function name Crypto:


def Crypto():
    # Now we ask the user whether he wants to encrypt or decrypt a message and what the message is:
    mode = input("Encrypt (e), Decrypt (d) or exit(exit):  ")
    if mode != "exit":
        msg = input("Type message:  ")
        # We create a while loop to indicate when should the program stop:
        while mode != "exit":
            # Now we use the conditionals to write the programs logics:
            # We will update the msg and mode so we can indicate when we want to end the program or what else we want to do:
            if mode.lower() == "e":
                print("".join([dict_code_e[letter] for letter in msg.lower()]))
                mode = input("Encrypt (e), Decrypt (d) or exit(exit):  ")
                msg = input("Type message:  ")
            elif mode.lower() == "d":
                print("".join([dict_code_d[letter] for letter in msg.lower()]))
                mode = input("Encrypt (e), Decrypt (d) or exit(exit):  ")
                msg = input("Type message:  ")
            elif mode.lower() == "exit":
                break


# Now we run the function we write for the whole program:
Crypto()