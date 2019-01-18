import webbrowser

helloIntent = ['hi','hello','hey','hi there','hello there']

chat = True
while chat:
    msg = input("Enter your message : ")
    if msg in helloIntent:
        print("Hello There...")
    elif msg.startswith('open'):
        web = msg.split()[-1]
        webbrowser.open(web+'.com')
    elif msg == "bye":
        print("Bye User")
        chat = False
    else:
        print("I don't understand")
