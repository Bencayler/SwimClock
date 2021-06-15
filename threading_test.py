import time
import threading
import concurrent.futures

start = time.perf_counter()



def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     f1 = executor.submit(do_something, 1)
#     f2 = executor.submit(do_something, 1)
    
#     print(f1.result()) # Printing the returned value of the do_something function
#     print(f2.result())

# Using a loop to run this 10 times
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = [executor.submit(do_something, sec) for sec in secs]
    # Use another function to from the concurent futures to receive the output of results
    for f in concurrent.futures.as_completed(results):
        print(f.result())



# def do_something():
#     print('Sleeping 1 second...')
#     time.sleep(1)
#     print('Done Sleeping...')

# do_something()
# Run it twice and it takes 2 seconds
# do_something()

# Turn them into threads
# t1 = threading.Thread(target=do_something) # Pass in the function name but don't execute it by adding parenthesis
# t2 = threading.Thread(target=do_something)
# Created two thread objects, but not running the code
# If ran like this it would complete in 0.0 seconds

# Use the start method for each thread
# This would only begin the scripts and then move on to the next lines, hence the completed in 0.0 seconds on the output of the last line
# t1.start()
# t2.start()

# Use the join method to combine the thread objects
# t1.join()
# t2.join()
# They're both joined so run microseconds a part so it completes in 1.0 seconds
# # Create a for loop to run several threads at once
# threads = []
# for i in range(10):
#     t = threading.Thread(target=do_something, args=[1.7]) # use args for the arguments
#     t.start()
#     threads.append(t)
# # Now join all the indexes in the list
# for thread in threads:
#     thread.join()


finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')