import pandas as pd
from typing import List, Any

"""
В файле med.csv в столбце M удалите дубликаты, отсортируйте в  порядке  убывания.

Note: Все алгоритмы должны быть реализованы самостоятельно, встроенные методы сортировки и поиска не использовать, 
свойства уникальности элементов set не использовать, можно использовать получение элемента из списка или кортежа по его индексу,
 встроенное получение значения словаря по ключу не использовать. Сравнение строк производить посимвольно, лексикографически.
"""

FILENAME = "med.csv"
M = "Principal Practitioner Name CVRM"

def readCSV(filename: str, columnName: str) -> List[Any]:
    dataframe = pd.read_csv(filename, sep=";")
    data = dataframe[columnName].tolist()
    
    return data

def compareStrings(a: str, b: str) -> int:
        lenA = len(a)
        lenB = len(b)
        minLen = min(lenA, lenB)
        for i in range(minLen):
            if a[i] < b[i]:
                return -1
            elif a[i] > b[i]:
                return 1

        if lenA < lenB:
            return -1
        elif lenA > lenB:
            return 1
        else:
            return 0

def removeDuplicates(data: List[Any]) -> List[Any]:
    uniqueData = []
            
    for element in data:
        seen = False
        for item in uniqueData:
            if compareStrings(element, item) == 0:
                seen = True
                break
        if not seen:
            uniqueData.append(element)

    return uniqueData

def descSorting(data: List[Any]) -> List[Any]:
    n = len(data)
    for i in range(n):
        for j in range(0, n - 1 - i):
            if compareStrings(data[j], data[j+1]) == -1:
                data[j], data[j+1] = data[j+1], data[j]
    
    return data

def main() -> None:
    data = readCSV(FILENAME, M)
    uniqueData = removeDuplicates(data)
    sortedUniqueData = descSorting(uniqueData)

    print(sortedUniqueData)

if __name__ == "__main__":
    main()
