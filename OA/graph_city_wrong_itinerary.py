"""
给定一个graph，graph的node表示city，
原话是给你两个方法 getAllCities和getNeightorByCity，
总之就是给你一个graph。City的名字有规则，
一定是AAA这样的大写英文字母，类似于机场的缩写，长度为3。
然后给你一个String表示Itinerary，这个itinerary是错误的，有两种错误的情况，
第一种是city的名字写错了，比如城市是AAA，但是写成了AAB。
第二种错误是itinerary写的是从AAA到BBB，但是实际上graph里头这两个城市并不联通。
要求是把这个itinerary改成正确的。之后给了一个概念，就是更改itinerary有cost，
更改一个英文字母的cost就是1，比如第一种情况AAA -> AAB的cost是1，
第二种情况 AAA -> BBB改成 AAA -> CCC -> BBB的cost是3. 
最终的要求是把itinerary改正确，并且要求cost最低。
"""

# Dijkstra's algorithm
# heap will save (cost, index in itenerary, path)
import heapq
def repairItinerary(graph, itinerary):
    if not itinerary:
        return []
        
    heap = []
    for city in graph:  # equivalent to getAllCities()
        heapq.heappush(heap, (getCost(city, itinerary[0]), 0, [city]))
    
    while heap:
        cost, i, path = heapq.heappop(heap)
        if i == len(itinerary)-1:
            return path
        for neighbor in graph[path[-1]]: # getAllChildren(city)
            heapq.heappush(heap, 
                (cost+getCost(neighbor, itinerary[i+1]), i+1, path+[neighbor]))

def getCost(city1, city2):
    if len(city1) != len(city2):
        raise ValueError("City must have and only have three letters.")
    cost = 0
    for i in range(len(city1)):
        if city1[i] != city2[i]:
            cost += 1
    return cost

if __name__ == "__main__":
    graph = {"AAA": ["BBB", "BBE", "CCC"], "BBB":["CEE"], "BBE":["CCC"]}
    itinerary1 = ["AAA", "BBB", "CCC"]
    itinerary2 = ["BBA", "BBB", "CCC"]

    print(repairItinerary(graph, itinerary1))
    print(repairItinerary(graph, itinerary1))
    
    