from DataTypes import Class


class Complexity:

    # @staticmethod
    # def get_WMC(c: Class):
    #     this metric has not clear for me yet

    @staticmethod
    def get_NOM(c: Class):
        nom = len(c.methods)
        if nom <= 3:
            return 0
        if nom <= 10:
            return float(nom) / 7.0
        if nom <= 40:
            return 1
        if nom <= 50:
            return float(50 - nom) / 10.0
        return 0
