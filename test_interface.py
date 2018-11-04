from pytivo import tivo_client

host = input("IP Address: ")
port = int(input("Port (Should be 31339): "))

tc = tivo_client.TivoClient(host, port)

print("STATUS: "+ tc.getStatus())

def menu():
    print("""
    1. Set Channel
    2. Get Status
    3. Send an IRCode
    4. Teleport Somewhere
    5. Send a keyboard code
    """)
    selection = int(input("Choose an action: "))
    if selection == 1:
        #Set Channel
        print(tc.setChannel( input("Enter a channel number: ") ))
        menu()
    elif selection == 2:
        #Get Status
        print(tc.getStatus())
        menu()
    elif selection == 3:
        #Send IRCode
        print(tc.sendIRCode( input("Enter an IRCode: ") ))
        menu()
    elif selection == 4:
        #Teleport
        print(tc.teleport( input("Enter a teleport area") ))
        menu()
    elif selection == 5:
        #Send Keyboard Code
        menu()

menu()