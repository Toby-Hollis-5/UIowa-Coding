#include <stdio.h>
#include <limits.h>
#include <string.h>

struct Process {
    int pid;
    int arrival_time;
    int burst_time;
    int remaining_time; // For SRJF
};

// Example test processes
struct Process processes[] = {
    {1, 0, 10, 10},
    {2, 2, 5, 5},
    {3, 4, 8, 8},
    /*
    {4, 4, 4, 4},
    {5, 11, 2, 2},
    */
    /*
    {1, 0, 1, 1},
    {2, 5, 9, 9},
    */
    // Add more processes here
};

void schedule_processes_FIFO(struct Process fifoProcesses[], int num_processes) {
    int current_time = 0; // Initialize current time

    //make copy of Process list
    struct Process processes[num_processes];
    for (int i = 0; i < num_processes; i++) {
        processes[i] = fifoProcesses[i];
    }

    printf("Process Execution Order (FIFO):\n");
    for (int i = 0; i < num_processes; ++i) {
        // Wait until the process arrives (if needed)
        if (current_time < processes[i].arrival_time) {
            current_time = processes[i].arrival_time;
        }
        // Execute the process
        printf("Executing Process %d (Burst Time: %d)\n", processes[i].pid, processes[i].burst_time);
        current_time += processes[i].burst_time;
        // Calculate turnaround time
        int turnaround_time = current_time - processes[i].arrival_time;
        printf("Turnaround Time for Process %d: %d\n", processes[i].pid, turnaround_time);
        // Response time measurement need to be implemented.
    }
}

void schedule_processes_sjf(struct Process sjfProcesses[], int num_processes) {
    int current_time = 0; // Initialize current time
    printf("Process Execution Order (SJF):\n");
    int completed_processes = 0;

    //make copy of Process list
    struct Process processes[num_processes];
    for (int i = 0; i < num_processes; i++) {
        processes[i] = sjfProcesses[i];
    }

    while (completed_processes < num_processes) {
        int min_burst_index = -1;
        int min_burst = INT_MAX;

        //find index of min burst
        for (int i = 0; i < num_processes; ++i) {
            if (processes[i].arrival_time <= current_time && processes[i].remaining_time > 0) {
                if (processes[i].burst_time < min_burst) {
                    min_burst = processes[i].burst_time;
                    min_burst_index = i;
                }
            }
        }
        if (min_burst_index == -1) {
            printf("No process to execute.");
            current_time++;
            continue;
        }
        // Execute the process
        printf("Executing Process %d (Burst Time: %d)\n", processes[min_burst_index].pid, processes[min_burst_index].burst_time);
        current_time += processes[min_burst_index].burst_time;
        processes[min_burst_index].remaining_time = 0; // Mark as completed
        completed_processes++;
        // Calculate turnaround time
        int turnaround_time = current_time - processes[min_burst_index].arrival_time;
        printf("Turnaround Time for Process %d: %d\n", processes[min_burst_index].pid, turnaround_time);
    }
}

void schedule_processes_srjf(struct Process srjfProcesses[], int num_processes) {
    int current_time = 0; // Initialize current time
    printf("Process Execution Order (SRJF):\n");
    int completed_processes = 0;
    int min_remaining_index = -1;

    //make copy of Process list
    struct Process processes[num_processes];
    for (int i = 0; i < num_processes; i++) {
        processes[i] = srjfProcesses[i];
    }

    while (completed_processes < num_processes) {
        //printf("current time = %d\n", current_time);
        int min_remaining = INT_MAX;

        if (processes[min_remaining_index].remaining_time == 0) {
            min_remaining_index = -1;
        }

        //find index of min remaining within current time
        for (int i = 0; i < num_processes; i++) {
            if (processes[i].arrival_time <= current_time && processes[i].remaining_time > 0) {
                if (processes[i].remaining_time < min_remaining) {
                    min_remaining = processes[i].remaining_time;
                    min_remaining_index = i;
                }
            }
        }

        if (min_remaining_index == -1) {
            printf("No process to execute.\n");
            current_time++;
            continue;
        }

        // Execute the process
        printf("Executing Process %d (Burst Time: %d, Remaining Time: %d)\n", processes[min_remaining_index].pid, processes[min_remaining_index].burst_time, processes[min_remaining_index].remaining_time);
        int execution_time = (processes[min_remaining_index].remaining_time < processes[min_remaining_index].burst_time) ? processes[min_remaining_index].remaining_time : processes[min_remaining_index].burst_time;
        processes[min_remaining_index].remaining_time -= 1;

        current_time++;

        if (processes[min_remaining_index].remaining_time == 0) {
            completed_processes++;
            // Calculate turnaround time
            int turnaround_time = current_time - processes[min_remaining_index].arrival_time;
            printf("Turnaround Time for Process %d: %d\n", processes[min_remaining_index].pid, turnaround_time);
        }
    }
}

int main() {
    int num_processes = sizeof(processes) / sizeof(struct Process);
   
    printf("FIFO Scheduling:\n");
    schedule_processes_FIFO(processes, num_processes);
   
    printf("\nSJF Scheduling:\n");
    schedule_processes_sjf(processes, num_processes);
   
    printf("\nSRJF Scheduling:\n");
    schedule_processes_srjf(processes, num_processes);
   
    return 0;
}
