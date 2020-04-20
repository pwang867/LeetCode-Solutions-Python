import collections


class FileNode:
    def __init__(self, val=None):
        self.val = val
        self.children = collections.defaultdict(FileNode)


class FileSystem(object):

    def __init__(self):
        self.root = FileNode()

    def createPath(self, path, value):
        """
        :type path: str
        :type value: int
        :rtype: bool
        """
        path_list = self.parse_path(path)
        if not path_list:
            return False
        node = self.root
        for i in range(len(path_list) - 1):
            name = path_list[i]
            if name not in node.children:
                return False  # parent path doesn't exist
            else:
                node = node.children[name]
        if path_list[-1] in node.children:
            return False  # when path already exists
        else:
            node.children[path_list[-1]] = FileNode(value)
            return True

    def get(self, path):
        """
        :type path: str
        :rtype: int
        """
        path_list = self.parse_path(path)
        if not path:
            return -1
        node = self.root
        for name in path_list:
            if name not in node.children:
                return -1
            else:
                node = node.children[name]
        return node.val

    def parse_path(self, path):
        # path = path.strip()
        if not path:
            return []
        # if path[0] == "/":
        #     path = path[1:]
        # if path and path[-1] == "/":
        #     path = path[:-1]
        path_list = path.split("/")
        return path_list[1:]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)


"""
You are asked to design a file system which provides two functions:

createPath(path, value): Creates a new path and associates a value to it if possible and returns True. 
Returns False if the path already exists or its parent path doesn't exist.
get(path): Returns the value associated with a path or returns -1 if the path doesn't exist.
The format of a path is one or more concatenated strings of the form: / followed by one or more 
lowercase English letters. For example, /leetcode and /leetcode/problems are valid paths while an empty string 
and / are not.

Implement the two functions.

Please refer to the examples for clarifications.

 

Example 1:

Input: 
["FileSystem","createPath","get"]
[[],["/a",1],["/a"]]
Output: 
[null,true,1]
Explanation: 
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/a", 1); // return true
fileSystem.get("/a"); // return 1
Example 2:

Input: 
["FileSystem","createPath","createPath","get","createPath","get"]
[[],["/leet",1],["/leet/code",2],["/leet/code"],["/c/d",1],["/c"]]
Output: 
[null,true,true,2,false,-1]
Explanation: 
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/leet", 1); // return true
fileSystem.createPath("/leet/code", 2); // return true
fileSystem.get("/leet/code"); // return 2
fileSystem.createPath("/c/d", 1); // return false because the parent path "/c" doesn't exist.
fileSystem.get("/c"); // return -1 because this path doesn't exist.
 

Constraints:

The number of calls to the two functions is less than or equal to 10^4 in total.
2 <= path.length <= 100
1 <= value <= 10^9
NOTE: create method has been changed on August 29, 2019 to createPath. Please reset to default code 
definition to get new method signature.
"""