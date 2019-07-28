from os.path import join, dirname, realpath


class TreeNode:
    def __init__(self, int_list):
        self._children = []
        self._metadata = []
        child_count = int_list.pop(0)
        metadata_count = int_list.pop(0)
        while child_count > 0:
            child_count -= 1
            self._children.append(TreeNode(int_list))
        while metadata_count > 0:
            metadata_count -= 1
            self._metadata.append(int_list.pop(0))

    def value(self):
        if self._children:
            # Node has children
            value = 0
            for i in self._metadata:
                if i < 1 or i > len(self._children):
                    continue
                else:
                    value += self._children[i-1].value()
            return value
        else:
            # Node does not have any child, return sum of metadata entries
            return sum(self._metadata)


with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    file_input = f.readline()

file_input = [int(x) for x in file_input.split()]
tree = TreeNode(file_input)
print(tree.value())
