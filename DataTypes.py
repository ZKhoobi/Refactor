class Node:
    name: str

    def __init__(self):
        self.name = ""


class Attribute(Node):
    type: str
    is_static: bool

    def __init__(self, name = ""):
        Node.__init__(self)
        self.type = ""
        self.is_static = False
        self.name = name


class Method(Node):
    parameters: list
    attributes: list
    is_static: bool
    invocation: list
    access_level: str

    def __init__(self):
        Node.__init__(self)
        self.parameters = list()
        self.attributes = list()
        self.invocation = list()
        self.is_static = False
        self.access_level = ""


class Class(Node):
    attributes: list
    methods: list

    def __init__(self):
        Node.__init__(self)
        self.attributes = list()
        self.methods = list()
