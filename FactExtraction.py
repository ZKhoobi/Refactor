import glob
import plyj.parser as plyj

from DataTypes import Class, Method, Attribute


class FactExtractor:
        model: list
        src_path: str

        def __init__(self, src_path):
            self.model = list()
            self.src_path = src_path

        def make_model(self):
            for filename in glob.iglob(self.src_path+'**/*.java', recursive=True):
                parser = plyj.Parser()
                # parse a compilation unit from a file
                tree = parser.parse_file(open(filename))
                for type_declaration in tree.type_declarations:
                    if isinstance(type_declaration, plyj.ClassDeclaration):
                        new_class = self.make_class(type_declaration)
                        self.model.append(new_class)
            return self.model

        @staticmethod
        def make_class(class_declaration: plyj.ClassDeclaration):
            new_class = Class()
            new_class.name = class_declaration.name
            for b in class_declaration.body:
                if isinstance(b, plyj.MethodDeclaration):
                    new_method = FactExtractor.make_method(b, new_class)
                    new_class.methods.append(new_method)
                elif isinstance(b, plyj.FieldDeclaration):
                    new_attribute = FactExtractor.make_attribute(b)
                    new_class.attributes.append(new_attribute)
            return new_class

        @staticmethod
        def make_method(method: plyj.MethodDeclaration, base_class: Class):
            new_method = Method()
            new_method.name = method.name
            new_method.access_level = method.modifiers[0]
            class_attribute_names = list(map(lambda x: x.name, base_class.attributes))

            if 'parameters' in method._fields:
                for p in method.parameters:
                    new_attribute = FactExtractor.make_attribute(p)
                    new_method.parameters.append(new_attribute)
            if method.body is not None:
                for b in method.body:

                    # Method Invocation: data of method and input and body needed
                    if isinstance(b, plyj.MethodInvocation):
                        new_method.invocation.append(b)
                        # If this invocation use one of class attribute
                        for a in b.arguments:
                            if a.name in class_attribute_names:
                                new_method.attributes.append(Attribute(a.name))
                    # Assignment: should search for class attribute in lhs and rhs
                    elif isinstance(b, plyj.Assignment):
                        if isinstance(b.lhs, plyj.Name):
                            if b.lhs.value in class_attribute_names:
                                new_method.attributes.append(Attribute(b.lhs.value))
                        else:
                            if b.lhs.lhs.value in class_attribute_names:
                                new_method.attributes.append(Attribute(b.lhs.lhs.value))
                        if isinstance(b.rhs, plyj.Name):
                            if b.rhs.value in class_attribute_names:
                                new_method.attributes.append(Attribute(b.rhs.value))
                        else:
                            if b.rhs.rhs.value in class_attribute_names:
                                new_method.attributes.append(Attribute(b.rhs.rhs.value))

                    elif isinstance(b, plyj.Conditional):
                        print(b)

            return new_method

        @staticmethod
        def make_attribute(attribute: plyj.FieldDeclaration):
            new_attribute = Attribute()
            new_attribute.type = attribute.type.name.value
            new_attribute.name = attribute.variable_declarators[0].variable.name
            return new_attribute

        @staticmethod
        def make_attribute(attribute: plyj.FormalParameter):
            new_attribute = Attribute()
            if isinstance(attribute.type, str):
                new_attribute.type = attribute.type
            else:
                new_attribute.type = attribute.type.name.value
            if 'variable' in attribute._fields:
                new_attribute.name = attribute.variable.name
            else:
                new_attribute.name = attribute.variable_declarators[0].variable.name
            return new_attribute


