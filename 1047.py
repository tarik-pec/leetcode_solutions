#1047. Remove All Adjacent Duplicates In String

#You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

#We repeatedly make duplicate removals on s until we no longer can.

#Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.


class Solution:
    def removeDuplicates(self, s: str) -> str:
        char_index = 0
        last_index_of_curr_s = len(s)-2
        #Begin checking adjacent duplicates from the start of s
        while char_index <= last_index_of_curr_s:
            #if an adjacent duplicate is found, remove the duplicate then check for another duplicate at the same position
            if s[char_index]==s[char_index+1]:
                duplicate_found = True
                while duplicate_found:
                    #remove duplicate and update indicies
                    s = s[:char_index] + s[char_index+1:]
                    s = s[:char_index] + s[char_index+1:]
                    if char_index != 0:
                        char_index -=  1
                    last_index_of_curr_s -= 2
                    if s == '':
                        return s
                    #if char_index is at last index, return s (no duplicate can be found as there is no next char), otherwise check for another duplicate at the same position. If yes we will loop again to remove (and check again), otherwise change flag to exit loop.
                    if char_index <= last_index_of_curr_s:
                        if s[char_index] != s[char_index+1]:
                            duplicate_found = False
                    else:
                        return s
            else:
                char_index += 1
        return s
                        
