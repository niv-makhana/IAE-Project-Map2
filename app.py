import streamlit as st
st.title("Project IAE Map by Sadhana and Niveditha")
st.write("Computer Science")

def get_directions(start_room_input, destination_input):

    start_room = int(start_room_input)
    destination_input = destination_input.strip()

    # 13-15, 17-23, 10, and 25 blocked off as it is TCT and not for public use.
    science = [24, 27, 29, 30, 31, 26, 28, 32, 34, 35]
    commons = [2, 39, 33, 36]
    art = [16]
    main = [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 39, 40, 41, 42]
    music = [36, 37, 38]
    science_cut = [34, 35]
    tct = [13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 25]

    room = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 16, 24, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 17]


    # Fixed string-to-number conversion
    if destination_input.lower() in ["gym"]:
        destination = 39
    elif destination_input.lower() in ["cafeteria", "cafe"]:
        destination = 40
    elif destination_input.lower() in ["stage"]:
        destination = 41
    elif destination_input.lower() in ["office", "main office", "mr.griffin office", "mrs. naus office"]:
        destination = 42
    elif destination_input.lower() in ["media center", "media"]:
        destination = 17
    else:
        try:
            destination = int(destination_input)
        except ValueError:
            st.write("Invalid destination entered. Please enter a valid room number or name.")
            return

    st.write(" ")

    # Check for TCT restricted areas
    if start_room in tct or destination in tct:
        st.write("That room is in TCT and not for public use.")
        return

    if destination == start_room:
        st.write("You are already at your destination!!!")
        return

    # Turning onto the art hallway from science/main
    if destination in main:
        st.write("Your destination is in this hallway.")
    else:
        if start_room in main and start_room not in art:
            st.write("Head to end of hallway and turn right.")
        elif start_room in science and destination in art:
            st.write("Head to end of hallway and turn left.")

    # Turning onto the science hallway from art/music/commons
    if destination in art:
        st.write("Your destination is in this hallway.")
    elif destination in science and destination in room:
        if start_room in art:
            st.write("Turn right onto the science hallway.")
        elif start_room in commons:
            st.write("Turn left onto the science hallway.")
        elif start_room in music:
            st.write("Turn left from the music hallway and turn right onto the science hallway.")
        elif start_room in science_cut:
            st.write("Continue straight into the opposite hallway.")

    # Turning onto the commons hallway
    if destination in science_cut or destination in science:
        st.write("Your destination is in this hallway. If you are in rooms 34 or 35, continue to the opposite hallway.")
    elif start_room in science and destination not in [33, 36]:
        st.write("Turn right onto commons hallway.")
    elif start_room in music:
        st.write("Turn left onto commons hallway after the lockers.")
    elif start_room in science_cut and (destination in music or destination in [33, 36]):
        st.write("Turn right onto the commons hallway.")
    elif start_room in science_cut and destination not in [33, 36]:
        st.write("Turn left onto the commons hallway.")
    elif start_room in science and (destination in music or destination in [33, 36]):
        st.write("Turn left onto commons hallway.")
    elif start_room in commons:
        if destination in science:
            st.write("Head down hallway and turn left onto science hallway.")

    # Turning onto the music hallway
    if destination in commons:
        st.write("You are on the end hallway!")
    elif destination in music:
        st.write("At rm 36, turn right after the lockers onto the music hallway.")

    # Turning onto main hallway
    if start_room in main:
        st.write("Your destination is in this hallway.")
    elif start_room in art and destination in main:
        st.write("Turn left onto the main hallway.")
    elif start_room in commons:
        if start_room == 33:
            st.write("Facing the lockers, turn right and continue past the gym.")
            if destination in [1, 40, 41, 42, 39, 911]:
                st.write("Turn left onto the main hallway.")
            elif destination not in [1, 39, 40, 41, 42, 911] and destination in main:
                st.write("Turn right onto the main hallway for classrooms.")
        if start_room == 36:
            st.write("Head straight down the hallway.")
            if destination in [1, 40, 41, 42, 39, 911]:
                st.write("Turn left onto the main hallway.")
            elif destination not in [1, 39, 40, 41, 42, 911] and destination in main:
                st.write("Turn right onto the main hallway for classrooms.")

    if start_room in [2, 39]:
        if destination in [1, 40, 41, 42, 39, 911] and destination in main:
            st.write("Turn left onto the main hallway.")
        elif destination not in [1, 39, 40, 41, 42, 911] and destination in main:
            st.write("Turn right onto the main hallway for classrooms.")

    # Room side determination
    if destination % 2 == 0 and (destination in science or destination in main) and start_room not in commons:
        st.write("Your room will be found on the right side of the hallway! Look at the numbers on the side of the doors or on top.")
    elif destination in music or destination in science_cut:
        st.write("Your room will be on your left! Room numbers are on the top.")
    elif destination % 2 == 1 and (destination in main or destination in science) and start_room not in commons:
        st.write("Your room will be found on the left! Look at the room numbers.")
    elif destination == 16:
        st.write("Your room (16) is on the right side! Yay!")
    elif destination == 17:
        st.write("Your room (17) is on the left side! Congrats!")
    elif destination == 39:
        st.write("Your end room is the gym! Go down the hallway and your room is next to the trophy case.")


# UI elements for user inputs
start_room_input = st.number_input("Where are you starting from?", min_value=1, step=1)
destination_input = st.text_input("Where do you want to go?")

if st.button("Get Directions"):
    if destination_input:
        get_directions(int(start_room_input), destination_input)
    else:
        st.warning("Please enter a destination!")
