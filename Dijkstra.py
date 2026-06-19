
from collections import defaultdict
import heapq
def network_delay_time(times,n,k):
 g=defaultdict(list)
 for u,v,w in times:
        g[u].append((v,w))
 dist=[float("inf")]*n
 pq=[]
 heapq.heappush(pq,(0,k))
 dist[k-1]=0
 while pq:
    w,u=heapq.heappop(pq)
    if w>dist[u-1]:
        continue
    for nei,wei in g[u]:
        if dist[u-1]+wei<dist[nei-1]:
            dist[nei-1]=dist[u-1]+wei
            heapq.heappush(pq,(dist[nei-1],nei))
 mini=max(dist)
 if mini!=float("inf"):
        return mini
 return -1
print(network_delay_time([[2,1,1],[2,3,1],[3,4,1]],4,2))