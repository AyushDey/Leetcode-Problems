#Input: tickets = [2,3,2], k = 2
#Output: 6
#Explanation: 
#- In the first pass, everyone in the line buys a ticket and the line becomes [1, 2, 1].
#- In the second pass, everyone in the line buys a ticket and the line becomes [0, 1, 0].
#The person at position 2 has successfully bought 2 tickets and it took 3 + 3 = 6 seconds.

#Algo 
# If people before kth index have: 
#   - Higher requirement than k, take the k amount as after each ticket the person will go to the back
#   - Lower requirement than k, take the amount of that index.
# If people after kth index have: 
#   - Higher requirement than k, take the difference between k and 1 as the person will have to go back after each ticket.
#   - Lower requirement than k, take the amount of that index.

def timeTickets(tickets, k):
    time = 0
    for i in range(len(tickets)):
        if i > k:
            time += min(tickets[i], tickets[k] - 1)
        else:
            time += min(tickets[i], tickets[k])

    return time


tickets = [5,1,1,1]
k = 0
print(timeTickets(tickets, k))