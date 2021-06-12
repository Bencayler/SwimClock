import time
import datetime

'''
class SwimClock2:
    def __init__(self, lap_number, lap_time):
        self.__lap_time = lap_time
        self.__lap_number = lap_number

    def set_lap_time(self, lap_time):
        lap_time = lap_time

    def get_lap_time(self):
        return self.__lap_time

    def set_lap_number(self, lap_number):
        lap_number = lap_number

    def get_lap_number(self):
        return self.__lap_number
'''


def main():
    menu_choice = main_menu()
    if menu_choice == 1:
        stored_splits = interval_mode()
        post_swim_menu(stored_splits)
    if menu_choice == 2:
        stored_splits = rest_interval_mode()
        post_swim_menu(stored_splits)
    if menu_choice ==3:
        stored_splits = free_interval_mode()
        post_swim_menu(stored_splits)
    if menu_choice == 4:
        print('Exiting program now.')
        return


def main_menu():
    try:
        print('Enter the desired number for each menu option.')
        print('1. Interval mode')
        print('2. Rest-Interval mode')
        print('3. Free-Interval mode')
        print('4. Quit')
        selection = input('Make a selection: ')
        selection = int(selection)
        while selection <= 0 or selection > 4:
            print('Invalid input detected ')
            print('Try again: ')
            print('1. Interval mode')
            print('3. Free-Interval mode')
            print('4. Quit')
            selection = input('Make a selection: ')
            selection = int(selection)
        if selection == 1 or selection == 2 or selection == 3 \
                or selection == 4:
            return selection
    except ValueError:
        print('Float or empty entry detected. Try again.')
        main_menu()


def store_splits_option(stored_splits, difference, total, average):
    menu_choice = input('Do you want to store your splits? ( Y / N ) ')
    menu_choice = menu_choice.lower()
    if menu_choice != 'y':
        print('Very well.')
    if menu_choice == 'y':
        store_swim_times(stored_splits, difference, total, average)


def store_swim_times(stored_splits, difference, total, average):
    print('Writing time . . .')
    stored_file = open(r'C:\Users\THEJANKMACHINE\Desktop\swim_times.txt', 'w')
    stored_file.writelines('Lap Number | Lap Times\n')
    stored_file.writelines('-----------------------\n')
    for r in range(len(stored_splits)):
        stored_file.writelines(f'    {stored_splits[r][0]}\t{str(stored_splits[r][1])}\n')
    stored_file.writelines(f'Total time: {total}\n')
    stored_file.writelines(f'Average Split: {average}\n')
    stored_file.writelines(f'The change in time between the fastest and slowest lap is:'
                           f' {difference}\n')
    stored_file.close()
    print('Times written successfully.')


def free_interval_mode():
    stored_splits = []
    current_lap = 0
    continued = ''
    while continued == '':
        today = datetime.datetime.today()
        continued = input('Enter any input to end session: ')
        future = datetime.datetime.today()
        split = future - today
        current_lap += 1
        print(f'{current_lap} | {split}')
        interior_splits = [current_lap, split]
        stored_splits.append(interior_splits)
    return stored_splits


def interval_mode():
    stored_splits = []
    current_lap = 0
    desired_interval_number = int(input('Enter desired amount of laps: '))
    desired_distance = desired_interval_number * 50
    print(f'Distance: {desired_distance} yards / meters')
    desired_interval_rate = int(input('Enter desired interval '
                                      'rate in seconds: '))
    input('Press enter to begin')
    while current_lap < desired_interval_number:
        today = datetime.datetime.today()
        input('Hit enter to log a split: ')
        future = datetime.datetime.today()
        split = future - today
        current_lap += 1


def rest_interval_mode():
    stored_splits = []
    current_lap = 0
    desired_lap_number = int(input('Enter desired amount of laps: '))
    desired_distance = desired_lap_number * 50
    print(f'Distance: {desired_distance} yards / meters')
    desired_rest_rate = int(input('Entered desired rest period in seconds: '))
    input('Press enter to begin')
    while current_lap < desired_lap_number:
        today = datetime.datetime.today()
        input('Hit enter to end a split desired split: ')
        future = datetime.datetime.today()
        split = future - today
        current_lap += 1
        print(f'{current_lap} | {split}')
        for i in range(desired_rest_rate, 0, -1):
            time.sleep(1)
            print(i)
        if current_lap < (desired_lap_number - 1):
            print('Go')

        interior_splits = [current_lap, split]
        stored_splits.append(interior_splits)
    return stored_splits


def post_swim_menu(stored_splits):
    try:
        menu_choice = input('Do you want to display your splits? ( Y / N ) ')
        menu_choice = menu_choice.lower()
        if menu_choice == 'y':
            display_swim_times(stored_splits)
        elif menu_choice == 'n':
            print('Returning to main menu . . .')
            main_menu()
        else:
            print('Invalid input detected.')
            post_swim_menu(stored_splits)
    except ValueError:
        print('Float or empty entry detected. Try again.')
        post_swim_menu(stored_splits)


def display_swim_times(stored_splits):
    try:
        print('Display Options: ')
        print('1. Chronological')
        print('2. Fastest to Slowest ')
        print('3. Slowest to Fastest')
        print('4. Exit')
        menu_choice = input('Enter option: ')
        menu_choice = int(menu_choice)
        while menu_choice < 1 or menu_choice > 4:
            menu_choice = input('Please enter valid menu option.')
        if menu_choice == 1:
            display_chronological(stored_splits)
        if menu_choice == 2:
            display_fastest_slowest(stored_splits)
        if menu_choice == 3:
            display_slowest_fastest(stored_splits)
        if menu_choice == 4:
            print('Returning to main menu: ')
            main_menu()
    except ValueError:
        print('Float or empty entry detected. Try again.')
        display_swim_times(stored_splits)


def display_chronological(stored_splits):
    total = datetime.timedelta(seconds=0)
    for r in range(len(stored_splits)):
        total += stored_splits[r][1]
    average = total / len(stored_splits)
    print('Lap Number | Lap Times')
    print('-----------------------')
    for r in range(len(stored_splits)):
        print(f'\t{stored_splits[r][0]}\t\t{(str(stored_splits[r][1]))}')
    print(f'\nTotal time: {total}')
    print(f'Average Split: {average}')
    stored_splitsV2 = sorted(stored_splits, key=lambda x: x[1])
    print(f'Fastest Lap / Time: {stored_splitsV2[0][0]}\t{stored_splitsV2[0][1]}')
    print(f'Slowest Lap / Time: {stored_splitsV2[len(stored_splitsV2) - 1][0]}',
          f'{stored_splitsV2[len(stored_splitsV2) - 1][1]}')
    difference = stored_splitsV2[len(stored_splitsV2) - 1][1] - stored_splitsV2[0][1]
    print(f'The change in time between the fastest and slowest lap is:'
          f' {difference}')
    store_splits_option(stored_splits, difference, total, average)


def display_fastest_slowest(stored_splits):
    total = datetime.timedelta(seconds=0)
    stored_splits = sorted(stored_splits, key=lambda x: x[1])
    print('Lap Number | Lap Times')
    print('-----------------------')
    for r in range(len(stored_splits)):
        total += stored_splits[r][1]
        print(f'\t{stored_splits[r][0]}\t\t{(str(stored_splits[r][1]))}')
    average = total / len(stored_splits)
    print(f'\nTotal time: {total}')
    print(f'Average Split: {average}')
    difference = stored_splits[len(stored_splits) - 1][1] - stored_splits[0][1]
    print(f'The change in time between the fastest and slowest lap is:'
          f' {difference}')
    store_splits_option(stored_splits, difference, total, average)


def display_slowest_fastest(stored_splits):
    total = datetime.timedelta(seconds=0)
    stored_splits = sorted(stored_splits, key=lambda x: x[1], reverse=True)
    print('Lap Number | Lap Times')
    print('-----------------------')
    for r in range(len(stored_splits)):
        total += stored_splits[r][1]
        print(f'\t{stored_splits[r][0]}\t\t{(str(stored_splits[r][1]))}')
    average = total / len(stored_splits)
    print(f'\nTotal time: {total}')
    print(f'Average Split: {average}')
    difference = stored_splits[0][1] - stored_splits[len(stored_splits) - 1][1]
    print(f'The change in time between the fastest and slowest lap is:'
          f' {difference}')
    store_splits_option(stored_splits, difference, total, average)


if __name__ == '__main__':
    main()