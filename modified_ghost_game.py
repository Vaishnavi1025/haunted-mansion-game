import random

MAX_HEALTH = 100
WIN_KEYS = 3

health = MAX_HEALTH
keys = 0

name = input("Enter your name: ")
print(f"Welcome {name}! You are trapped in a haunted mansion.")
print(f"Find {WIN_KEYS} keys and stay alive to escape.\n")

def show_status():
    global health, keys
    print(f"\nHealth: {health} | Keys: {keys}")
    if health > 70:
        print("You feel strong and confident.")
    elif health > 30:
        print("You are hurt but can continue.")
    else:
        print("You are very weak. One more big hit might kill you!")

while True:
    if health <= 0:
        print("\nYour health reached 0. The ghosts drag you into the darkness...")
        print("GAME OVER!")
        break

    if keys >= WIN_KEYS:
        print("\nYou collected enough keys and found the main gate!")
        print("You unlock the gate and escape the haunted mansion!")
        print("YOU WIN!")
        break

    show_status()
    start = input("\nWhere do you want to go? (gate/hall/garden/q to quit): ").lower().strip()

    if start == 'q':
        print("You chose to escape the game. Maybe next time you'll face the ghosts!")
        break

    elif start == 'gate':
        choice = input("At the gate. Move (right/left/forward): ").lower().strip()

        if choice == 'right':
            if random.random() > 0.5:
                keys += 1
                print("You searched the bushes and found a rusty key!")
            else:
                health -= 10
                print("A hidden spider bit you! You lose 10 health.")

        elif choice == 'left':
            sub = input("You see a broken mirror. (see/escape): ").lower().strip()
            if sub == 'see':
                health -= 15
                print("A ghost appears in the reflection and attacks you! -15 health.")
            else:
                print("You wisely avoid the mirror and walk away safely.")

        elif choice == 'forward':
            sub = input("It is very dark. Try to find a torch (right/left): ").lower().strip()
            if sub == 'right':
                if random.random() > 0.7:
                    health = 0
                    print("A shadowy ghost grabs you in the dark. You are dead!")
                else:
                    keys += 1
                    print("You find a torch and also a key on the floor!")
            else:
                print("You move carefully and stay safe, but find nothing.")

        else:
            print("That direction doesn't exist at the gate.")

    elif start == 'hall':
        choice = input("You enter the hall. Move (right/left): ").lower().strip()

        if choice == 'left':
            if random.random() > 0.6:
                keys += 1
                print("Behind an old painting, you discover a key!")
            else:
                health -= 10
                print("A snake hidden under a carpet bites you! -10 health.")

        elif choice == 'right':
            door = input("You find a secret door. (enter/back): ").lower().strip()
            if door == 'enter':
                if random.random() > 0.5:
                    health -= 20
                    print("Zombies attack you in the room! -20 health.")
                else:
                    keys += 1
                    print("You find a glowing key on a table and escape quickly!")
            else:
                print("You step back carefully and avoid the danger.")

        else:
            print("You bump into a wall. Choose left or right only.")

    elif start == 'garden':
        choice = input("You walk into the garden. Move (right/left): ").lower().strip()

        if choice == 'right':
            if random.random() > 0.4:
                keys += 1
                print("Under a stone near a tree, you find a key!")
            else:
                health -= 20
                print("Thorny ghost vines wrap around you! -20 health.")
        elif choice == 'left':
            health = 0
            print("A powerful garden ghost appears and finishes you instantly!")
        else:
            print("You wander around but find nothing this way.")

    else:
        print("Choose a valid place: gate, hall, garden, or q.")
