def max_prob_to_destination(start,end,edges,prob):
    g=defaultdict(list)
    for (u,v),p in zip(edges,prob):
        g[u].append((v,p))
        g[v].append((u,p))
    dist=[0]*n
    pq=[]
    heapq.heappush(pq,(-1,start))
    dist[start]=1
    while pq:
        p,u=heapq.heappop(pq)
        p=-p
        if p<dist[u]:
            continue
        for nei,wei in g[u]:
            if dist[u]*wei>dist[nei]:
                dist[nei]=dist[u]*wei
                heapq.heappush(pq,(-dist[nei],nei))
    return dist[end]
print(max_prob_to_destination(0,2,[[0,1],[1,2],[0,2]],[0.5,0.5,0.2]))