#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <assert.h>
#include <stdio.h>

// Problem 1
/* Replace this comment with answers to...
a. Explain what the specific source(s) of the invalid read errors were in Problem 1.
	The specific sources of the invalid read errors were in freeNode, freeSubTree, and freeTree. They are trying to use members of n after already freeing n. After running Valgrind, many calls to these functions were showing up.

b. This problem demonstrated an example of a common class of errors called use-after-free. Explain why this kind of error has that name.
	This error has that name because we were freeing the node and then trying to access its data and pointers after already freeing it. 
*/



// Problem 2
/* The problem for this was that we were replacing the pointer for p, but never deleting the original one or the temporary replacement. So, I free'd p's data, set replacement's data to NULL, and then at the end free'd p and the leaf.
*/

#define MAXLEN 200

typedef struct Node {
  char *data;
  struct Node *left;
  struct Node *right;
  struct Node *parent;
} Node;

typedef struct BinaryTree {
  struct Node *root;
} BinaryTree;

bool isExternal(Node *n) {
  return n->left == NULL && n->right == NULL;
}

Node* treeSearch(Node *n, char *key) {
  if (isExternal(n)) return n;

  if (strncmp(key, n->data, MAXLEN) < 0) {
    return treeSearch(n->left, key);
  } else if (strncmp(key, n->data, MAXLEN) > 0) {
    return treeSearch(n->right, key);
  } else {
    return n;
  }
}

Node* newNode(Node *parent) {
  Node *n = malloc(1 * sizeof(Node));
  n->data = NULL; 
  n->left = NULL;
  n->right = NULL;
  n->parent = parent;
  return n;
}


BinaryTree* newBinaryTree() {
  BinaryTree *b = malloc(1 * sizeof(BinaryTree));
  b->root = newNode(NULL);
  return b;
}

void expandExternal(Node *n, char *data) {
  n->data = malloc(MAXLEN * sizeof(char));
  strncpy(n->data, data, MAXLEN);
  n->left = newNode(n);
  n->right = newNode(n);
}

void add(BinaryTree *b, char *key) {
  Node *found = treeSearch(b->root, key);
  if (isExternal(found)) {
    expandExternal(found, key);
  }
} 

bool contains(BinaryTree *b, char *key) {
  Node *found = treeSearch(b->root, key);
  return !isExternal(found);
}

void freeNode(Node *n) {
  
  if (n->data != NULL) free(n->data);
  free(n);
}

void freeSubTree(Node *n) {
  if (n != NULL) {
    
    freeSubTree(n->left);
    freeSubTree(n->right);
    freeNode(n);
  }
} 

void freeTree(BinaryTree *b) {
  
  freeSubTree(b->root);
  free(b);
}  

void removeNode(BinaryTree *b, Node *n) {
  assert(n->left == NULL || n->right == NULL);

  Node *child = n->left != NULL ? n->left : n->right;
  if (child != NULL) {
    child->parent = n->parent;
  }
  if (n == b->root) {
    b->root = child;                       // child becomes root
  } else {
    Node *parent = n->parent;
    if (n == parent->left) {
      parent->left = child;
    } else {
      parent->right = child;
    }
  }
}

Node* sibling(Node *p) {
    Node *parent = p->parent; 
    if (parent == NULL) return NULL;                  // p must be the root
    if (p == parent->left) {                           // p is a left child
      return parent->right;                           // (right child might be null)
    } else {                                              // p is a right child
      return parent->left;                           // (left child might be null)
    }
 }

Node* treeMax(Node *p) {
    Node *walk = p;
    while (!isExternal(walk)) {
      walk = walk->right; 
    }
    return walk->parent; 
  }


void removeKey(BinaryTree *b, char *key) {
  Node *p = treeSearch(b->root, key);
  if (!isExternal(p)) {   
    if (!isExternal(p->left) && !isExternal(p->right)) { // both children are internal
      Node *replacement = treeMax(p->left);
      free(p->data);
      p->data = replacement->data;
      replacement->data = NULL;
      p = replacement;
    } // now p has at most one child that is an internal node
    Node *leaf = (isExternal(p->left)) ? p->left : p->right;
    removeNode(b, leaf);
    removeNode(b, p);
    free(leaf);
    free(p);
  }
}

void printSubTree(Node *p, int depth) {
    char indent[MAXLEN];
    if (depth == 0) sprintf(indent, "%s", "");
    else sprintf(indent, "%*c", 2*depth, ' ');

    if (isExternal(p))
      printf("%s leaf\n", indent);
    else {
      printf("%s %s\n", indent, p->data);
      printSubTree(p->left, depth+1);
      printSubTree(p->right, depth+1);
    }
}

void printTree(BinaryTree *b) {
  printSubTree(b->root, 0);
}




int main() {
  BinaryTree *tree = newBinaryTree();
  // repeatedly using a string buffer
  // to ensure you don't replace string
  // copy in newNode with pointer 
  // assignment
  char buffer[MAXLEN];
  sprintf(buffer, "35");
  add(tree, buffer);
  sprintf(buffer, "30");
  add(tree, buffer);
  sprintf(buffer, "89");
  add(tree, buffer);
  sprintf(buffer, "22");
  add(tree, buffer);
  sprintf(buffer, "83");
  add(tree, buffer);
  sprintf(buffer, "95");
  add(tree, buffer);
  sprintf(buffer, "09");
  add(tree, buffer);
  sprintf(buffer, "80");
  add(tree, buffer);
  sprintf(buffer, "85");
  add(tree, buffer);
  sprintf(buffer, "91");
  add(tree, buffer);
  sprintf(buffer, "98");
  add(tree, buffer);
  sprintf(buffer, "60");
  add(tree, buffer);

  // uncomment this during "Fix the memory leak"
  removeKey(tree, "89");

  printTree(tree);

  freeTree(tree);
}
