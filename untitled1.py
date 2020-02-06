class Solution(object):
    def isSolvable(self, words, result):
        unique = set()
        for word in words:
            for letter in word:
                unique.add(letter)
        for letter in result:
            unique.add(letter)
        unique = sorted(unique)
        assignedinv = [None] * 10
        assigned = {}
        ordA = ord('A')
        
        K = max(len(word) for word in words)
        K = max(K, len(result))
        def search(ii, bal):
            if ii == K:
                if bal: return False
                # check 0 prefix
                for word in words:
                    if len(word) > 1:
                        first = word[0]
                        if assigned[first] == 0:
                            return False
                if len(result) > 1:
                    first = result[0]
                    if assigned[first] == 0:
                        return False
                return True

            # 'S'-> 6, 'I'->5, 'X'->0, 'E'->8,
            # 'V'->7, 'N'->2, 'T'->1, 'W'->'3', 'Y'->4
            
            unassigned = [0] * 26
            for word in words:
                if ii >= len(word): continue
                letter = word[len(word) - 1 - ii]
                d = assigned.get(letter, -1)
                if d == -1:
                    unassigned[ord(letter) - ordA] += 1
                else:
                    bal += d
            
            if ii < len(result):
                letter = result[len(result) - 1- ii]
                d = assigned.get(letter, -1)
                if d == -1:
                    unassigned[ord(letter) - ordA] -= 1
                else:
                    bal -= d
            
            free = [d for d, have in enumerate(assignedinv) if have is None]
            toassign = [ci for ci, x in enumerate(unassigned) if x]


            for choice in itertools.permutations(free, len(toassign)):
                # assign digit choice[i] to charindex toassign[i]
                
                baldelta = 0
                for i, d in enumerate(choice):
                    ci = toassign[i]
                    c = chr(ordA + ci)
                    assignedinv[d] = c
                    assigned[c] = d
                    baldelta += unassigned[ci] * d
                #print 'c', choice, baldelta
                bal += baldelta
                if bal % 10 == 0:
                    #if ii == 0: print ("!", choice)
                    if search(ii+1, bal // 10): return True
                bal -= baldelta
                for i, d in enumerate(choice):
                    ci = toassign[i]
                    c = chr(ordA + ci)
                    assignedinv[d] = None
                    del assigned[c]
            if len(toassign) == 0 and bal % 10 == 0:
                search(ii+1, bal // 10)
            return False
        
        return search(0, 0)
        
        