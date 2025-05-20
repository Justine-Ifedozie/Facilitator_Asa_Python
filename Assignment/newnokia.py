first_menu = True
while first_menu:
    # List of menu functions
    menu_1 = """
    List of menu functions

    Press:
    1. Phone book
    2. Messages
    3. Chat
    4. Call register
    5. Tones
    6. Settings
    7. Call divert
    8. Games
    9. Calculator
    10. Reminders
    11. Clock
    12. Profiles
    13. SIM services
    0. To switch off your phone
    """
    # 1 Phone book list
    phoneBook = """
    Phone book

    Press:
    1. Search
    2. Service Nos.
    3. Add name
    4. Erase
    5. Edit
    6. Assign tone
    7. Send b'card
    8. Option
    9. Speed dials
    10. Voice tags
    0. Back
    """
    # Number 8 under phonebook
    oPtions = """
    Options

    Press:
    1. Type of view
    2. Memory status
    0. Back
    """
    # 2 Messages list
    mEssages = """
    Messages

    Press:
    1. Write messages
    2. Inbox
    3. Outbox
    4. Picture messages
    5. Templates
    6. Smileys
    7. Message settings
    8. Info service
    9. Voice mailbox number
    10. Service command editor
    0. Back
    """
    # Number 7 under messages
    messagesSEttings = """
    Messsage settings

    Press:
    1. Set 1
    2. Common
    0. Back
    """
    # Set 1 under messages settings
    setOne = """
    Set 1

    Press:
    1. Message centre number
    2. Messages sent as
    3. Message validity
    0. Back
    """
    # Common under messages settings
    coMmon = """
    Common

    Press:
    1. Delivery reports
    2. Reply via same centre
    3. Character support
    0. Back
    """
    # 4 Call register list
    callRegister = """
    Call Register

    Press:
    1. Missed calls
    2. Received calls
    3. Dialled numbers
    4. Erase recent call lists
    5. Show call duration
    6. Show call cost
    7. Call cost settings
    8. Prepaid credit
    0. Back
    """
    # Show call duration under (Call register)
    showCallDuration = """
    Show call duration

    Press:
    1. Last call duration
    2. All calls' duration
    3. Received calls' duration
    4. Dialled calls' duration
    5. Clear timers
    0. Back
    """

    # Show call cost under (Call register)
    showCallCost = """
    Show call costs

    Press:
    1. Last call cost
    2. All calls' cost
    3. Clear counters
    0. Back
    """
    # Call cost settings under (Call register)
    callCostSettings = """
    Call cost settings

    Press:
    1. Call cost limit
    2. Show costs in
    0. Back
    """
    # 5 Tones list
    tOnes = """
    Tones

    Press:
    1. Ringing tones
    2. Ringing volume
    3. Incoming call alert
    4. Composer
    5. Message alert tone
    6. Keypad tones
    7. Warning and game tones
    8. Vibrating alert
    9. Screen saver
    0. Back
    """

    # 6 Settings
    sEttings = """
    Settings

    Press:
    1. Call settings
    2. Phone settings
    3. Security settings
    4. Restore factory settings
    0. Back
    """
    # Call settings under (Settings)
    callSettings = """
    Call settings

    Press:
    1. Automatic redial
    2. Speed dialling
    3. Call waiting options
    4. Own number sending
    5. Phone line in use
    6. Automatic answer
    0. Back
    """
    # Phone settings under (Settings)
    phoneSettings = """
    Phone settings

    Press:
    1. Language
    2. Cell info display
    3. Welcome note
    4. Network selection
    5. Lights
    6. Confirm SIM service actions
    0. Back
    """
    # Security settings under (Settings)
    securitySettings = """
    Security settings

    Press:
    1. PIN code request
    2. Call barring service
    3. Fixed dialling
    4. Closed user group
    5. Phone security
    6. Change access codes
    0. Back
    """
    # 11 Clock lists
    cLock = """
    Clock

    Press:
    1. Alarm clock
    2. Clock settings
    3. Date setting
    4. Stopwatch
    5. Countdown timer
    6. Auto update of date and time
    0. Back
    """

    # Starting point after variables declaration
    print(menu_1)
    menu = int(input("Press a number to make a selection between 1 - 13: "))
    print("Invalid input.")

    if menu >= 0 or menu <= 13:
         print("You entered an invalid option!! Kindly try again or press 0 to switch off your phone")
        

    match menu:
        case 1:
            phonebOOk = True
            while phonebOOk:
                print(phoneBook)
                phonebook = int(input("Press a number to make a selection: "))
                print("Invalid input. Enter a number.")

                match phonebook:
                    case 1:
                        print("Search")
                    case 2:
                        print("Service Nos.")
                    case 3:
                        print("Add name")
                    case 4:
                        print("Erase")
                    case 5:
                        print("Edit")
                    case 6:
                        print("Assign tone")
                    case 7:
                        print("Send b'card")
                    case 8:
                        opTION = True
                        while opTION:
                            print(oPtions)
                            options = int(input("Press a number to make a selection: "))
                            print("Invalid input. Please enter a number.")
 
                            match options:
                                case 1:
                                    print("Type of view")
                                case 2:
                                    print("Memory status")
                                case 0:
                                    opTION = False
                                case _:
                                    print("Invalid input")
                    case 9:
                        print("Speed dials")
                    case 10:
                        print("Voice tags")
                    case 0:
                        phonebOOk = False
                    case _:
                        print("Invalid input")

                if phonebook >= 0 or phonebook <= 10:
                    print("You entered an invalid option, kindly enter a positive selection")

        case 2:
            mESSages = True
            while mESSages:
                print(mEssages)
                messages = int(input("Press a number to make a selection: "))
                print("Invalid input. Enter a number.")

                match messages:
                    case 1:
                        print("Write messages")
                    case 2:
                        print("Inbox")
                    case 3:
                        print("Outbox")
                    case 4:
                        print("Picture messages")
                    case 5:
                        print("Templates")
                    case 6:
                        print("Smileys")
                    case 7:
                        mESSagessett = True
                        while mESSagessett:
                            print(messagesSEttings)
                            messagessettings = int(input("Press a number to make a selection: "))
                            print("Invalid input. Enter a number.")

                            match messagessettings:
                                case 1:
                                    print(setOne)
                                    setone = int(input("Press a number to make a selection: "))
                                    print("Invalid input. Enter a number.")
                                    match setone:
                                        case 1:
                                            print("Message centre number")
                                        case 2:
                                            print("Messages sent as")
                                        case 3:
                                            print("Message validity")
                                        case _:
                                            print("Invalid input")
                                case 2:
                                    print(coMmon)
                                    common = int(input("Press a number to make a selection: "))
                                    print("Invalid input. Enter a number.")
                                    match common:
                                        case 1:
                                            print("Delivery reports")
                                        case 2:
                                            print("Reply via same centre")
                                        case 3:
                                            print("Character support")
                                        case _:
                                            print("Invalid input")
                                case 0:
                                    mESSagessett = False
                                case _:
                                    print("Invalid input")
                    case 8:
                        print("Info service")
                    case 9:
                        print("Voice mailbox number")
                    case 10:
                        print("Service command editor")
                    case 0:
                        mESSages = False
                    case _:
                        print("Invalid input")

                if messages >= 0 or messages <= 10:
                    print("You entered an invalid option, kindly enter a positive selection")

        case 3:
            cHat = True
            while cHat:
                print("Chat ")
                chat = int(input(" Press 0 to return to the mainmenu: "))
                print("Invalid input. Please enter a number.")
 
                match chat:
                    case 0:
                        cHat = False
                    case _:
                        print("Invalid input")

        case 4:
            cALLreGister = True
            while cALLreGister:
                print(callRegister)
                callregister = int(input("Press a number to make a selection: "))
                print("Invalid input. Please enter a number.")

                match callregister:
                    case 1:
                        print("Missed calls")
                    case 2:
                        print("Received calls")
                    case 3:
                        print("Dialled numbers")
                    case 4:
                        print("Erase recent calls list")
                    case 5:
                        print(showCallDuration)
                        showcallduration = int(input("Press a number to make a selection: "))
                        print("Invalid input. Enter a number.")

                        match showcallduration:
                            case 1:
                                print("Last call cost")
                            case 2:
                                print("All calls' cost")
                            case 3:
                                print("Received calls' duration")
                            case 4:
                                print("Dialled calls' duration")
                            case 5:
                                print("Clear timers")
                            case _:
                                print("Invalid input")
                    case 6:
                        print(showCallCost)
                        showcallcost = int(input("Press a number to make a selection: "))
                        print("Invalid input. Enter a number.")

                        match showcallcost:
                            case 1:
                                print("Last call cost")
                            case 2:
                                print("All calls' cost")
                            case 3:
                                print("Clear counters")
                            case _:
                                print("Invalid input")
                    case 7:
                        print(callCostSettings)
                        callcostsettings = int(input("Press a number to make a selection: "))
                        print("Invalid input. Enter a number.")

                        match callcostsettings:
                            case 1:
                                print("Call cost limit")
                            case 2:
                                print("Show costs in")
                            case _:
                                print("Invalid input")
                    case 8:
                        print("Prepaid credit")
                    case 0:
                        cALLreGister = False
                    case _:
                        print("Invalid input")

        case 5:
            tONEs = True
            while tONEs:
                print(tOnes)
                tones = int(input("Press a number to make a selection: "))
                print("Invalid input. Enter a number.")

                match tones:
                    case 1:
                        print("Ringing tone")
                    case 2:
                        print("Ringing volume")
                    case 3:
                        print("Incoming call alert")
                    case 4:
                        print("Composer")
                    case 5:
                        print("Message alert tone")
                    case 6:
                        print("Keypad tones")
                    case 7:
                        print("Warning and game tones")
                    case 8:
                        print("Vibrating alert")
                    case 9:
                        print("Screen saver")
                    case 0:
                        tONEs = False
                    case _:
                        print("Invalid input")

        case 6:
            sETTing = True
            while sETTing:
                print(sEttings)
                settings = int(input("Press a number to make a selection: "))
                print("Invalid input. Please enter a number.")

                match settings:
                    case 1:
                        callsETTing = True
                        while callsETTing:
                            print(callSettings)
                            callsettings = int(input("Press a number to make a selection: "))
                            print("Invalid input. Enter a number.")

                            match callsettings:
                                case 1:
                                    print("Automatic redial")
                                case 2:
                                    print("Speed dialling")
                                case 3:
                                    print("Call waiting options")
                                case 4:
                                    print("Own number sending")
                                case 5:
                                    print("Phone line in use")
                                case 6:
                                    print("Automatic answer")
                                case 0:
                                    callsETTing = False
                                case _:
                                    print("Invalid input")
                    case 2:
                        print(phoneSettings)
                        phonesettings = int(input("Press a number to make a selection: "))
                        print("Invalid input. Enter a number.")

                        match phonesettings:
                            case 1:
                                print("Language")
                            case 2:
                                print("Cell info display")
                            case 3:
                                print("Welcome note")
                            case 4:
                                print("Network selection")
                            case 5:
                                print("Lights")
                            case 6:
                                print("Confirm SIM service actions")
                            case _:
                                print("Invalid input")
                    case 3:
                        print(securitySettings)
                        securitysettings = int(input("Press a number to make a selection: "))                            
                       print("Invalid input. Please enter a number.")
                            
                        match securitysettings:
                            case 1:
                                print("PIN code request")
                            case 2:
                                print("Call barring service")
                            case 3:
                                print("Fixed dialling")
                            case 4:
                                print("Closed user group")
                            case 5:
                                print("Phone security")
                            case 6:
                                print("Change access codes")
                            case _:
                                print("Invalid input")
                    case 4:
                        print("Restore factory settings")
                    case 0:
                        sETTing = False
                    case _:
                        print("Invalid input")

        case 7:
            dIVErt = True
            while dIVErt:
            print("Call divert")
            divert = int(input("Press 0 to return to the mainmenu: "))
            print("Invalid input. Please enter a number.")

                match divert:
                    case 0:
                        dIVErt = False
                    case _:
                        print("Invalid input")

        case 8:
            gAMes = True
            while gAMes:
                       print("Thanks for playing our Games")
                    games = int(input("Press 0 to return to the mainmenu: "))
                    print("Invalid input. Please enter a number.")

                match games:
                    case 0:
                        gAMes = False
                    case _:
                        print("Invalid input")

        case 9:
            cALculator = True
            while cALculator:
                print("Calculator")
                caLCUlator = int(input("Press 0 to return to the mainmenu: "))
                print("Invalid input. Please enter a number.")

                match caLCUlator:
                    case 0:
                        cALculator = False
                    case _:
                        print("Invalid input")

        case 10:
            rEMInders = True
            while rEMInders:
                print("Reminders")