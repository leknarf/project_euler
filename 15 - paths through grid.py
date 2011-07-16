def _routes():
    results = {}
    def r(x, y):
        if x == 0 or y == 0:
            return 1
        if (x, y) not in results:
            results[(x,y)] = r(x-1, y) + r(x, y-1)
        return results[(x,y)]
    return r
routes = _routes()
                
print(routes(20,20))