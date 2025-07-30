#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define num_frames 20

typedef struct {
    int pageReference;
    char accessType;
} Page;

void enhancedSecondChance(Page pages[], int num_pages) {
    int frames[num_frames];
    bool referenced[num_frames]; // Array to track if a page has been referenced
    bool modified[num_frames]; // Array to track if a page has been modified (dirty)
    int num_faults = 0;
    int num_disk_writes = 0;
    int pointer = 0; // Pointer for enhanced second chance algorithm
    int occupied = 0;

    // Initialize referenced and modified arrays with false
    memset(referenced, false, sizeof(referenced));
    memset(modified, false, sizeof(modified));

    for (int i = 0; i < num_pages; i++) {
        Page page = pages[i];
        bool hit = false;

        // Check if the page is in memory
        for (int j = 0; j < occupied; j++) {
            if (frames[j] == page.pageReference) {
                hit = true;
                referenced[j] = true; // Mark the page as referenced
                if (page.accessType == 'w') {
                    modified[j] = true; // Mark the page as modified if it's a write access
                }
                break;
            }
        }

        // If the page is not in memory, perform page fault
        if (!hit) {
            num_faults++;
            
            // If there are empty frames, insert the page into an empty frame
            if (occupied < num_frames) {
                frames[occupied] = page.pageReference;
                referenced[occupied] = true; // Mark the page as referenced
                if (page.accessType == 'w') {
                    modified[occupied] = true; // Mark the page as modified if it's a write access
                }
                occupied++;
            } 
            // Otherwise, find the page with the lowest reference bit and replace it
            else {
                while (true) {
                    if (!referenced[pointer]) {
                        // Replace the page with the lowest reference bit
                        frames[pointer] = page.pageReference;
                        referenced[pointer] = true; // Mark the page as referenced
                        modified[pointer] = false; // Reset the modified bit
                        if (page.accessType == 'w') {
                            modified[pointer] = true; // Mark the page as modified if it's a write access
                        }
                        pointer = (pointer + 1) % num_frames; // Move pointer to the next frame
                        break;
                    }
                    referenced[pointer] = false; // Reset the reference bit
                    pointer = (pointer + 1) % num_frames; // Move pointer to the next frame
                }
            }

            // Increment the number of disk writes if the replaced page was modified
            if (modified[pointer]) {
                num_disk_writes++;
            }
        }
    }

    printf("\nNumbers of faults with Enhanced Second Chance: %d\n", num_faults);
    float fault_rate = (float) num_faults / num_pages;
    printf("Page fault rate: %.2f%%\n", fault_rate * 100);
    printf("Number of disk writes: %d\n", num_disk_writes);
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

    // Run Enhanced Second Chance Algorithm on pages
    enhancedSecondChance(pages, num_pages);

    // Clean up
    free(pages);

    return 0;
}