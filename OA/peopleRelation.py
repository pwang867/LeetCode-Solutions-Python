from collections import defaultdict

class PeopleRelation:
    def getRelationSequence(self, relations, name1, name2):
        dic = defaultdict(list)
        for person1, relation, person2 in relations:
            dic[person1].append((person2, relation))
        res = []
        self.dfs(dic, name1, [name1], set(), name2, res)
        return res
        
    def dfs(self, dic, cur, path, visited, target, res):
        # cur means we are visiting cur person right now
        # path is like: ["person1", " relation1, person2", " relation3, person3"]
        # visited is the visited persons along the path, not including cur yet
        # visited is important to avoid infinite loops
        if cur == target:
            res.append("".join(path))
        if cur not in dic:
            return
        
        visited.add(cur)
        for person, relation in dic[cur]:
            if person not in visited:
                path.append(" "+relation+" "+person)
                self.dfs(dic, person, path, visited, target, res)
                path.pop()      # backtrack
        visited.remove(cur)     # backtrack


if __name__ == "__main__":
    relations = [["A", "brother", "B"],
                 ["A", "son", "C"],
                ["D", "wife", "C"],
                ["B", "daughter", "C"],
                ["C","father", "A"]]
                
    print(PeopleRelation().getRelationSequence(relations, "A", "C"))
    
    
    