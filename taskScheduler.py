# ### Round 1 Technical

# You are given a list of tasks defined as (id, queue_time, task_duration)

# We want to get the sequence of tasks outputted via their id

# The list of tasks are defined as tuples and is passed into your function as an array of tuples

# The order is which you are scheduling the task is determined by the task_duration time

# each queue_time and task_duration represent units **t** of time

# Basically we’ll find the first task that can be queued - this is the queue time that starts closest to t = 0

# we’ll also want a way to get the task duration with the shortest time easily from the list (thus as the queue time for a task comes along - meaning the queue time of that task y ≤ t ( meaning the time t has past the queue time of the task and thus we can queue it)

# To do this we’ll want to use a min heap that stores the tuples based off of their task duration time

# basically we’ll want to iteratively add the tasks to the queue

# we also need to determine the first task that can be queued
# this is the task with the earliest queue time or closest to time = 0
# we can do this by sorting the tasks by queue time
# is there another way to do this?

# we want to add the tasks to the queue only if the time t is greater than or equal to the queue time of the task

# after a task is popped we want to move the time forward by the task duration
# we want to add the task id to the result list

# we want to repeat this process until all tasks are processed

# we want to return the result list


import heapq
from typing import List, Tuple


def taskScheduler(tasks: List[Tuple[str, int, int]]) -> List[str]:

    result = []
    task_heap = []
    time = 0
    tasks.sort(key=lambda x: x[1])
    task_idx = 0

    while task_idx < len(tasks) or task_heap:

        while task_idx < len(tasks) and tasks[task_idx][1] <= time:
            heapq.heappush(
                task_heap, (tasks[task_idx][2], tasks[task_idx][0], tasks[task_idx][1])
            )
            # task_duration, task_id, task_queue_time
            task_idx += 1

        if task_heap:
            duration, task_id, queue_time = heapq.heappop(task_heap)
            result.append(task_id)
            time += duration
        else:
            time = tasks[task_idx][1]

    return result


if __name__ == "__main__":
    # Test 1: Normal case
    tasks1 = [("A", 0, 3), ("B", 1, 2), ("C", 2, 1)]
    print(taskScheduler(tasks1))  # Expected: ["A", "C", "B"]

    # Test 2: Idle time case
    tasks2 = [("A", 0, 1), ("B", 10, 2)]
    print(taskScheduler(tasks2))  # Expected: ["A", "B"]

    # Test 3: All available at same time
    tasks3 = [("A", 0, 5), ("B", 0, 2), ("C", 0, 1)]
    print(taskScheduler(tasks3))  # Expected: ["C", "B", "A"]
