#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define num_frames 20

typedef struct {
    int pageReference;
    char accessType;
} Page;

void secondChance(Page pages[], int num_pages) {
    int frames[num_frames];
    bool referenced[num_frames]; 
    int num_faults = 0;
    int pointer = 0; 
    int occupied = 0;

    // Initialize referenced array with false
    memset(referenced, false, sizeof(referenced));

    for (int i = 0; i < num_pages; i++) {
        Page page = pages[i];
        bool hit = false;

        // Check if page in memory
        for (int j = 0; j < occupied; j++) {
            if (frames[j] == page.pageReference) {
                hit = true;
                referenced[j] = true; // Mark the page as referenced!
                break;
            }
        }

        // If page not in memory
        if (!hit) {
            num_faults++;

            // Cold start
            if (occupied < num_frames) {
                frames[occupied] = page.pageReference;
                referenced[occupied] = true; // Mark the page as referenced!
                occupied++;
            } 
            // Memory full, cycle through and find page with no reference bit
            else {
                while (true) {
                    if (!referenced[pointer]) {
                        frames[pointer] = page.pageReference;
                        referenced[pointer] = true; // Mark the page as referenced!
                        pointer = (pointer + 1) % num_frames;
                        break;
                    }
                    referenced[pointer] = false; // Reset the reference bit
                    pointer = (pointer + 1) % num_frames;
                }
            }
        }
    }

    printf("\nNumbers of faults with Second Chance: %d\n", num_faults);
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

    // Run Second Chance Algorithm on pages
    secondChance(pages, num_pages);

    // Clean up
    free(pages);

    return 0;
}