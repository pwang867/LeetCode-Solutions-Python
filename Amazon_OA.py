import heapq
import collections

def extract_words(request):
    # return {word in lower case: cnt}
    request = request.strip().lower()
    if request and not request[-1].isalpha():
        request = request[:-1]
    words = request.split()
    return collections.Counter(words)
    
def popularNFeatures(numFeatures, topFeatures, possibleFeatures, 
                    numFeatureRequests, featureRequests):
    # WRITE YOUR CODE HERE
    possibleFeatures = [s.lower() for s in possibleFeatures]
    dic = {s: 0 for s in possibleFeatures}
    for request in featureRequests:
        words = extract_words(request)
        for word in words:
            if word in dic:
                dic[word] += 1
    pairs = [(-cnt, word) for word, cnt in dic.items() if cnt > 0]
    heapq.heapify(pairs)
    res = []
    for _ in range(topFeatures):
        cnt, word = heapq.heappop(pairs)
        res.append(word)
    return res
