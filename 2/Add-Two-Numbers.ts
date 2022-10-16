/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    const solution = new ListNode(0);
    let head = solution;
    
    let sum = 0;
    let carryOver = 0;
    
    while(l1 !== null || l2 !== null || sum > 0) {
        if(l1 !== null) {
            sum += l1.val;
            l1 = l1.next;
        }
        
        if(l2 !== null) {
            sum += l2.val;
            l2 = l2.next;
        }
        
        if(sum >= 10) {
            carryOver = 1;
            sum -= 10;
        }
        
        head.next = new ListNode(sum);
        head = head.next;
        
        sum = carryOver;
        carryOver = 0;
    }
    
    return solution.next;
};
