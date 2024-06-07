class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return(False)
        hand = sorted(hand)

        n = int(len(hand)/groupSize)
        j = 0
        i = 0

        while i < len(hand):
            j = hand[i]
            for k in range(groupSize):
                if j not in hand:
                    return(False)
                hand.pop(hand.index(j))
                j+=1

        return(True)
