import time
import datetime

def interval_mode():
    stored_splits = []
    current_lap = 0
    desired_interval_number = int(input('Enter desired amount of laps: '))
    desired_distance = desired_interval_number * 50
    print(f'Distance: {desired_distance} yards / meters')
    desired_interval_rate = int(input('Enter desired interval '
                                      'rate in seconds: '))
    desired_interval_rate = datetime.timedelta(seconds=desired_interval_rate)
    input('Press enter to begin')
    while current_lap < desired_interval_number:
        today = datetime.datetime.today()
        input('Hit enter to end a split desired split: ')
        future = datetime.datetime.today()
        split = future - today
        current_lap += 1
        print(f'{current_lap} | {split}')
        countdown = desired_interval_rate - split
        countdown = int(countdown.seconds)
        if current_lap < (desired_interval_number):
            for i in range(countdown, 0, -1):
                time.sleep(1)
                print(i)
            print('Go')
        interior_splits = [current_lap, split]
        stored_splits.append(interior_splits)
    return stored_splits

interval_mode()

# def interval_mode_countdown():
#     current_lap = 0
#     desired_interval_number = int(input('Enter desired amount of laps: '))
#     desired_distance = desired_interval_number * 50
#     print(f'Distance: {desired_distance} yards / meters')
#     desired_interval_rate = int(input('Enter desired interval '
#                                       'rate in seconds: '))
#     input('Press enter to begin')
#     while current_lap < desired_interval_number:
#         for i in range(desired_interval_rate, 10, -1):
#             time.sleep(1)
#         for i in range(10, 0, -1):
#             time.sleep(1)
#             print(i)
#         print('GO!')
#         current_lap += 1

# def interval_mode_receive_times():
#     stored_splits = []
#     today = datetime.datetime.today()
#     input('Hit enter to end a split desired split: ')
#     future = datetime.datetime.today()
#     split = future - today
#     print(split)