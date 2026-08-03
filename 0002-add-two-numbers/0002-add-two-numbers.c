#include <stdlib.h>
 // Definition for singly-linked list.
// typedef struct ListNode{
//      int val;
//      struct ListNode *next;
//  }ListNode;

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode dummy;
    dummy.val = 0;
    dummy.next = NULL;

    struct ListNode* curr = &dummy;
    int carry = 0, sum = 0;

    //the function will run while there are still nodes left or carry is not empty
    while(l1!=NULL || l2!=NULL || carry!=0 ){
        sum = carry;
        
        if(l1 != NULL){
            sum += l1->val;
            l1 = l1->next;
        }

        if(l2!=NULL){
            sum += l2->val;
            l2 = l2->next;
        }

        struct ListNode* new_node =(struct ListNode*) malloc(sizeof(struct ListNode));
        //check memory allocation
        if(new_node==NULL){
            exit(1);
        }

        //sets the new node
        new_node->val = sum%10;
        new_node->next = NULL;

        //adds new node to the list
        curr->next = new_node;
        curr = curr->next;

        carry = sum/10;
    }
    //returns pointer to ListNode
    return dummy.next;
}

