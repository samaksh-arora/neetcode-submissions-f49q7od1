class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        #Array where hand[i] = value written on that card
        #integer groupSize
        #rearrange into groups of size = groupSize
        #&& them have be in consecutive increasing order
        #If possible return true, if not return false
        #how to begin

        #we could take approach of longest consecutive sequenceand apply to this
        #when the length reaches groupSize, you move on to the next,
        #we can use hash map to make sure we dont reuse something we cant
        #if len(hand) % groupSize != 0 return False
        #make a frequency map
        #now start iterating through hand, if hand[i] - 1 not in map or map[hand[i]-1] == 0:
        # Then initialize length = 1
        #while hands[i] + length in map and map[hand[i]+length] > 0 and length<groupSize: length += 1
        #hands[i] + length frequency reduced from map
        #if length!=groupSize return False?

        hand.sort()
        if (len(hand) % groupSize) != 0:
            return False
        frequencyMap ={}
        for card in hand:
            frequencyMap[card] = frequencyMap.get(card,0) + 1
       
        for card in hand:
            
            if (card-1) not in frequencyMap or frequencyMap[card-1] == 0 and frequencyMap[card]>0:
                
                length = 1
                
                frequencyMap[card] -= 1
                while (card + length) in frequencyMap and frequencyMap[card+length] > 0 and length < groupSize:
                    frequencyMap[card+length] -= 1
                    
                    length += 1
        
               
                if length!= groupSize:
                    return False
        
        return True

                
