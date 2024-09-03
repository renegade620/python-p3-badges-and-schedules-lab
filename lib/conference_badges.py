def badge_maker(name):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
    badges = []
    for name in names:
        list_badges = f"Hello, my name is {name}."
        badges.append(list_badges)
    return badges

def assign_rooms(names):
    room_assignments = []
    for i, name in enumerate(names, 1):
        room = f"Hello, {name}! You'll be assigned to room {i}!"
        room_assignments.append(room)
    return room_assignments

def printer(names):
    badges = batch_badge_creator(names)
    room_assignments = assign_rooms(names)

    for badge in badges:
        print(badge)

    for assignment in room_assignments:
        print(assignment)
    return None
