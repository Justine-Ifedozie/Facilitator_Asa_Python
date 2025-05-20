first_menu1 = True
while first_menu1: 


#List of menu functions
        first_menu = '''
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
        '''

        #1 Phone book list
        phone_book = """
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

        #Number 8 under phonebook
        first_options = """
        Options

        Press: 
        1. Type of view
        2. Memory status
        0. Back
        """

        #2 Messages list
        messages = """
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

        #Number 7 under messages
        messages_settings = """
        Messsage settings

        Press: 
        1. Set 1
        2. Common 
        0. Back
			"""

        #Set 1 under messages settings
        set_one = """
		Set 1

        Press: 
        1. Message centre number
        2. Messages sent as
        3. Message validity
        0. Back
			"""
        #Common under messages settings
        common = """
        Common

        Press: 
        1. Delivery reports
        2. Reply via same centre
        3. Character support
        0. Back
			"""
			
        #4 Call register list
        call_register = """
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
			#Show call duration under (Call register)
        show_call_duration = """
        Show call duration

        Press: 
        1. Last call duration
        2. All calls' duration
        3. Received calls' duration
        4. Dialled calls' duration
        5. Clear timers
        0. Back
			"""

        #Show call cost under (Call register)
        show_call_cost = """
        Show call costs

        Press: 
        1. Last call cost
        2. All calls' cost
        3. Clear counters
        0. Back
			"""			
			
        #Call cost settings under (Call register)
        call_cost_settings = """
        Call cost settings

        Press: 
        1. Call cost limit
        2. Show costs in
        0. Back
			"""
        #5 Tones list
        tones = """
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
			
        #6 Settings
        settings = """
        Settings

        Press: 
        1. Call settings
        2. Phone settings
        3. Security settings
        4. Restore factory settings
        0. Back
			"""
        #Call settings under (Settings)
        call_settings = """
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
        #Phone settings under (Settings)
        phone_settings = """
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
			
        #Security settings under (Settings)
        security_settings = """
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
        #11 Clock lists
        clock = """
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

#Starting point after variables declaration
			
        print(first_menu)
        menu = int(input("Press a number to make a selection between 1 - 13: "))
        
        if menu > 0 or menu < 13:
                print("You entered an invalid option!! Kindly try again or press 0 for pidgin")
                print("Press a number to make a selection between 1 - 13: ")
                menu = input("Press a number to make a selection between 1 - 13: ")
                
                
        match menu:
                case 1:
                        phone_books = True
                        while phone_books:
                                print(phone_book)
                                phonebook = input("Press a number to make a selection: ")
                
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
                                                        options1 = True
                                                        while options1:
                                                                
                                                                print(first_options)
                                                                option = input("Press a number to make a selection: ")

                                                                match option:
                                                                        case 1: print("Type of view")
                                                                                        #break
                                                                        case 2: print("Memory status") #break
                                                                                                #break
                                                                        case 0: options1 = False
                                                                                        #break
                                                                                        
                                                                                        
                                                                                        
                                                                                        







