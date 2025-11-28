class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        trabalhos = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        n = len(trabalhos)

        dp = [0] * n
        
        import bisect
        fins = [trabalho[1] for trabalho in trabalhos]

        for i in range(n):
            inicio, fim, lucro = trabalhos[i]

            indice = bisect.bisect_right(fins, inicio) - 1

            nao_pegar = dp[i-1] if i > 0 else 0

            pegar = lucro + (dp[indice] if indice >= 0 else 0)

            dp[i] = max(nao_pegar, pegar)

        return dp[-1]
