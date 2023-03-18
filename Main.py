import Calendar


if __name__ == "__main__":
    calendar = []
    while True:
        option = int(input("\nWhat would you like to do?\n1. Add new meeting.\n2. Search for a meeting.\n\
3. Delete a meeting.\n4. Get time and room recommendation.\n5. Save calendar to a file.\n\
6. Load calendar from a file.\n7. Print calendar\n8. Update an existing meeting.\n9. Exit\n"))
        if option == 1:
            Calendar.create_and_add(calendar)
        elif option == 2:
            Calendar.find_meeting(calendar)
        elif option == 3:
            Calendar.delete_meeting(calendar)
        elif option == 4:
            Calendar.recommend_meeting(calendar)
        elif option == 5:
            Calendar.save_calendar(calendar)
        elif option == 6:
            Calendar.print_calendar(Calendar.load_calendar())
        elif option == 7:
            Calendar.print_calendar(calendar)
        elif option == 8:
            Calendar.update_meeting(calendar)
        elif option == 9:
            break