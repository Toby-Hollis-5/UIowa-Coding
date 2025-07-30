#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>

// code is learned from lectures and Quiz 1

#define MAX_INPUT_SIZE 1024
#define MAX_ARGS 64

int parse_input(char *input, char *args[]) {
    int count = 0;
    char *token = strtok(input, " \t\n");

    while (token != NULL) {
        args[count++] = token;
        token = strtok(NULL, " \t\n");

        if (count >= MAX_ARGS - 1) {
            fprintf(stderr, "Too many arguments\n");
            exit(EXIT_FAILURE);
        }
    }

    args[count] = NULL;
    return count;
}

void execute_command(char *args[]) {
    pid_t pid, wpid;
    int status;

    //Create fork
    pid = fork();

    if (pid == 0) {
        if (execvp(args[0], args) == -1) {
            perror("error");
        }
        exit(EXIT_FAILURE);
    } else if (pid < 0) {
        perror("error");
    } else { //run command
        do {
            wpid = waitpid(pid, &status, WUNTRACED);
        } while (!WIFEXITED(status) && !WIFSIGNALED(status));
    }
}

int main() {
    char input[MAX_INPUT_SIZE];
    char *args[MAX_ARGS];

    while (1) {
        printf(">>>");
        fgets(input, sizeof(input), stdin);

        input[strcspn(input, "\n")] = '\0';

        if (strcmp(input, "exit") == 0) {
            printf("Exiting...\n");
            break;
        }

        //Special for cd
        if (strcmp(input, "cd") == 0) {
            printf("Changing directory...\n");
            chdir(args[1]);
        }

        int arg_count = parse_input(input, args);

        if (arg_count > 0) {
            execute_command(args);
        }
    }

    return 0;
}