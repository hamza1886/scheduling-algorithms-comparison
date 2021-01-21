# Scheduling Algorithms Comparison

A comparison of CPU scheduling algorithms on average response time, average waiting time and average turnaround time. Non-preemptive algorithms like First-Come-First-Serve, Shortest-Job-First and
Priority scheduling algorithms are analyzed.

## Getting Started

1. Clone repo ```git clone ```
2. Run code ```python main.py```

### Aside

Test data can be changed in `dataset1`, `dataset2` and `dataset3` variables in [main.py](main.py).

## Comparison of Algorithm

### First-Come-First-Serve Scheduling

| **Process** | **Burst Time** | **Arrival Time** | **Response Time** | **Waiting Time** | **Turnaround Time** |
| --- | --- | --- | --- | --- | --- |
| **P1** | 24 | 0 | 0 | 0 | 24 |
| **P2** | 3 | 0 | 24 | 24 | 27 |
| **P3** | 3 | 0 | 27 | 27 | 30 |
| **Average** | | | 17 | 17 | 27 |

### Shortest-Job-First Scheduling

| **Process** | **Burst Time** | **Arrival Time** | **Response Time** | **Waiting Time** | **Turnaround Time** |
| --- | --- | --- | --- | --- | --- |
| **P1** | 6 | 0 | 3 | 3 | 9 |
| **P2** | 8 | 0 | 16 | 16 | 24 |
| **P3** | 7 | 0 | 9 | 9 | 16 |
| **P4** | 3 | 0 | 0 | 0 | 3 |
| **Average** | | | 7 | 7 | 13 |

### Priority Scheduling

| **Process** | **Burst Time** | **Arrival Time** | **Response Time** | **Priority** | **Waiting Time** | **Turnaround Time** |
| --- | --- | --- | --- | --- | --- | --- |
| **P1** | 10 | 0 | 3 | 6 | 6 | 16 |
| **P2** | 1 | 0 | 1 | 0 | 0 | 1 |
| **P3** | 2 | 0 | 4 | 16 | 6 | 18 |
| **P4** | 1 | 0 | 5 | 18 | 18 | 19 |
| **P5** | 5 | 0 | 2 | 1 | 1 | 6 |
| **Average** | | | | 8.2 | 8.2 | 12 |

## Results

From the comparison of CPU scheduling algorithm on test data it is shown that Shortest-Job-First scheduling is the quickest on average response time and average waiting time whereas Priority
scheduling is the quickest on average turnaround time.

## License

The project is open-source software licensed under the MIT [license](LICENSE).