#Time_Complexity: O(n)
#Space_Complexity: O(n) - size of hashset

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        hashset = [0]*256   #Initializing a hashset as an array of 0s for 256 because it 's' may contain alphabets, digits, symbols and spaces
        maximum = 0 #Initializing maximum as 0
        start = 0   #Initializing start as 0
        for end in range(n):    #Continue the loop until it reaches the end of the string 's'
                if (hashset[ord(s[end])] == True):  #If the incoming element is already present in the hashset
                    while s[start] != s[end]:   #Continue till the start element is equal to the end element
                        hashset[ord(s[start])] = False  #Change the outgoing element to False
                        start += 1  #Increment start by 1 till the condition satisfies
                    start += 1  #Increment the start by 1 to start from the next index
                else:   #Else check the maximum with the size of the window i.e., difference of end and start and adding it by 1
                    maximum = max(maximum, end-start + 1)
                    hashset[ord(s[end])] = True #Set the incoming elements as True in hashset
    
        return maximum  #Return maximum which will give the length of the longest substring