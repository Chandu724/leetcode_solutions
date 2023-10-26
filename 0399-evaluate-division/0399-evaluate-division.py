class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        def dfs(k, v, visit):
            print(k, v, visit)
            if k not in gr or v not in gr:
                return -1
            if v in gr[k]:
                return gr[k][v]
            visit.append(k)
            for z in gr[k]:
                print("here")
                if z not in visit:
                    r = dfs(z, v, visit)
                    if r != -1:
                        return gr[k][z]*r
            return -1
            
        
        gr = defaultdict(dict)
        
        for (a, b), v in zip(equations, values):
            gr[a][b] = v
            gr[b][a] = 1.0 / v
            
        print(gr)
            
        res = []
        for i in range(len(queries)):
            x, y = queries[i]
            res.append(dfs(x,y,[]))
            
        print(res)
        return res
            
                