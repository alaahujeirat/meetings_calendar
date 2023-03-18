import UI


START_TIME_IDX = 0
END_TIME_IDX = 1
ROOM_IDX = 2
PARTICIPANTS_IDX = 3


def create_meeting():
    meeting = []
    start_time = UI.get_start_time()
    meeting.append(start_time)
    meeting.append(UI.get_end_time(start_time))
    meeting.append(UI.get_room_number())
    meeting.append(UI.get_participant_list())
    return meeting


def search_meeting(calendar, start_Time, room):
    for i, meeting in enumerate(calendar):
        if meeting[START_TIME_IDX] == start_Time:
            if meeting[ROOM_IDX] == room:
                return i
        
    print("Meeting doesn't exist.")
    return -1


