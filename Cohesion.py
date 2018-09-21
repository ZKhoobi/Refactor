from DataTypes import Class


class Cohesion:
    @staticmethod
    def get_TCC(c: Class):
        shared_param = 0
        public_method_number = 0
        for m1 in c.methods:
            for m2 in c.methods:
                if m1.name != m2.name and m1.access_level == 'public' and m2.access_level == 'public':
                    find = False
                    for a1 in m1.parameters:
                        if find is True:
                            break
                        for a2 in m2.parameters:
                            if find is True:
                                break
                            if a1.type == a2.type or (isinstance(a1.type, str) is False
                                                      and isinstance(a2.type, str) is False
                                                      and isinstance(a1.type, a2.type)
                                                      and issubclass(a1.type, a2.type)):
                                shared_param += 1
                                find = True
        for m in c.methods:
            if m.access_level == 'public':
                public_method_number += 1

        if public_method_number < 2:
            return 0
        else:
            return shared_param / (public_method_number * (public_method_number - 1))

    @staticmethod
    def get_ICH(c: Class):
        ich = 0
        for m in c.methods:
            for i in m.invocation:
                if i.target.value is None:  # this method is New or Overloading method of this class
                    ich += len(i.arguments) + 1
        return ich

    # @staticmethod
    # def get_LCOM5(c: Class):

