 # "/".join([""]) is ""
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        
        # "/b/c/" - directory 'b ' - > directory 'c '
        # "." - current directory
        # "./" - current directory
        # "../" - one directory up
        # e.g
        # "/" : root directory
        # "b/c/../" : it will go from c to b
        # "c/b/./" : it is still in directory b
        
        path = path.split("/")
        new_path = []  # mistake: new_path = ["/"]
        for item in path:
            if item == "." or item == "":
                continue
            elif item == "..":
                if len(new_path) == 0:
                    continue
                else:
                    new_path.pop()
            else:
                new_path.append(item)
        
        return "/" + "/".join(new_path)  

"""
Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.

In a UNIX-style file system, a period . refers to the current directory. Furthermore, a double period .. moves the directory up a level. For more information, see: Absolute path vs relative path in Linux/Unix

Note that the returned canonical path must always begin with a slash /, and there must be only a single slash / between two directory names. The last directory name (if it exists) must not end with a trailing /. Also, the canonical path must be the shortest string representing the absolute path.

 

Example 1:

Input: "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.
"""
