from collections import defaultdict


class FileNode:
    def __init__(self):
        self.is_file = False
        self.children = defaultdict(FileNode)
        self.file_content = ""


class FileSystem(object):

    def __init__(self):
        self.root = FileNode()

    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        arr = self._clean_path(path)
        node = self.root
        for name in arr:
            node = node.children[name]
        if node.is_file and arr:
            return [arr[-1]]  # mistake: return arr[-1]
        else:
            return sorted(node.children.keys())

    def _clean_path(self, path):
        if not path:
            return []
        if path[-1] == "/":
            path = path[:-1]
        if path and path[0] == "/":
            path = path[1:]
        if not path:
            return []
        else:
            return path.split('/')

    def mkdir(self, path):
        """
        :type path: str
        :rtype: None
        """
        arr = self._clean_path(path)
        node = self.root
        for name in arr:
            node = node.children[name]

    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: None
        """
        arr = self._clean_path(filePath)
        node = self.root
        for name in arr:
            node = node.children[name]
        if not node.is_file:
            node.is_file = True
        node.file_content += content

    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        arr = self._clean_path(filePath)
        node = self.root
        for name in arr:
            node = node.children[name]
        return node.file_content

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)


"""
Design an in-memory file system to simulate the following functions:

ls: Given a path in string format. If it is a file path, return a list that only contains this file's name. If it is a directory path, return the list of file and directory names in this directory. Your output (file and directory names together) should in lexicographic order.

mkdir: Given a directory path that does not exist, you should make a new directory according to the path. If the middle directories in the path don't exist either, you should create them as well. This function has void return type.

addContentToFile: Given a file path and file content in string format. If the file doesn't exist, you need to create that file containing given content. If the file already exists, you need to append given content to original content. This function has void return type.

readContentFromFile: Given a file path, return its content in string format.

 

Example:

Input: 
["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
[[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]

Output:
[null,[],null,null,["a"],"hello"]

Explanation:
filesystem
 

Note:

You can assume all file or directory paths are absolute paths which begin with / and do not end with / except that the path is just "/".
You can assume that all operations will be passed valid parameters and users will not attempt to retrieve file content or list a directory or file that does not exist.
You can assume that all directory names and file names only contain lower-case letters, and same names won't exist in the same directory.
"""