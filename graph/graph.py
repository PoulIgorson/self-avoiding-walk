class Vertex:
    def __init__(self, name, tree):
        self.name = name
        self.tree = tree

    def __eq__(self, other):
        if isinstance(other, Vertex):
            return self.name == other.name
        return False

    def __len__(self):
        return len(self.tree)

    def __iter__(self):
        return iter(self.tree)

    def in_(self, where):
        for br in where:
            if self.name == br.name:
                return True
        return False

    def join(self, j=''):
        s = ''
        for br in self.tree:
            s += str(br) + j
        if not s:
            s = '\n'
        else:
            s = s[:-1]
        return s

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)


def search_path(begin, end, path=[]):
    path = path + [begin]

    if begin == end:
        return [path]

    if len(begin) == 0:
        return []

    paths = []
    for branch in begin:
        tpath = search_path(branch, end, path)
        for p in tpath:
            paths.append(p)
    return paths


def filter_with_branch(paths, br):
    new_paths = []
    for path in paths:
        if br.in_(path):
            new_paths.append(path)
    return new_paths


def filter_without_branch(paths, br):
    new_paths = []
    for path in paths:
        if not br.in_(path):
            new_paths.append(path)
    return new_paths
