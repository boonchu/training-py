#!/usr/bin/env python3

from pandas import DataFrame,read_csv

class Compare():
    """
    https://carloarg02.medium.com/my-favorite-coding-question-to-give-candidates-17ea4758880c
    """
    header  = ["Index","Organization Id","Name","Website","Country","Description","Founded","Industry","Number of employees"]

    def __init__(self, fileOfA: str, fileOfB: str):
        """
        Set a comparison of two simple dimension array of data
        """
        dataOfA = read_csv(fileOfA)
        dataOfB = read_csv(fileOfB)
        self.setOfA = DataFrame(dataOfA, columns=self.header)
        self.setOfB = DataFrame(dataOfB, columns=self.header)
        

    def showTable(self) -> None:
        print(self.setOfA)
        print(self.setOfB)


    def compareIndustry(self, listOfIndustry: list) -> dict:
        """
        how-to-initialize-a-dict-with-keys-from-a-list-and-empty-value-in-python
        https://stackoverflow.com/questions/2241891/how-to-initialize-a-dict-with-keys-from-a-list-and-empty-value-in-python
        """
        matched = dict.fromkeys(listOfIndustry, 0)
        for idx in self.setOfB.index:
            name = self.setOfB['Industry'][idx]
            if name in listOfIndustry:
                matched[name] = matched[name] + 1
        return matched


    @staticmethod
    def getIndustry(dFrame: DataFrame) -> set:
        """
        Iterate index attribue access of the DataFrame
        """
        result = []
        for idx in dFrame.index:
            result.append(dFrame['Industry'][idx])
        return set(result)


compare = Compare('organizations-100.csv', 'organizations-1000.csv')
compare.showTable()
# sorting-a-set-of-values
# https://stackoverflow.com/questions/17457793/sorting-a-set-of-values
listOfIndustry = sorted(compare.getIndustry(compare.setOfA))
print(compare.compareIndustry(listOfIndustry))
