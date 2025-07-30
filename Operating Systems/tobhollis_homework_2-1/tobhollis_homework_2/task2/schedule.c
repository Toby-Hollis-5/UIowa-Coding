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
    {1, 0, 8, 8},
    {2, 1, 5, 5},
    {3, 2, 10, 10},
    {4, 3, 3, 3},
    {5, 4, 6, 6},
    {6, 5, 7, 7},
    {7, 6, 4, 4},
    {8, 7, 9, 9},
    {9, 8, 2, 2},
    {10, 9, 5, 5},
    {11, 10, 6, 6},
    {12, 11, 8, 8},
    {13, 12, 4, 4},
    {14, 13, 7, 7},
    {15, 14, 3, 3},
    {16, 15, 6, 6},
    {17, 16, 5, 5},
    {18, 17, 4, 4},
    {19, 18, 7, 7},
    {20, 19, 9, 9},
};

void schedule_processes_FIFO(struct Process fifoProcesses[], int num_processes) {
    int current_time = 0; // Initialize current time

    //make copy of Process list
    struct Process processes[num_processes];
    for (int i = 0; i < num_processes; i++) {
        processes[i] = fifoProcesses[i];
    }

    int turnaroundTimes[num_processes];
    int avg_turnaround_time = 0;
    int responseTimes[num_processes];
    int avg_response_time = 0;

    printf("Process Execution Order (FIFO):\n");
    for (int i = 0; i < num_processes; ++i) {
        // Wait until the process arrives (if needed)
        if (current_time < processes[i].arrival_time) {
            current_time = processes[i].arrival_time;
        }
        // Execute the process
        printf("Executing Process %d (Burst Time: %d)\n", processes[i].pid, processes[i].burst_time);
        current_time += processes[i].burst_time;

        // Calculate turnaround time and add to list of turnaround times
        int turnaround_time = current_time - processes[i].arrival_time;
        turnaroundTimes[i] = turnaround_time;
        printf("Turnaround Time for Process %d: %d\n", processes[i].pid, turnaround_time);

        // Calculate response time and add to list of response times
        int response_time = current_time;
        responseTimes[i] = response_time;
        printf("Reponse Time for Process %d: %d\n", processes[i].pid, response_time);
    }

    //calculate average turnaround and response times
    for (int i = 0; i < num_processes; i++) {
        avg_turnaround_time += turnaroundTimes[i];
        //printf("turnaround_time[%d] = %d\n", i, turnaroundTimes[i]);
        avg_response_time += responseTimes[i];
        //printf("response_time[%d] = %d\n", i, responseTimes[i]);
    }

    avg_turnaround_time = avg_turnaround_time / num_processes;
    avg_response_time = avg_response_time / num_processes;

    printf("Avg turnaround time: %d\n", avg_turnaround_time);
    printf("Avg response time: %d\n", avg_response_time);


}

void schedule_processes_sjf(struct Process sjfProcesses[], int num_processes) {
    int current_time = 0; // Initialize current time
    int completed_processes = 0;
    int turnaroundTimes[num_processes];
    int avg_turnaround_time = 0;
    int responseTimes[num_processes];
    int avg_response_time = 0;

    printf("Process Execution Order (SJF):\n");

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
            current_time++;
            continue;
        }

        // Execute the process
        printf("Executing Process %d (Burst Time: %d)\n", processes[min_burst_index].pid, processes[min_burst_index].burst_time);
        current_time += processes[min_burst_index].burst_time;
        processes[min_burst_index].remaining_time = 0; // Mark as completed
        completed_processes++;
        
        // Calculate turnaround time and add to list of turnaround times
        int turnaround_time = current_time - processes[min_burst_index].arrival_time;
        turnaroundTimes[min_burst_index] = turnaround_time;
        printf("Turnaround Time for Process %d: %d\n", processes[min_burst_index].pid, turnaround_time);

        // Calculate response time and add to list of response times
        int response_time = current_time;
        responseTimes[min_burst_index] = response_time;
        printf("Reponse Time for Process %d: %d\n", processes[min_burst_index].pid, response_time);
    }

    //calculate average turnaround and response times
    for (int i = 0; i < num_processes; i++) {
        avg_turnaround_time += turnaroundTimes[i];
        //printf("turnaround_time[%d] = %d\n", i, turnaroundTimes[i]);
        avg_response_time += responseTimes[i];
        //printf("response_time[%d] = %d\n", i, responseTimes[i]);
    }

    avg_turnaround_time = avg_turnaround_time / num_processes;
    avg_response_time = avg_response_time / num_processes;

    printf("Avg turnaround time: %d\n", avg_turnaround_time);
    printf("Avg response time: %d\n", avg_response_time);
}

void schedule_processes_srjf(struct Process srjfProcesses[], int num_processes) {
    int current_time = 0; // Initialize current time
    printf("Process Execution Order (SRJF):\n");
    int completed_processes = 0;
    int min_remaining_index = -1;

    int turnaroundTimes[num_processes];
    int avg_turnaround_time = 0;
    int responseTimes[num_processes];
    int avg_response_time = 0;

    //initialize responseTimes array
    for (int i = 0; i < num_processes; i++) {
        responseTimes[i] = -1;
    }

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
        printf("Executing Process %d (Burst Time: %d", processes[min_remaining_index].pid, processes[min_remaining_index].remaining_time);
        printf(", Remaining Time: %d)", processes[min_remaining_index].remaining_time);
        printf("\n");
        int execution_time = (processes[min_remaining_index].remaining_time < processes[min_remaining_index].remaining_time) ? processes[min_remaining_index].remaining_time : processes[min_remaining_index].remaining_time;
        processes[min_remaining_index].remaining_time -= 1;

        //process completes
        if (processes[min_remaining_index].remaining_time == 0) {
            completed_processes++;
            // Calculate turnaround time and add to list of response times
            int turnaround_time = current_time - processes[min_remaining_index].arrival_time;
            turnaroundTimes[min_remaining_index] = turnaround_time;
            printf("Turnaround Time for Process %d: %d\n", processes[min_remaining_index].pid, turnaround_time);
        }

        if (responseTimes[min_remaining_index] == -1) {
            // Calculate response time and add to list of response times
            int response_time = current_time;
            responseTimes[min_remaining_index] = response_time;
            printf("Reponse Time for Process %d: %d\n", processes[min_remaining_index].pid, response_time);
        }

        current_time++;
    }

    //calculate average turnaround and response times
    for (int i = 0; i < num_processes; i++) {
        avg_turnaround_time += turnaroundTimes[i];
        //printf("turnaround_time[%d] = %d\n", i, turnaroundTimes[i]);
        avg_response_time += responseTimes[i];
        //printf("response_time[%d] = %d\n", i, responseTimes[i]);
    }

    avg_turnaround_time = avg_turnaround_time / num_processes;
    avg_response_time = avg_response_time / num_processes;

    printf("Avg turnaround time: %d\n", avg_turnaround_time);
    printf("Avg response time: %d\n", avg_response_time);
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
