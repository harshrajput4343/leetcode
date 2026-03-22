class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        result = 0
        for i , ticket in enumerate(tickets):
            if i <= k:
                result += min(ticket, tickets[k])

            else:
                result += min(ticket, tickets[k]-1)

        return result



# target = tickets[k]   to handle edge cases

# for i, ticket in enumerate(tickets):
#    if i <= k:
#        result += min(ticket, target)
#    else:
#        result += min(ticket, max(target - 1, 0))