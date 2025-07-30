#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// see the ASIDE below for why
// this constant is useful
#define MAX_STR_LEN 200


// Linked list of strings

struct Node {
  char *data;
  struct Node *next;
};

struct Node* new_node(char *d) {
  struct Node *n = (struct Node*) malloc(sizeof(struct Node));

  // TIP: We cannot depend on the string pointed to by
  // data necessarily staying the same. Therefore,
  // we'll copy the string. This involves allocating
  // space for it and then copying the elements.

  // allocate space for the string
  n->data = (char*) malloc(MAX_STR_LEN * sizeof(char));
  
  // copy the input string into the new node's data field
  strncpy(n->data, d, MAX_STR_LEN);
  // ASIDE: there are two similar library procedures: strncpy and strcpy
  // they differ in that strncpy requires a length argument. Others
  // like strcmp/strncmp follow this convention, too.
  // It is good practice to always use the "n" variant because
  // the "non-n" variant could overflow the array you are copying into!

  n->next = NULL;
  return n;
}

// add an element to the front
struct Node* list_prepend(struct Node *l, char *e) {
  struct Node *n = new_node(e);
  n->next = l;
  return n;
}

// free the memory associated with the list
void free_list(struct Node *l) {
  while (l != NULL) {
    struct Node* c = l->next;
    free(l->data);
    free(l);
    l = c;
  }
}

int main() {
  char str[MAX_STR_LEN];
  sprintf(str, "I am %d", 0);
  
  struct Node* head = new_node(str);

  for (int i=1; i<10000; i++) {
    sprintf(str, "I am %d", i);
    head = list_prepend(head, str);
  }
  
  free_list(head);
}
