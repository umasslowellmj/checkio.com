class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        if n==1:
            return ["1"]
        for i in range(1,n+1):
            if i%3==0 and i%5!=0:
                ret.append("Fizz")
            elif i%5==0 and i%3!=0:
                ret.append("Buzz")
            elif i%15==0:
                ret.append("FizzBuzz")
            else:
                ret.append(str(i))
        return ret
                  
            
