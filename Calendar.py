import Meeting
import UI

WORKDAY_START = 9.00
WORKDAY_END = 18.00
ROOMS = frozenset((1, 2, 3, 4))
PARTICIPANTS = frozenset(('ME', 'CEO', 'MANAGER', 'HR', 'SECRETARY'))
MIN_PAR_PER_MEETING = 1


def check_time_overlap(meeting, new_meeting):
    if new_meeting[Meeting.START_TIME_IDX] >= meeting[Meeting.START_TIME_IDX] and\
    new_meeting[Meeting.START_TIME_IDX] < meeting[Meeting.END_TIME_IDX]:
        return True
    if new_meeting[Meeting.END_TIME_IDX] > meeting[Meeting.START_TIME_IDX] and\
    new_meeting[Meeting.END_TIME_IDX] <= meeting[Meeting.END_TIME_IDX]:
        return True
    if meeting[Meeting.START_TIME_IDX] >= new_meeting[Meeting.START_TIME_IDX] and\
    meeting[Meeting.END_TIME_IDX] <= new_meeting[Meeting.END_TIME_IDX]:
        return True 

    return False


def check_room_overlap(meeting, new_meeting):
    if new_meeting[Meeting.ROOM_IDX] == meeting[Meeting.ROOM_IDX]:
        return True
    return False


def check_pars_overlap(meeting, new_meeting):
    for participant in new_meeting[Meeting.PARTICIPANTS_IDX]:
        if participant in meeting[Meeting.PARTICIPANTS_IDX]:
            return True
    return False


def check_overlap(calendar, new_meeting):
    for meeting in calendar:
        if check_time_overlap(meeting, new_meeting):
            if check_room_overlap(meeting, new_meeting) or check_pars_overlap(meeting, new_meeting):
                return True
    return False


def add_meeting(calendar, new_meeting):
    if len(calendar) != 0:
        for i, meeting in enumerate(calendar):
            if meeting[Meeting.START_TIME_IDX] > new_meeting[Meeting.START_TIME_IDX]:
                calendar.insert(i, new_meeting)
                return calendar

    calendar.append(new_meeting)
    return calendar


def create_and_add(calendar):
    new_meeting = Meeting.create_meeting()

    if check_overlap(calendar, new_meeting):
        print("\nMeeting overlaps with an existing meeting.\n")
    else:
        add_meeting(calendar, new_meeting)
        print("Meeting added successfully.")
    
    return calendar


def find_meeting(calendar):
    start_time = UI.get_start_time()
    room_number = UI.get_room_number()
    idx = Meeting.search_meeting(calendar, start_time, room_number)
    if idx != -1:
        UI.print_meeting_info(calendar[idx])


def delete_meeting(calendar):
    start_time = UI.get_start_time()
    room_number = UI.get_room_number()
    idx = Meeting.search_meeting(calendar, start_time, room_number)
    if idx != -1:
        calendar.pop(idx)
        print("Meeting deleted")
    return calendar


def recommend_meeting(calendar):
    duration = UI.get_meeting_duration()
    pars_list = UI.get_participant_list()
    i = WORKDAY_START
    while i <= WORKDAY_END:
        for room in ROOMS:
            meeting = [i, i+duration, room, pars_list]
            if check_overlap(calendar, meeting):
                continue
            else:
                if UI.suggest_meeting(meeting):
                    add_meeting(calendar, meeting)
                    print("Meeting added successfully.")
                    return calendar
        i += 0.15
    
    return calendar


def save_calendar(calendar):
    file_name = UI.get_file_name()
    f = open(file_name, "a+")
    for meeting in calendar:
        print(meeting, file=f)
    f.close()


def load_calendar():
    try:
        calendar = []
        file_name = UI.get_file_name()
        f = open(file_name, "r")
        for line in f:
            meeting = line.split()
            add_meeting(calendar, meeting)
        f.close()
    except FileNotFoundError:
        print("ERROR: file not found.")
    return calendar


def print_calendar(calendar):
    print('\n')
    if len(calendar) == 0:
        print("Calendar empty.")
    else:
        for i, meeting in enumerate(calendar):
            print(i+1, end= ': ')
            UI.print_meeting_info(meeting)


def update_meeting(calendar):
    start_time = UI.get_start_time()
    room_number = UI.get_room_number()
    idx = Meeting.search_meeting(calendar, start_time, room_number)
    if idx == -1:
        return calendar
    old_meeting, new_meeting = calendar[idx].copy(), calendar[idx].copy()
    calendar.pop(idx)

    option = UI.what_to_update()
    if option == "start":
        new_start_time = UI.get_start_time()
        new_meeting[Meeting.START_TIME_IDX] = new_start_time

    elif option == "end":
        new_end_time = UI.get_end_time(old_meeting[Meeting.START_TIME_IDX])
        new_meeting[Meeting.END_TIME_IDX] = new_end_time

    elif option == "room":
        new_room = UI.get_room_number()
        new_meeting[Meeting.ROOM_IDX] = new_room

    elif option == "participants":
        new_pars_list = UI.get_participant_list()
        new_meeting[Meeting.PARTICIPANTS_IDX] = new_pars_list


    if check_overlap(calendar, new_meeting):
        add_meeting(calendar, old_meeting)
        print("\nMeeting overlaps with an existing meeting.\n")
    else:
        add_meeting(calendar, new_meeting)
        print("Meeting updated successfully.")
    
    
    return calendar