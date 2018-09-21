from DataTypes import Class


class Coupling:
    @staticmethod
    def get_RFC(c: Class):  # Response For Class: means number os method called in class plus number of method of class
        counter = 0
        for m in c.methods:
            counter += (1 + len(m.invocation))
        return counter

    @staticmethod
    def get_ICP(c: Class):  # Information-Flow-Based Coupling:
        icp = 0
        for m in c.methods:
            for i in m.invocation:
                if i.target.value is not None:  # this method is not New or Overloading method of this class
                    icp += len(i.arguments) + 1
        return icp

