from Rational_num.rational import Rational

class RationalList:
    def __init__(self):
        self.data = []

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        if not isinstance(value, Rational):
            raise TypeError("Значення має бути типу Rational")
        self.data[index] = value

    def __len__(self):
        return len(self.data)

    def __add__(self, other):
        result = RationalList()
        result.data = self.data.copy()
        if isinstance(other, RationalList):
            result.data.extend(other.data)
        elif isinstance(other, Rational):
            result.data.append(other)
        elif isinstance(other, int):
            result.data.append(Rational(other))
        else:
            raise TypeError("Непідтримуваний тип для додавання")
        return result

    def __iadd__(self, other):
        if isinstance(other, RationalList):
            self.data.extend(other.data)
        elif isinstance(other, Rational):
            self.data.append(other)
        elif isinstance(other, int):
            self.data.append(Rational(other))
        else:
            raise TypeError("Непідтримуваний тип для += операції")
        return self

    def __str__(self):
        return "[" + ", ".join(str(r) for r in self.data) + "]"

    def sort(self):
        self.data.sort(key=lambda r: r())

    def __iter__(self):
        return iter(self.data)

    def generator(self):
        for item in self.data:
            yield item

if __name__ == "__main__":
    input_files = [
        "test_files/input01 (2).txt",
        "test_files/input02.txt",
        "test_files/input03.txt"
    ]

    with open("test_files/output.txt", "w") as output_file:
        for filename in input_files:
            operation = '-'
            with open(filename, "r") as f:
                for line in f.readlines():
                    data = line.split()
                    result = Rational(0, 1)
                    for item in data:
                        if item == '+':
                            operation = '+'
                        elif item == '-':
                            operation = '-'
                        elif item == '*':
                            operation = '*'
                        else:
                            number = Rational(item)
                            if operation == '+':
                                result += number
                            elif operation == '-':
                                result -= number
                            elif operation == '*':
                                result *= number
                    output_file.write(f"{filename}: {result} = {result()}\n")