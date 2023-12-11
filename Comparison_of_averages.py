# Задание 1. Создайте программу на Python или Java,
# которая принимает два списка чисел и выполняет следующие действия:
# a. Рассчитывает среднее значение каждого списка.
# b. Сравнивает эти средние значения и выводит соответствующее сообщение:
# - "Первый список имеет большее среднее значение", если среднее значение первого списка больше.
# - "Второй список имеет большее среднее значение", если среднее значение второго списка больше.
# - "Средние значения равны", если средние значения списков равны.

class Comparison_of_averages:
    def __init__(self, list1: [int | float], list2: [int | float]):
        """The class for comparing the average values of two lists."""
        self.list1 = list1
        self.list2 = list2

    def get_averages(self) -> [float | float]:
        """A method for calculating the average values of two lists"""
        average1 = average2 = 0

        if self.list1:
            average1 = sum(self.list1) / len(self.list1)

        if self.list2:
            average2 = sum(self.list2) / len(self.list2)

        return average1, average2

    def averages_comparatison(self):
        """The method compares the lists by their average values"""
        average1, average2 = self.get_averages()
        if average1 > average2:
            print('Первый список имеет большее среднее значение')
        elif average1 < average2:
            print('Второй список имеет большее среднее значение')
        else:
            print("Средние значения равны")
