class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        ProfToDif = {}
        for i in range(len(difficulty)):
            if profit[i] in ProfToDif.keys():
                if difficulty[i] > ProfToDif[profit[i]]:
                    continue
            ProfToDif.update({profit[i]:difficulty[i]})

        ProfToDif = dict(sorted(ProfToDif.items(), reverse = True))
        worker.sort()
        profits = 0

        def binary_search(difficulty, left,right, skill):
            while right >= left:
                mid = (left + right) //2
                if skill[mid] == difficulty:
                    return(mid)
                elif skill[mid] > difficulty:
                    temp[0] = mid
                    right =  mid - 1
                else:
                    left = mid + 1
            return(-1)
 
        temp = [-1]
        for Profit in ProfToDif:
            l = 0
            r = len(worker) - 1
            temp[0] = -1
            x = binary_search(ProfToDif[Profit], l, r, worker)
            if x >=0:
                y = worker.index(worker[x])
                profits += Profit*(len(worker)-y)
                worker = worker[:y]
            elif temp[0] >=0:
                profits += Profit*(len(worker)-temp[0])
                worker = worker[:temp[0]]
            
        return(profits)
