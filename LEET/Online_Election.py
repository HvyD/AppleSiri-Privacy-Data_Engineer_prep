"""
In an election, the i-th vote was cast for persons[i] at time times[i].

Now, we would like to implement the following query function: TopVotedCandidate.q(int t) will return the number of the person that was leading the election at time t.

Votes cast at time t will count towards our query.  In the case of a tie, the most recent vote (among tied candidates) wins.



Example 1:

Input: ["TopVotedCandidate","q","q","q","q","q","q"], [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
Output: [null,0,1,1,0,0,1]
Explanation:
At time 3, the votes are [0], and 0 is leading.
At time 12, the votes are [0,1,1], and 1 is leading.
At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
This continues for 3 more queries at time 15, 24, and 8.

"""
from bisect import bisect
class TopVotedCandidate:

    def __init__(self, persons, times):
        self.time_interval = times
        self.res = []
        max_vote = 0
        count_vote = {}
        for i, p in enumerate(persons):
            count_vote[p] = count_vote.get(p, 0) + 1
            if count_vote[p] >= max_vote:
                max_vote = count_vote[p]
                recent_ppl = p
            self.res.append(recent_ppl)

    def q(self, t):
        pos = bisect(self.time_interval, t)
        return self.res[pos-1]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)

obj = TopVotedCandidate()
assert(obj.q(["TopVotedCandidate","q","q","q","q","q","q"], [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]) ==  [null,0,1,1,0,0,1] )
