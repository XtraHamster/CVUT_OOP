# Brute force

# Cross table with airplane ticket prices
prices = [
        [0,4270,1799,2602,10236],
        [4270,0,2017,9873,14300],
        [1799, 3922, 0, 0, 12110],
        [2602, 9873, 2435, 0, 7503],
        [10236, 14300, 12110, 7503, 0]
       ]

# List of cities
cities = ["Prague", "New York", "London", "Moscow", "Bejing"]

def sorter(e):
    return e['total']

def tracker(fr, to):
    fr = cities.index(fr)
    to = cities.index(to)
    destination = cities[to]
    result=[]
    for i in range(len(cities)):
        if prices[fr][i] != 0:
            if cities[i] == destination:
                result.append({'routes':2,'total':prices[fr][i],'info':(f"from {cities[fr]} to {cities[i]} for {prices[fr][i]} totally = {prices[fr][i]} CZK")})
            for ii in range(len(cities)):
                if prices[i][ii] != 0:
                    if cities[ii] == destination:
                        result.append({'routes':3,'total':(prices[fr][i]+prices[i][ii]),'info':(f"from {cities[fr]} to {cities[i]} to {cities[ii]} for {prices[fr][i]} and {prices[i][ii]} totally = {prices[fr][i]+prices[i][ii]} CZK")})
                    # All code below is not needed for this application. It should be used when more cities would be added.
                    for iii in range(len(cities)):
                        if prices[ii][iii] != 0:
                            if cities[iii] == destination:
                                result.append({'routes':4,'total':(prices[fr][i]+prices[i][ii]+prices[ii][iii]),'info':(f"from {cities[fr]} to {cities[i]} to {cities[ii]} to {cities[iii]} for {prices[fr][i]} and {prices[i][ii]} and {prices[ii][iii]} totally = {prices[fr][i]+prices[i][ii]+prices[ii][iii]} CZK")})             
                            for iv in range(len(cities)):
                                if prices[iii][iv] != 0:
                                    if cities[iv] == destination:
                                        result.append({'routes':5,'total':(prices[fr][i]+prices[i][ii]+prices[ii][iii]+prices[iii][iv]),'info':(f"from {cities[fr]} to {cities[i]} to {cities[ii]} to {cities[iii]} to {cities[iv]} for {prices[fr][i]} and {prices[i][ii]} and {prices[ii][iii]} and {prices[iii][iv]}")})
    
    result.sort(key=sorter)
    return f"The best route is through {result[0]['routes']} cities {result[0]['info']}"

x = tracker("Prague", "London")
print(x)
y = tracker("London", "Moscow")
print(y)
z = tracker("Prague", "Prague")
print(z)