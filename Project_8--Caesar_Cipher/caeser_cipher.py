alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

#importing logo
from art import logo

print(logo)


#encoding and decoding
def caesar(text, shift, direction):
    list = []
    if direction == 'decode':
        shift *= -1
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index + shift) % 26
            list.append(alphabet[new_index])
        else:
            list.append(char)
    print(f"The {direction}d text is {''.join(list)}")


should_continue = True
while should_continue:
    #user input
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #Calling function
    caesar(text, shift, direction)
    user_choice = input(
        "Type 'yes' if you want to go again. Otherwise type 'no' \n")
    if user_choice == 'no':
        should_continue = False
        print("Good Bye")