from DataTypes import Class


class Stability:

    @staticmethod
    def get_instability(c: Class, model: list):
        c_called = 0
        called_c = 0
        for c1 in model:
            for a in c.attributes:
                if a.type == c1.name:
                    c_called += 1
            for a in c1.attributes:
                if a.type == c.name:
                    called_c += 1
        if (c_called + called_c) == 0:
            return 0
        return float(c_called) / float(c_called + called_c)
