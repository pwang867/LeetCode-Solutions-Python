

class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        if not folder:
            return []
        if len(folder) == 1:
            return folder
        folder.sort()
        res = [folder[0]]
        for i in range(1, len(folder)):
            if not self.isSub(res[-1], folder[i]):  # mistake: folder[i].startswith(start[-1])
                res.append(folder[i])
        return res
    
    def isSub(self, folder1, folder2):
        folder1 = folder1.split("/")
        folder2 = folder2.split("/")
        return folder2[:len(folder1)] == folder1


"""
5231. Remove Sub-Folders from the Filesystem

Given a list of folders, remove all sub-folders in those folders and return in any order the folders after removing.

If a folder[i] is located within another folder[j], it is called a sub-folder of it.

The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. For example, /leetcode and /leetcode/problems are valid paths while an empty string and / are not.

 

Example 1:

Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
Output: ["/a","/c/d","/c/f"]
Explanation: Folders "/a/b/" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.
Example 2:

Input: folder = ["/a","/a/b/c","/a/b/d"]
Output: ["/a"]
Explanation: Folders "/a/b/c" and "/a/b/d/" will be removed because they are subfolders of "/a".
Example 3:

Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
Output: ["/a/b/c","/a/b/ca","/a/b/d"]
 

Constraints:

1 <= folder.length <= 4 * 10^4
2 <= folder[i].length <= 100
folder[i] contains only lowercase letters and '/'
folder[i] always starts with character '/'
Each folder name is unique.
"""
