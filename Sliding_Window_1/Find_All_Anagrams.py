class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #Edge case
        if len(p)>len(s):   #If the length of p is greater than length of s return an empty array   
            return []
        result = []         #Initialize result as an empty array
        pCount={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}    #Initialize pCount as letter dictionary with all the letters with values 0
        ssCount={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}   #Initialize ssScount as letter dictionary with the letters with value 0
        for ch in p:    #For every character in p
            if ch in pCount:    #If ch is already in pCount add 1 to that ch in pCount
                pCount[ch]+=1 
            else:   #Else initialize 1 to that ch in pCount
                pCount[ch]=1 
    
        start =0    #Initialize start as 0

        #Building the window
        for end in range(len(p)): #Continue till the length of p
            if s[end] in pCount:    #If s[end] is already in pCount add 1 to that ch in ssCount
                ssCount[s[end]]+=1
        if pCount==ssCount:     #If pCount is equal to ssCount append start into result
            result.append(start)


        #Sliding Window
        for end in range(len(p),len(s)):    #Continue till the length of p and length of s
            if s[end] in pCount:    #If s[end] is already in pCount add 1 to that element in ssCount[s[end]]
                ssCount[s[end]]+=1

            if s[start] in ssCount:     #If s[start] is already in ssCount decrement 1 to that element in ssCount[s[start]]
                ssCount[s[start]]-=1
            start+=1    #Increment start by 1

            if pCount==ssCount:     #If pCount is equal to ssCount appand start to result
                result.append(start)


        return result   #Return result