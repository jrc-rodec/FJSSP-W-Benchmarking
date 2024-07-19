import numpy as np

def makespan(start_times : list[int], machine_assignments : list[int], worker_assignments : list[int], durations : list[list[list[int]]]) -> float:
    # NOTE: assume first operation to start at t = 0
    return np.max([start_times[i] + durations[i][machine_assignments[i]][worker_assignments[i]] for i in range(len(start_times))])

def workload_balance(machine_assignments : list[int], worker_assignments : list[int], durations : list[list[list[int]]]) -> float:
    n_workers = max(worker_assignments)
    working_time = [0] * n_workers
    for i in range(len(worker_assignments)):
        working_time[worker_assignments[i]] += durations[i][machine_assignments[i]][worker_assignments[i]]
    mean_working_time = np.mean(working_time)
    result = 0.0
    for i in range(len(working_time)):
        result += np.pow((mean_working_time - working_time), 2)
    return result