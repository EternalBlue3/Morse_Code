import pygame, time
pygame.init()

char_to_morse = {
'!':"-.-.--",
'"':".-..-.",
'$':"...-..-",
'&':".-...",
"'":".----.",
'(':"-.--.",
')':"-.--.-",
'+':".-.-.",
',':"--..--",
'-':"-....-",
'.':".-.-.-",
'/':"-..-.",
'0':"-----",
'1':".----",
'2':"..---",
'3':"...--",
'4':"....-",
'5':".....",
'6':"-....",
'7':"--...",
'8':"---..",
'9':"----.",
':':"---...",
';':"-.-.-.",
'=':"-...-",
'?':"..--..",
'@':".--.-.",
'_':"..--.-",
'A':".-",
'B':"-...",
'C':"-.-.",
'D':"-..",
'E':".",
'F':"..-.",
'G':"--.",
'H':"....",
'I':"..",
'J':".---",
'K':"-.-",
'L':".-..",
'M':"--",
'N':"-.",
'O':"---",
'P':".--.",
'Q':"--.-",
'R':".-.",
'S':"...",
'T':"-",
'U':"..-",
'V':"...-",
'W':".--",
'X':"-..-",
'Y':"-.--",
'Z':"--.."
}
morse_to_char = {v:k for k,v in char_to_morse.items()}

char_delimit = " "
word_delimit = "  "
# Between chars is 2 spaces
def charToMorse(c):
    if c in char_to_morse:
        return char_to_morse[c]
    elif c == ' ':
        return char_delimit
    else:
        return ""

# Between words is 3 spaces
def writeMorse(msg):
    out = []
    for word in msg.upper().split(" "):
        out.append(char_delimit.join( filter(bool, map(charToMorse, word)) ))
    return word_delimit.join(out)

def morseToChar(m):
    if m in morse_to_char:
        return morse_to_char[m]
    else:
        return ""

def readMorse(morse):
    out = []
    for word in morse.split(word_delimit):
        out.append( "".join( filter(bool, map(morseToChar, word.split(char_delimit))) ) )
    return " ".join(out)

def play_morse_sound(morse):
    
    for x in range(len(morse)):
        if morse[x] != ' ':
            if morse[x] == '.':
                dot = pygame.mixer.Sound("dot.wav")
                dot.play()
                pygame.time.wait(int(dot.get_length() * 1400))
            else:
                dash = pygame.mixer.Sound("dash.wav")
                dash.play()
                pygame.time.wait(int(dash.get_length() * 1200))
        else:
            time.sleep(0.2)
            
    time.sleep(0.2)

def doTest(test_message):
    print("--------------------------------------------------------------")
    print("Original: %s" % test_message.upper())
    a = writeMorse(test_message)
    print("Morse: %s" % a)
    b = readMorse(a)
    print("and Back: %s" % readMorse(a))
    print("Valid? %s" % ("Yes" if test_message.upper() == b else "No"))
    print("--------------------------------------------------------------")
    return a

a = doTest(str(input("Enter message: ")))

play_morse_sound(a)