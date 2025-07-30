#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

struct Process {
    int pid;
    int arrival_time;
    int burst_time;
    int remaining_time; // Remaining burst time for SRJF scheduling
    int priority; // Priority level (higher value indicates higher priority)
};

// Example test processes
struct Process processes[] = {
    {11, 10, 6, 6, 1},
    {12, 11, 8, 8, 3},
    {13, 12, 4, 4, 2},
    {14, 13, 7, 7, 1},
    {15, 14, 3, 3, 3},
    {16, 15, 6, 6, 2},
    {17, 16, 5, 5, 1},
    {18, 17, 4, 4, 3},
    {19, 18, 7, 7, 2},
    {20, 19, 9, 9, 1},
    /*
    {1, 1, 5, 5, 3},
    {2, 2, 10, 10, 1},
    */
};

void schedule_processes(struct Process processes[], int num_processes) {
    // Separate queues for different priority levels
    struct Process high_priority_queue[10];
    struct Process medium_priority_queue[10];
    struct Process low_priority_queue[10];
    int high_size = 0, medium_size = 0, low_size = 0;
    int current_time = 0;
    int current_queue = 0;
    int completed_processes = 0;
    int queue_index = -1;
    int total_turnaround_time = 0;
    int total_response_time = 0;

    // Distribute processes to respective queues based on priority
    for (int i = 0; i < num_processes; ++i) {
        if (processes[i].priority == 1) {
            high_priority_queue[high_size++] = processes[i];
        } else if (processes[i].priority == 2) {
            medium_priority_queue[medium_size++] = processes[i];
        } else {
            low_priority_queue[low_size++] = processes[i];
        }
    }

    // Execute processes from each queue
    printf("Process Execution Order:\n");

    // SRJF scheduling logic
    while (completed_processes < num_processes) {
        //printf("current time = %d\n", current_time);
        int min_remaining = INT_MAX;

        queue_index = -1;

        // High-priority queue
        for (int i = 0; i < high_size; ++i) {
            if (high_priority_queue[i].arrival_time <= current_time && high_priority_queue[i].remaining_time > 0) {
                if (high_priority_queue[i].remaining_time < min_remaining) {
                    min_remaining = high_priority_queue[i].remaining_time;
                    queue_index = i;
                    current_queue = 1;
                }
            }
        }

        if (queue_index == -1) {
            // Medium-priority queue
            for (int i = 0; i < medium_size; ++i) {
                if (medium_priority_queue[i].arrival_time <= current_time && medium_priority_queue[i].remaining_time > 0) {
                    if (medium_priority_queue[i].remaining_time < min_remaining) {
                        min_remaining = medium_priority_queue[i].remaining_time;
                        queue_index = i;
                        current_queue = 2;
                    }
                }
            }
            if (queue_index == -1) {
                // Low-priority queue
                for (int i = 0; i < low_size; ++i) {
                    if (low_priority_queue[i].arrival_time <= current_time && low_priority_queue[i].remaining_time > 0) {
                        if (low_priority_queue[i].remaining_time < min_remaining) {
                            min_remaining = low_priority_queue[i].remaining_time;
                            queue_index = i;
                            current_queue = 3;
                        }
                    }
                }
            }
        }

        //check for found process
        if (queue_index == -1) {
            printf("No process to execute.\n");
            current_time++;
            continue;
        }

        // Execute the process, based on current_queue

        // If High-priority queue
        if (current_queue == 1) {
            //if process seen for first time
            if (high_priority_queue[queue_index].burst_time == high_priority_queue[queue_index].remaining_time) {
                // Calculate response time and add to list of response times
                int response_time = current_time - high_priority_queue[queue_index].arrival_time;
                total_response_time += response_time;
                printf("Reponse Time for Process %d: %d\n", high_priority_queue[queue_index].pid, response_time);
            }

            printf("Executing Process %d (Burst Time: %d", high_priority_queue[queue_index].pid, high_priority_queue[queue_index].remaining_time);
            printf(", Remaining Time: %d)", high_priority_queue[queue_index].remaining_time);
            printf("\n");
            int execution_time = (high_priority_queue[queue_index].remaining_time < high_priority_queue[queue_index].remaining_time) ? high_priority_queue[queue_index].remaining_time : high_priority_queue[queue_index].remaining_time;
            high_priority_queue[queue_index].remaining_time -= 1;

            //if process completes
            if (high_priority_queue[queue_index].remaining_time == 0) {
                completed_processes++;
                // Calculate turnaround time and add to list of response times
                int turnaround_time = current_time - high_priority_queue[queue_index].arrival_time + 1; // added a +1
                total_turnaround_time += turnaround_time;
                printf("Turnaround Time for Process %d: %d\n", high_priority_queue[queue_index].pid, turnaround_time);
            }
        } else if (current_queue == 2) { // Else if Medium queue
            //if process seen for first time
            if (medium_priority_queue[queue_index].burst_time == medium_priority_queue[queue_index].remaining_time) {
                // Calculate response time and add to list of response times
                int response_time = current_time - medium_priority_queue[queue_index].arrival_time;
                total_response_time += response_time;
                printf("Reponse Time for Process %d: %d\n", medium_priority_queue[queue_index].pid, response_time);
            }

            printf("Executing Process %d (Burst Time: %d", medium_priority_queue[queue_index].pid, medium_priority_queue[queue_index].remaining_time);
            printf(", Remaining Time: %d)", medium_priority_queue[queue_index].remaining_time);
            printf("\n");
            int execution_time = (medium_priority_queue[queue_index].remaining_time < medium_priority_queue[queue_index].remaining_time) ? medium_priority_queue[queue_index].remaining_time : medium_priority_queue[queue_index].remaining_time;
            medium_priority_queue[queue_index].remaining_time -= 1;

            //if process completes
            if (medium_priority_queue[queue_index].remaining_time == 0) {
                completed_processes++;
                // Calculate turnaround time and add to list of response times
                int turnaround_time = current_time - medium_priority_queue[queue_index].arrival_time + 1; // added a +1
                total_turnaround_time += turnaround_time;
                printf("Turnaround Time for Process %d: %d\n", medium_priority_queue[queue_index].pid, turnaround_time);
            }
        } else { // Else Low queue
            //if process seen for first time
            if (low_priority_queue[queue_index].burst_time == low_priority_queue[queue_index].remaining_time) {
                // Calculate response time and add to list of response times
                int response_time = current_time - low_priority_queue[queue_index].arrival_time;
                total_response_time += response_time;
                printf("Reponse Time for Process %d: %d\n", low_priority_queue[queue_index].pid, response_time);
            }

            printf("Executing Process %d (Burst Time: %d", low_priority_queue[queue_index].pid, low_priority_queue[queue_index].remaining_time);
            printf(", Remaining Time: %d)", low_priority_queue[queue_index].remaining_time);
            printf("\n");
            int execution_time = (low_priority_queue[queue_index].remaining_time < low_priority_queue[queue_index].remaining_time) ? low_priority_queue[queue_index].remaining_time : low_priority_queue[queue_index].remaining_time;
            low_priority_queue[queue_index].remaining_time -= 1;

            //if process completes
            if (low_priority_queue[queue_index].remaining_time == 0) {
                completed_processes++;
                // Calculate turnaround time and add to list of response times
                int turnaround_time = current_time - low_priority_queue[queue_index].arrival_time + 1; // added a +1
                total_turnaround_time += turnaround_time;
                printf("Turnaround Time for Process %d: %d\n", low_priority_queue[queue_index].pid, turnaround_time);
            }
        }

        /*
        //Feedback Mechanism
        int feedback = 25;
        //check medium queue for long wait
        for (int i = 0; i < medium_size; i++) {
            if (current_time - medium_priority_queue[i].arrival_time > feedback) {
                high_priority_queue[high_size++] = medium_priority_queue[i];

                for (int k = i; k < medium_size - 1; k++) {
                    medium_priority_queue[k] = medium_priority_queue[k + 1];
                }
            }
        }
        //check low queue for long wait
        for (int i = 0; i < low_size; i++) {
            if (current_time - low_priority_queue[i].arrival_time > feedback) {
                high_priority_queue[high_size++] = low_priority_queue[i];

                for (int k = i; k < low_size - 1; k++) {
                    low_priority_queue[k] = low_priority_queue[k + 1];
                }
            }
        }
        */

        current_time++;
    }

    // Calculate and print average turnaround time and average response time
    float avg_turnaround_time = (float)total_turnaround_time / num_processes;
    float avg_response_time = (float)total_response_time / num_processes;
    printf("\nAverage Turnaround Time: %.2f\n", avg_turnaround_time);
    printf("Average Response Time: %.2f\n", avg_response_time);
}

int main() {
    int num_processes = sizeof(processes) / sizeof(struct Process);
    schedule_processes(processes, num_processes);
    return 0;
}
