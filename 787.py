class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        INFINITO = float('inf')
        distancia = [INFINITO] * n
        distancia[src] = 0
        
        for _ in range(k + 1):
            temp = distancia.copy()
            
            for origem, destino, preco in flights:
                if distancia[origem] != INFINITO and distancia[origem] + preco < temp[destino]:
                    temp[destino] = distancia[origem] + preco
            
            distancia = temp
        
        return -1 if distancia[dst] == INFINITO else distancia[dst]