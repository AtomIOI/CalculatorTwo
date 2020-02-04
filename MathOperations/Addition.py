class Addition:
    @staticmethod
    def sum(augend, addend):
        return augend + addend

    @staticmethod
    def sumList(list):
        result = 0
        for value in list:
            result = Addition.sum(value,result)
        return result