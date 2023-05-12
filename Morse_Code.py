import pygame, time
pygame.init()

char_to_morse = {'!':"-.-.--",'"':".-..-.",'$':"...-..-",'&':".-...","'":".----.",'(':"-.--.",')':"-.--.-",'+':".-.-.",',':"--..--",'-':"-....-",'.':".-.-.-",'/':"-..-.",'0':"-----",'1':".----",'2':"..---",'3':"...--",'4':"....-",'5':".....",'6':"-....",'7':"--...",'8':"---..",'9':"----.",':':"---...",';':"-.-.-.",'=':"-...-",'?':"..--..",'@':".--.-.",'_':"..--.-",'A':".-",'B':"-...",'C':"-.-.",'D':"-..",'E':".",'F':"..-.",'G':"--.",'H':"....",'I':"..",'J':".---",'K':"-.-",'L':".-..",'M':"--",'N':"-.",'O':"---",'P':".--.",'Q':"--.-",'R':".-.",'S':"...",'T':"-",'U':"..-",'V':"...-",'W':".--",'X':"-..-",'Y':"-.--",'Z':"--.."}
morse_to_char = {v:k for k,v in char_to_morse.items()}

def text_to_morse(msg):
    out = [char_to_morse[x] if x in char_to_morse else '' for x in msg.upper()]
    return " ".join(out)

def morse_to_text(morse):
    return " ".join("".join(morse_to_char.get(code, "") for code in word.split(" ")) for word in morse.split("  "))

def play_morse_sound(morse):
    dot = pygame.mixer.Sound("dot.wav")
    dash = pygame.mixer.Sound("dash.wav")
    
    for x in morse:
        if x != ' ':
            if x == '.':
                dot.play()
                pygame.time.wait(200)
            else:
                dash.play()
                pygame.time.wait(400)
        else:
            pygame.time.wait(200)
    pygame.time.wait(200)

def main(message):
    print("--------------------------------------------------------------")
    print(f"Original: {message.upper()}")
    encoded = text_to_morse(message)
    print(f"Encoded: {encoded}")
    print(f"Decoded: {morse_to_text(encoded)}")
    print("--------------------------------------------------------------")
    
    play_morse_sound(encoded)

if __name__ == '__main__':
    message = input("Enter message: ")
    main(message)
