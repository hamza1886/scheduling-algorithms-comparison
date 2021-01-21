import json
from statistics import mean
from typing import List, Dict


class SchedulingAlgorithm:
    _timeline = 0
    _average_time = {}

    def __init__(self, dataset: List[Dict]):
        self._dataset: List[Dict] = dataset

    def _non_preemptive_execution(self):
        self._timeline = 0

        for i, p in enumerate(self._dataset):
            self._dataset[i].update({'response_time': self._timeline})
            self._dataset[i].update({'waiting_time': self._timeline})

            self._timeline += p['burst_time']
            self._dataset[i].update({'turnaround_time': self._timeline})

        self._average_time = {
            'response_time': mean([t['response_time'] for t in self._dataset]),
            'waiting_time': mean([t['waiting_time'] for t in self._dataset]),
            'turnaround_time': mean([t['turnaround_time'] for t in self._dataset]),
        }

        return sorted(self._dataset, key=lambda t: t['process']), self._average_time

    def first_come_first_serve(self):
        self._dataset = sorted(self._dataset, key=lambda t: t['arrival_time'])
        return self._non_preemptive_execution()

    def shortest_job_first(self):
        self._dataset = sorted(self._dataset, key=lambda t: (t['arrival_time'], t['burst_time']))
        return self._non_preemptive_execution()

    def priority_scheduling(self):
        self._dataset = sorted(self._dataset, key=lambda t: (t['arrival_time'], t['priority']))
        return self._non_preemptive_execution()

    def round_robin(self, time_quantum: int = 4):
        self._timeline = 0
        self._dataset = sorted(self._dataset, key=lambda t: t['arrival_time'])

        process_list = [p['burst_time'] for p in self._dataset]

        while max(process_list) != 0:
            print('while')

            for i, p in enumerate(process_list):
                print('for', process_list)

                # current process has not arrived in ready queue yet!
                if self._dataset[i]['arrival_time'] <= self._timeline:
                    continue

                print(1)
                # current process is complete
                if process_list[i] == 0:
                    continue

                print(2)
                # initialize response_time of current process
                if not ('response_time' in self._dataset[i]):
                    self._dataset[i].update({'response_time': self._timeline})

                print(3)
                # initialize waiting_time of current process
                if not ('waiting_time' in self._dataset[i]):
                    self._dataset[i].update({'waiting_time': self._timeline - self._dataset[i]['arrival_time']})

                print(f"processing {self._dataset[i]['process']}: ", end='')

                # execute current process for a maximum time of time_quantum
                time_delta = time_quantum if process_list[i] >= time_quantum else process_list[i]
                process_list[i] -= time_delta

                # add time_delta to turnaround_time of this process
                self._dataset[i].update({'turnaround_time': time_delta})
                # add time_delta to waiting_time of other (incomplete) processes
                for _i, _p in enumerate(process_list):
                    if i != _i and process_list[i] > 0:
                        self._dataset[i].update({'waiting_time': time_delta})

                # increment time_delta
                self._timeline += time_delta

                print(f' {time_delta} time')

        self._average_time = {
            'response_time': mean([t['response_time'] for t in self._dataset]),
            'waiting_time': mean([t['waiting_time'] for t in self._dataset]),
            'turnaround_time': mean([t['turnaround_time'] for t in self._dataset]),
        }

        return sorted(self._dataset, key=lambda t: t['process']), self._average_time


if __name__ == '__main__':
    dataset1 = [
        {'process': 'P1', 'burst_time': 24, 'arrival_time': 0},
        {'process': 'P2', 'burst_time': 3, 'arrival_time': 0},
        {'process': 'P3', 'burst_time': 3, 'arrival_time': 0},
    ]
    dataset2 = [
        {'process': 'P1', 'burst_time': 6, 'arrival_time': 0},
        {'process': 'P2', 'burst_time': 8, 'arrival_time': 0},
        {'process': 'P3', 'burst_time': 7, 'arrival_time': 0},
        {'process': 'P4', 'burst_time': 3, 'arrival_time': 0},
    ]
    dataset3 = [
        {'process': 'P1', 'burst_time': 10, 'arrival_time': 0, 'priority': 3},
        {'process': 'P2', 'burst_time': 1, 'arrival_time': 0, 'priority': 1},
        {'process': 'P3', 'burst_time': 2, 'arrival_time': 0, 'priority': 4},
        {'process': 'P4', 'burst_time': 1, 'arrival_time': 0, 'priority': 5},
        {'process': 'P5', 'burst_time': 5, 'arrival_time': 0, 'priority': 2},
    ]

    scheduling_algorithm = SchedulingAlgorithm(dataset=dataset1)
    updated_dateset, average_time = scheduling_algorithm.first_come_first_serve()
    print('First Come First Serve Scheduling')
    print(json.dumps(updated_dateset, indent=4))
    print('Average:', average_time)
    print()

    scheduling_algorithm = SchedulingAlgorithm(dataset=dataset2)
    updated_dateset, average_time = scheduling_algorithm.shortest_job_first()
    print('Shortest Job First Scheduling')
    print(json.dumps(updated_dateset, indent=4))
    print('Average:', average_time)
    print()

    scheduling_algorithm = SchedulingAlgorithm(dataset=dataset3)
    updated_dateset, average_time = scheduling_algorithm.priority_scheduling()
    print('Priority Scheduling')
    print(json.dumps(updated_dateset, indent=4))
    print('Average:', average_time)
    print()

    # scheduling_algorithm = SchedulingAlgorithm(dataset=dataset1)
    # updated_dateset, average_time = scheduling_algorithm.round_robin()
    # print('Round Robin Scheduling')
    # print(json.dumps(updated_dateset, indent=4))
    # print('Average:', average_time)
    # print()
