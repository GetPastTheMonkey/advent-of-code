from utils import get_input_lines


class Directory:
    def __init__(self, parent):
        self.parent = parent if parent is not None else self
        self._children = dict()
        self._files = dict()
        self._size = None

    def __contains__(self, item):
        return item in self._children

    def __getitem__(self, item):
        return self._children[item]

    def __setitem__(self, key, value):
        if self._size is not None:
            raise ValueError("Cannot add new children after asking for size")
        self._children[key] = value

    @property
    def size(self):
        if self._size is None:
            my_size = sum(self._files.values())
            for child in self._children.values():
                my_size += child.size
            self._size = my_size

        return self._size

    @property
    def children(self):
        return self._children

    def add_file(self, name, size):
        self._files[name] = size

    def get_sizes_as_list(self):
        sizes = [self.size]

        for v in self._children.values():
            sizes.extend(v.get_sizes_as_list())

        return sizes


def build_fs():
    root_dir = Directory(None)
    current_dir = root_dir

    for line in get_input_lines(__file__):
        commands = line.split(" ")
        if commands[0] == "$":
            if commands[1] == "cd":
                name = commands[2]

                if name == "/":
                    # Go to root dir
                    current_dir = root_dir
                elif name == "..":
                    # Go to parent dir
                    current_dir = current_dir.parent
                elif name in current_dir:
                    # Child exists, go to child
                    current_dir = current_dir[name]
                else:
                    # Child does not exist, create child, then go to child
                    new_dir = Directory(current_dir)
                    current_dir[name] = new_dir
                    current_dir = new_dir
            elif commands[1] == "ls":
                pass
            else:
                raise ValueError(f"Unsupported command: {commands[1]}")
        else:
            is_dir_or_size, name = commands

            if is_dir_or_size == "dir":
                # Current dir should have this directory in children
                if name not in current_dir:
                    current_dir[name] = Directory(current_dir)
            else:
                # Current dir should have this file
                size = int(is_dir_or_size)
                current_dir.add_file(name, size)

    return root_dir
