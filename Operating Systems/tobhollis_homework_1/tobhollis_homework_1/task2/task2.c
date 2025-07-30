#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <dirent.h>
#include <ctype.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>

#define MAX_PATH_LEN 4096
#define MAX_PID_LEN 10

// Function to check if a string represents a number
int is_number(const char *str) {
    while (*str) {
        if (!isdigit(*str))
            return 0;
        str++;
    }
    return 1;
}

long read_context_switches(int pid) {
    char filename[MAX_PATH_LEN];
    snprintf(filename, MAX_PATH_LEN, "/proc/%d/status", pid);
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        fprintf(stderr, "Error: Unable to open file %s\n", filename);
        return -1;
    }
    char line[256];
    long voluntary_ctxt_switches = -1;
    long nonvoluntary_ctxt_switches = -1;
    while (fgets(line, sizeof(line), file)) {
        if (sscanf(line, "voluntary_ctxt_switches: %ld", &voluntary_ctxt_switches) == 1) {
            continue;
        }
        if (sscanf(line, "nonvoluntary_ctxt_switches: %ld", &nonvoluntary_ctxt_switches) == 1) {
            continue;
        }
    }
    fclose(file);
    //combines voluntary and nonvoluntary context switches for total amount.
    return voluntary_ctxt_switches + nonvoluntary_ctxt_switches;
}

void print_process_info(int pid) {
    char filename[MAX_PATH_LEN];
    snprintf(filename, MAX_PATH_LEN, "/proc/%d/cmdline", pid);
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        fprintf(stderr, "Error: Unable to open file %s\n", filename);
        return;
    }
    char cmdline[MAX_PATH_LEN];
    size_t len = fread(cmdline, sizeof(char), MAX_PATH_LEN - 1, file);
    fclose(file);
    if (len > 0) {
        cmdline[len] = '\0';
        long ctxt_switches = read_context_switches(pid);
        printf("| %5d | %-50s | %10ld |\n", pid, cmdline, ctxt_switches);
    }
}

int main() {
    uid_t uid = getuid();
    DIR *dir = opendir("/proc");
    if (dir == NULL) {
        perror("Error: Unable to open /proc directory");
        exit(EXIT_FAILURE);
    }

    //set up table for formatting. Formatting taken from:
    //https://pubs.opengroup.org/onlinepubs/009695399/functions/fprintf.html
    printf("| %-6s | %-50s | %-12s |\n", "PID", "Executable Path", "Context Switches");
    printf("|--------|----------------------------------------------------|--------------|\n");

    struct dirent *entry;
    while ((entry = readdir(dir)) != NULL) {
        if (is_number(entry->d_name)) {
            int pid = atoi(entry->d_name);
            char status_path[MAX_PATH_LEN];
            snprintf(status_path, MAX_PATH_LEN, "/proc/%d/status", pid);
            FILE *file = fopen(status_path, "r");
            if (file == NULL) {
                continue;
            }
            char line[256];
            int found_uid = 0;
            while (fgets(line, sizeof(line), file)) {
                if (strncmp(line, "Uid:", 4) == 0) {
                    char *uid_str = strtok(line, "\t");
                    if (uid_str != NULL) {
                        uid_str = strtok(NULL, "\t");
                        if (uid_str != NULL && atoi(uid_str) == uid) {
                            found_uid = 1;
                            break;
                        }
                    }
                }
            }
            fclose(file);
            if (found_uid) {
                print_process_info(pid);
            }
        }
    }
    closedir(dir);

    return 0;
}