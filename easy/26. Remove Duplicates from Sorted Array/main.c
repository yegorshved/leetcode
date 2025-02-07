#include <stdio.h>
#include <stdlib.h>
typedef struct ListNode {
  int val;
  struct ListNode *next;
} ln;
void printList(ln* head);
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode* res = NULL;//(list1->val < list2->val ? list1->val : list2->val);
    struct ListNode* next = NULL;//(list1->val < list2->val ? list1->val : list2->val);
    if (list1 == NULL){
        res = list2;
        return res;
    }
    if (list2 == NULL){
        res = list1;
        return res;
    }
    while (list1 != NULL || list2 != NULL){
        if (res == NULL){
            if (list1->val < list2->val){
                res = list1;
                list1=list1->next;
            }
            else {
                res = list2;
                list2=list2->next;
            }
            next = res;
        }
        
        if (list1 == NULL){
          next->next = list2;
          break;
        }
        else if (list2 == NULL){
          next->next = list1;
          break;
        }
        

        if (list1->val < list2->val){
           next->next = list1;
           next=next->next;
           list1=list1->next;
        }
        else{
           next->next = list2;
           next=next->next;
           list2=list2->next;
        }
      printList(res);
    }
    return res;
}
void print(ln* res){
  if (res == NULL){
    printf("ln res is null!\n");
    return;
  }
  ln* temp = res;
  while (temp != NULL){
    printf("%d->", temp->val);
    temp=temp->next;
  }
  printf("\n");
  temp = NULL;
}
ln* createNode(int value) {
    ln* newNode = (ln*)malloc(sizeof(ln));
    if (newNode == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(1);
    }
    newNode->val = value;
    newNode->next = NULL;
    return newNode;
}

// Function to add an element to the end of the linked list
void addElement(ln** head, int value) {
    ln* newNode = createNode(value);
    if (*head == NULL) {
        // If the list is empty, set the new node as the head
        *head = newNode;
    } else {
        // Traverse to the end of the list
        ln* current = *head;
        while (current->next != NULL) {
            current = current->next;
        }
        // Append the new node
        current->next = newNode;
    }
}
void printList(ln* head) {
    ln* current = head;
    while (current != NULL) {
        printf("%d -> ", current->val);
        current = current->next;
    }
    printf("NULL\n");
}
int main(void){
  ln *l1 = NULL, *l2 = NULL;
    addElement(&l1, 1);
    addElement(&l1, 2);
    addElement(&l1, 4);

    // Add elements to l2 (list2 = [1, 3, 4])
    addElement(&l2, 1);
    addElement(&l2, 3);
    addElement(&l2, 4);
  //printList(l1);
  //printList(l2);
  ln *res = mergeTwoLists(l1, l2);
 // printf("res is %p\n", (void*)res);
//  print(res);
  return 0;
}
