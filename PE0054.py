#PE 54

cardDict = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

def score(hand):
    points = 0
    royal = testRoyal(hand)
    stFlush = testStFlush(hand)
    FourKind = testFourKind(hand)
    FullHouse = testFullHouse(hand)
    flush = testFlush(hand)
    straight = testStraight(hand)
    threeKind = testThreeKind(hand)
    twoPair = testTwoPair(hand)
    pair = testPair(hand)
    highCard = testHighCard(hand)

    bestHand = []
    if(len(royal) > 0):
        bestHand = royal
    elif(len(stFlush) > 0):
        bestHand = stFlush
    elif(len(FourKind) > 0):
        bestHand = FourKind
    elif(len(FullHouse) > 0):
        bestHand = FullHouse
    elif(len(flush) > 0):
        bestHand = flush
    elif(len(straight) > 0):
        bestHand = straight
    elif(len(threeKind) > 0):
        bestHand = threeKind
    elif(len(twoPair) > 0):
        bestHand = twoPair
    elif(len(pair) > 0):
        bestHand = pair
    elif(len(highCard) > 0):
        bestHand = highCard
    
    for i in range(len(bestHand)):
        points += 14**(len(bestHand) - i) * bestHand[i]

    return bestHand

def getNums(hand):
    nums = []
    for card in hand:
        nums.append(cardDict[card[0]])
    return nums

def getSuits(hand):
    suits = []
    for card in hand:
        suits.append(card[1])
    return suits

def testRoyal(hand):
    nums = getNums(hand)
    suits = getSuits(hand)
    if len(set(suits)) == 1:
        if(set(nums) == set([10, 11, 12, 13, 14])):
            return [14, 14, 14, 14, 14, 14]
            
    return []

def testStFlush(hand):
    nums = getNums(hand)
    suits = getSuits(hand)
    if len(set(suits)) == 1:
        if(max(set(nums)) - min(set(nums)) == 4):
            return [13, max(set(nums)), max(set(nums)), max(set(nums)), max(set(nums)), max(set(nums))]

    return []

def testFourKind(hand):
    nums = getNums(hand)
    if(len(set(nums)) == 2):
        if(nums.count(nums[0]) == 4):
            for x in nums:
                if x != nums[0]:
                    otherVal = x
            return [12, nums[0], nums[0], nums[0], nums[0], otherVal]
        elif(nums.count(nums[1]) == 4):
            for x in nums:
                if x!= nums[1]:
                    otherVal = x
            return [12, nums[1], nums[1], nums[1], nums[1], otherVal]

    return []

def testFullHouse(hand):
    nums = getNums(hand)
    if(len(set(nums)) == 2):
        if(nums.count(nums[0]) == 3):
            for x in nums:
                if x != nums[0]:
                    otherVal = x
            return [11, nums[0], nums[0], nums[0], otherVal, otherVal]
        elif(nums.count(nums[1]) == 3):
            for x in nums:
                if x != nums[1]:
                    otherVal = x
            return [11, nums[1], nums[1], nums[1], otherVal, otherVal]
        elif(nums.count(nums[2]) == 3):
            for x in nums:
                if x != nums[2]:
                    otherVal = x
            return [11, nums[2], nums[2], nums[2], otherVal, otherVal]

    return []

def testFlush(hand):
    nums = getNums(hand)
    suits = getSuits(hand)
    if(len(set(suits)) == 1):
        return [10, *reversed(sorted(nums))]

    return []

def testStraight(hand):
    nums = getNums(hand)
    if(len(set(nums)) == 5):
        if(max(nums) - min(nums) == 4):
            return [9, *reversed(sorted(nums))]

    return []

def testThreeKind(hand):
    nums = getNums(hand)
    if(len(set(nums)) == 3):
        if(nums.count(nums[0]) == 3):
            bigVal = 0
            smallVal = 100
            for x in nums:
                if x!= nums[0]:
                    bigVal = max(bigVal, x)
                    smallVal = min(smallVal, x)
            return [8, nums[0], nums[0], nums[0], bigVal, smallVal]
        elif(nums.count(nums[1]) == 3):
            bigVal = 0
            smallVal = 100
            for x in nums:
                if x!= nums[1]:
                    bigVal = max(bigVal, x)
                    smallVal = min(smallVal, x)
            return [8, nums[1], nums[1], nums[1], bigVal, smallVal]
        elif(nums.count(nums[2]) == 3):
            bigVal = 0
            smallVal = 100
            for x in nums:
                if x!= nums[2]:
                    bigVal = max(bigVal, x)
                    smallVal = min(smallVal, x)
            return [8, nums[2], nums[2], nums[2], bigVal, smallVal]

    return []

def testTwoPair(hand):
    nums = getNums(hand)
    numPairs = 0
    pairElements = []
    nonPair = -1
    for x in set(nums):
        if(nums.count(x) == 2):
            numPairs += 1
            pairElements.append(x)
        else:
            nonPair = x
    if(numPairs == 2):
        return [7, max(pairElements), max(pairElements), min(pairElements), min(pairElements), nonPair]

    return []

def testPair(hand):
    nums = getNums(hand)
    pairElement = -1
    nonPairs = []
    for x in set(nums):
        if(nums.count(x) == 2):
            pairElement = x
        else:
            nonPairs.append(x)
    if(pairElement > 0):
        return [6, pairElement, pairElement, *reversed(sorted(nonPairs))]
    
    return []

def testHighCard(hand):
    nums = getNums(hand)
    return [5, *reversed(sorted(nums))]


if(__name__ == "__main__"):
    hands_file = open("PE0054_hands.txt")
    hands = hands_file.read()

    matches = hands.split("\n")

    p1Wins = 0
    hand = 1
    testers = [25]
    for match in matches:
        cards = match.split(" ")
        player1, player2 = cards[:5], cards[5:]
        p1score = score(player1)
        p2score = score(player2)
        if(hand in testers):
            print(player1, p1score)
            print(player2, p2score)
        for i in range(len(p1score)):
            if(p1score[i] > p2score[i]):
                p1Wins += 1
                break
            elif(p2score[i] > p1score[i]):
                break
        hand += 1

    print(p1Wins)



