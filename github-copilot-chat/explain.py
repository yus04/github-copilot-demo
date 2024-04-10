import random

class NumberList:
    def __init__(self, length):
        self.numbers = []
        self.generate_numbers(length)

    def generate_numbers(self, length):
        for _ in range(length):
            self.numbers.append(random.randint(1, 100))

    def sort(self):
        self.numbers.sort()

if __name__ == "__main__":
    length = 10
    number_list = NumberList(length)
    print("Original list:", number_list.numbers)

    number_list.sort()
    print("Sorted list:", number_list.numbers)
