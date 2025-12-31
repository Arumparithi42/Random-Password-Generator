import random
import string

def generate(length):
    #creatring characters
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digit = string.digits
    symbol = string.punctuation
    characters = lower + upper + digit + symbol
    #Ensuring the password has atleast one character type
    password = [random.choice(lower), random.choice(upper),
                random.choice(digit), random.choice(symbol)]
    #Generating remaining characters
    for _ in range(length - 4):
        password.append(random.choice(characters))
    #Shuffling the password for better randomness
    random.shuffle(password)
    return ''.join(password)
def get_length():
    while True:
        try :
            length = int(input("Enter the length of the password : "))
            if length < 0 :
                raise IndexError("length cannot be negative")
            elif length < 10 :
                raise IndexError("length must be atleast 10")
            return length
        except IndexError as e:
            print(e)
        except ValueError:
            print("Please Enter a valid number")
if __name__ == "__main__":
    print("--Random Password Generator--\n")
    length = get_length()
    password = generate(length)
    print("Generated password :", password)
