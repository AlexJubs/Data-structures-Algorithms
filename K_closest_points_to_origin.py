class Solution:        
    def kClosest(self, allLocations, truckCapacity):
        # WRITE YOUR CODE HERE
        if len(allLocations) == truckCapacity: return allLocations
        mapping = dict()
        dists = []
        for loc in allLocations:
            dists.append(self.dist(loc[0],loc[1]))
            if mapping.get(self.dist(loc[0],loc[1])) == None:
                mapping[self.dist(loc[0],loc[1])] = str(loc[0]) + '|' + str(loc[1])
            elif mapping.get(self.dist(loc[0],loc[1])) != None: 
                mapping[self.dist(loc[0],loc[1])] = mapping[self.dist(loc[0],loc[1])] + '*' + str(loc[0]) + '|' + str(loc[1])

        dists = list(set(dists))
        dists.sort()
        res = []
        for i in range(truckCapacity):
            if '*' in mapping[dists[i]]:
                temp = mapping[dists[i]].split('*')
                for x in temp:
                    res.append([int(x[:x.find('|')]),int(x[x.find('|')+1:])])
            else:
                x = mapping[dists[i]]
                res.append([int(x[:x.find('|')]),int(x[x.find('|')+1:])])

        return (res[:truckCapacity])

    def dist(self,x,y):
        return (x**2 + y**2)