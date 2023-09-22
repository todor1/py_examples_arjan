#%% 
# # https://superfastpython.com/benchmark-stopwatch-timer/
# custom stopwatch timer class
from time import time

class StopwatchTimer(object):
    '''
        To start the timer we create an instance and call the start() method:
        ...
        # create the timer
        timer = StopwatchTimer()
        # start the timer
        timer.start()
        To stop the timer, we call the stop() method:
        ...
        # stop the timer
        timer.stop()
        Then, if we want to report the duration, we can call the duration() method and print the result:
        ...
        # report the duration
        print(timer.duration())
        The timer could be reused by calling start() and stop() again in the same order. This will overwrite the internal state and stop time attributes correctly.

        This timer cannot be resumed again if stopped.
    '''
    # start the timer
    def start(self):
        self.time_start = time()
    # stop the timer
    def stop(self):
        self.time_end = time()
    # get the duration
    def duration(self):
        return self.time_end - self.time_start
    
    
    
# custom stopwatch timer class that can be resumed
class ResumeStopwatchTimer(object):
    '''
        We can then create the timer and call the start() method to start the timer.
        ...
        # create the timer
        timer = ResumeStopwatchTimer()
        # start the timer
        timer.start()
        The timer can then be stopped and started again, then stopped.
        ...
        # stop the timer
        timer.stop()
        # ...
        # start the timer
        timer.start()
        ...
        # stop the timer
        timer.stop()
        Finally, we can retrieve and report the overall duration of all start-stop pairs and reset the timer for reuse.
        ...
        # report the duration
        print(timer.duration())
        # reset the timer
        timer.reset()
    '''
    # constructor
    def __init__(self):
        self.reset()
    # start or resume the timer
    def start(self):
        self.time_start = time()
    # stop the timer
    def stop(self):
        self.sum_duration += time() - self.time_start
    # get the duration
    def duration(self):
        return self.sum_duration
    # reset the timer
    def reset(self):
        self.sum_duration = 0

#%%
# example of a custom stopwatch timer class
# SuperFastPython.com
from time import time
 
# custom stopwatch timer class
class StopwatchTimer(object):
    # start the timer
    def start(self):
        self.time_start = time()
    # stop the timer
    def stop(self):
        self.time_end = time()
    # get the duration
    def duration(self):
        return self.time_end - self.time_start
 
# create the timer
timer = StopwatchTimer()
# start the timer
timer.start()
# create a list of squared numbers
result = [i*i for i in range(100_000_000)]
# stop the timer
timer.stop()
# report the duration
print(f'Took {timer.duration():.5f} seconds')

# %%
# example of a custom stopwatch timer class with resume support
# SuperFastPython.com
from time import time
 
# custom stopwatch timer class that can be resumed
class ResumeStopwatchTimer(object):
    # constructor
    def __init__(self):
        self.reset()
    # start or resume the timer
    def start(self):
        self.time_start = time()
    # stop the timer
    def stop(self):
        self.sum_duration += time() - self.time_start
    # get the duration
    def duration(self):
        return self.sum_duration
    # reset the timer
    def reset(self):
        self.sum_duration = 0
 
# create the timer
timer = ResumeStopwatchTimer()
# start the timer
timer.start()
# create a list of squared numbers
result = [i*i for i in range(100_000_000)]
# stop the timer
timer.stop()
# report the duration
print(f'Took {timer.duration():.5f} seconds')
# resume the timer
timer.start()
# do some more work
result = [i*i for i in range(100_000_000)]
# stop the timer
timer.stop()
# report the duration
print(f'Took {timer.duration():.5f} seconds')

# %%
