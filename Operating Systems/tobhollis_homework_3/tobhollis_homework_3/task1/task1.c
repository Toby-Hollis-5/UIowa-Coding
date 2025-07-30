#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define num_frames 20

typedef struct {
    int pageReference;
    char accessType;
} Page;

void FIFO(Page pages[], int num_pages) {
    int frames[num_frames];
    int occupied = 0;
    int num_faults = 0;
    bool hit;

    for (int i = 0; i < num_pages; i++) {
        hit = false;
        Page page = pages[i];
        // Check current frames for current page ref. If found, go to next.
        for (int j = 0; j < occupied; j++) {
            if (frames[j] == page.pageReference) {
                //printf("Page found\n");
                hit = true;
                break;
            }
        }

        if (hit) {
            continue;
        }
        if (!hit) {
            //Page not found in frames; fault
            num_faults++;

            if (occupied < num_frames) { // Cold start
                //printf("Cold start\n");
                frames[occupied] = page.pageReference;
                occupied++;
            } else { // Shift all frames in array left 1, add new to end
                //printf("Replace\n");
                for (int j = 0; j < num_frames - 1; j++) {
                    frames[j] = frames[j+1];
                }
                frames[num_frames - 1] = page.pageReference;
            }
        }
    }

    printf("\nNumber of faults with FIFO: %d\n", num_faults);
    float percentage = (float) num_faults / num_pages * 100;
    printf("Percentage rate: %.2f%%\n", percentage);
}

void LRU(Page pages[], int num_pages) {
    int frames[num_frames];
    int recent[num_frames]; // Array to store the most recent access time of each frame
    int num_faults = 0;
    int occupied = 0;

    // Initialize the recent array with -1, indicating no access yet
    for (int i = 0; i < num_frames; i++) {
        recent[i] = -1;
    }

    for (int i = 0; i < num_pages; i++) {
        Page page = pages[i];
        bool hit = false;

        // Check if the page is in memory
        for (int j = 0; j < occupied; j++) {
            if (frames[j] == page.pageReference) {
                hit = true;
                // Update the recent access time of the current frame
                recent[j] = i;
                break;
            }
        }

        // If the page is not in memory, perform page fault
        if (!hit) {
            num_faults++;
            
            // If there are empty frames, insert the page into an empty frame
            if (occupied < num_frames) {
                frames[occupied] = page.pageReference;
                recent[occupied] = i;
                occupied++;
            } 
            // Otherwise, find the least recently used frame and replace it
            else {
                int min_recent = recent[0];
                int min_index = 0;

                // Find the least recent frame
                for (int j = 1; j < num_frames; j++) {
                    if (recent[j] < min_recent) {
                        min_recent = recent[j];
                        min_index = j;
                    }
                }

                // Replace the least recent frame with the current page
                frames[min_index] = page.pageReference;
                recent[min_index] = i;
            }
        }
    }

    printf("\nNumber of faults with LRU: %d\n", num_faults);
    float percentage = (float) num_faults / num_pages * 100;
    printf("Percentage rate: %.2f%%\n", percentage);
}


int main() {
    FILE *file;
    int max_pages = 100;
    Page *pages = malloc(max_pages * sizeof(Page));
    int num_pages = 0;

    file = fopen("page_references.txt", "r");

    // Check if file opened successfully
    if (file == NULL) {
        perror("Error opening file.");
        return 1; // Exit with error
    }

    // Read each line from file
    while (fscanf(file, "%d %c", &pages[num_pages].pageReference, &pages[num_pages].accessType) == 2) {
        num_pages++;

        // Realloc if need more space
        if (num_pages >= max_pages) {
            max_pages *= 2;
            pages = realloc(pages, max_pages * sizeof(Page));
            if (pages == NULL) {
                perror("Error reallocating memory");
                return 1;
            }
        }
    }

    fclose(file);

    // Run FIFO on pages
    FIFO(pages, num_pages);

    // Run LRU on pages
    LRU(pages, num_pages);

    // Clean up
    free(pages);

    return 0;
}