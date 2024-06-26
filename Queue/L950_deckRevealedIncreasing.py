#Input: deck = [17,13,11,2,3,5,7]
#Output: [2,13,3,11,5,17,7]
#Explanation: 
#We get the deck in the order [17,13,11,2,3,5,7] (this order does not matter), and reorder it.
#After reordering, the deck starts as [2,13,3,11,5,17,7], where 2 is the top of the deck.
#We reveal 2, and move 13 to the bottom.  The deck is now [3,11,5,17,7,13].
#We reveal 3, and move 11 to the bottom.  The deck is now [5,17,7,13,11].
#We reveal 5, and move 17 to the bottom.  The deck is now [7,13,11,17].
#We reveal 7, and move 13 to the bottom.  The deck is now [11,17,13].
#We reveal 11, and move 17 to the bottom.  The deck is now [13,17].
#We reveal 13, and move 17 to the bottom.  The deck is now [17].
#We reveal 17.
#Since all the cards revealed are in increasing order, the answer is correct.

from collections import deque
def revealCards(deck):
    # Sort the deck in ascending order.
    deck.sort()
    # Initialize an empty list to store the result.
    res = [0]* len(deck)
    # Create a deque from the range of indices of the deck.
    q = deque(range(len(deck)))

    # Iterate through the sorted deck.
    for i in deck:
        # Pop the leftmost element from the deque.
        n = q.popleft()
        # Assign the current card to the corresponding index in the result list.
        res[n] = i
        # If the deque is not empty, append the leftmost element to the right.
        if q:
            q.append(q.popleft())
    # Return the result list.
    return res

deck = [17,13,11,2,3,5,7]
print(revealCards(deck))