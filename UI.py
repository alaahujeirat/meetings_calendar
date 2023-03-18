import Calendar
import Meeting


def get_start_time():
    try:
        while True:
            start_time = float(input("Please enter the start time of the meeting.\n\
(Note: must be between 9.00 and 18.00): "))
            if start_time >= Calendar.WORKDAY_START and start_time < Calendar.WORKDAY_END:
                break
            print("\nIllegal input. Try again\n")
    except ValueError:
        print("ERROR: Invalid input")

    return start_time


def get_end_time(start_time):
    try:
        while True:
            while True:
                end_time = float(input("\nPlease enter the end time of the meeting.\n\
(Note: must be between 9.00 and 18.00): "))
                if end_time > Calendar.WORKDAY_START and end_time <= Calendar.WORKDAY_END:
                    break
                print("\nIllegal input. Try again\n")
                
            if end_time - start_time >= 0.15:
                break
            else:
                print("\nMeeting duration must be at least 15 minutes. Try again.\n")
    except ValueError:
        print("ERROR: Invalid input")

    return end_time


def get_room_number():
    print('\n')
    try:    
        while True:
            print(Calendar.ROOMS)
            room = int(input("Please choose the room of the meeting.\n\
(Note: must be from the list above): "))
            if room in Calendar.ROOMS:
                break
            print("\nIllegal input. Try again\n")

    except ValueError:
        print("ERROR: Invalid input")
    
    return room


def get_participant_list():
    print('\n')
    par_list = []
    try:
        print(Calendar.PARTICIPANTS)
        par = input("Who's participating in the meeting?\n\
(Note: must be at least one): ")
        par = par.upper()
        if par not in Calendar.PARTICIPANTS:
            print("\nIllegal input.\n")
        else:
            par_list.append(par)
        while True:
            status = input("\nAnyone else? y/n ")
            if status == 'n':
                break
            print(Calendar.PARTICIPANTS)
            par = input("Who's participating in the meeting? ")
            par = par.upper()
            if par not in Calendar.PARTICIPANTS:
                print("\nIllegal input.\n")
                continue
            par_list.append(par)
    except ValueError:
        print("ERROR: Invalid input")
    
    return list(par_list)


def get_meeting_duration():
    print('\n')
    while True:
        meeting_duration = float(input("Enter the duration of the meeting: "))
        if meeting_duration >= 0.15:
            return meeting_duration
        print("\nMeeting duration is shorter than 15 minutes. Try again.\n")


def print_meeting_info(meeting):
    (print("Start time: {:2.2f} End time: {:2.2f} Room number: {} Participants: {}"
        .format(meeting[Meeting.START_TIME_IDX], meeting[Meeting.END_TIME_IDX], meeting[Meeting.ROOM_IDX],
        meeting[Meeting.PARTICIPANTS_IDX])))


def suggest_meeting(meeting):
    print_meeting_info(meeting)
    answer = input("Would you like to book this meeting? y/n ")
    if answer == 'y': return True
    else: return False


def get_file_name():
    return input("Enter name of file: ")


def what_to_update():
    option = int(input("What would you like to update?\n1. Start time.\n2. End time.\n3. Room.\n\
4. Participants.\n"))
    if option == 1:
        return "start"
    elif option == 2:
        return "end"
    elif option == 3:
        return "room"
    elif option == 4:
        return "participants"