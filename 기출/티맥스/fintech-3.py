class Node:
    def __init__(self, name = ''):
        self.name = name
        self.children = dict()
    
    def add(self, child):
        self.children[child.name] = child
    
    def delete(self, child_name):
        self.children[child_name] = None

    def get(self, child_name):
        return self.children[child_name]

    def get_children(self):
        children = list(filter(lambda c: c, self.children.values()))
        children.sort(key=lambda c: c.name)

        return children
    
    def copy(self):
        copy_node = Node(self.name)
        for child in self.get_children():
            copy_node.add(child.copy())
        
        return copy_node

def parse(path):
    return list(filter(lambda p: p, path.split('/')[1:]))

def search(root, path):
    target = root

    for p in path:
        target = target.get(p)
    
    return target

def create(root, path):
    target_name = path.pop()
    parent = search(root, path)
    
    parent.add(Node(target_name))

def delete(root, path):
    target = path.pop()
    parent = search(root, path)
    
    parent.delete(target)

def copy(root, spath, dpath):
    source = search(root, spath)
    dest = search(root, dpath)

    dest.add(source.copy())

def result(root, arr, path):
    path += root.name
    arr.append(path if path else '/')
    print(arr)

    for child in root.get_children():
        result(child, arr, path + '/')

    return arr


def solution(directory, command):
    ORDER = {
        'CREATE': 'mkdir',
        'DELETE': 'rm',
        'COPY': 'cp'
    }

    root = Node()

    for dir in directory[1:]:
        create(root, parse(dir))
    
    for com in command:
        com = com.split()
        order = com[0]
        
        if order == ORDER["CREATE"]:
            create(root, parse(com[1]))
        
        if order == ORDER["DELETE"]:
            delete(root, parse(com[1]))
        
        if order == ORDER["COPY"]:
            copy(root, parse(com[1]), parse(com[2]))
    
    answer = result(root, [], '')
    
    return answer


print(
    solution(
        ["/","/hello","/hello/tmp","/root","/root/abcd","/root/abcd/etc","/root/abcd/hello"], 
        ["mkdir /root/tmp","cp /hello /root/tmp","rm /hello"]
    )
)

print(
    solution(
        ["/"],
        ["mkdir /a", "mkdir /a/b", "mkdir /a/b/c", "cp /a/b /", "rm /a/b/c"]
    )
)
