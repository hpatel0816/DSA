# LeetCode (2347 - Best Poker Hand)

#Prompt: Given 2 integer arrays (ranks and suits) where the ith card has a rank of ranks[i] and a suit of suits[i], 
#return a string representing the best type of poker hand you can make

def bestHand(ranks, suits):
    #Check for flush first
    flush = True
    for i in range(1,len(suits)):
        if suits[i] != suits[i-1]:
            flush = False
    if flush:
        return "Flush"

    #Check for total occurances of each rank and return if three of a kind or pair found
    cards = {}
    for i in range(len(ranks)):
        if ranks[i] not in cards:
            cards[ranks[i]] = 1
        else:
            cards[ranks[i]] += 1

    pair = False
    for i in cards:
        if cards[i] >= 3:
            return "Three of a Kind"
        elif cards[i] == 2:
            pair = True
    if pair:
        return "Pair"

    #There must be a card with highest value out of the remaining unique cards
    return "High Card"
        


#Test Casses
assert bestHand([13,2,3,1,9], ["a","a","a","a","a"]) == "Flush", "Solution: 'Flush'"
assert bestHand([4,4,2,4,4], ["d","a","a","b","c"]) == "Three of a Kind",  "Solution: 'Three of a Kind'"
assert bestHand([10,10,2,12,9], ["a","b","c","a","d"]) == "Pair",  "Solution: 'Pair'"
assert bestHand([3,11,2,12,9], ["a","b","c","e","d"]) == "High Card", "Solution: 'High Card'"
print("All tests passed.")