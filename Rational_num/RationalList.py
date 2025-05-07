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
        sorted_data = sorted(self.data, key=lambda r: (-r["d"], -r["n"]))
        return iter(sorted_data)

    def generator(self):
        for item in self.data:
            yield item

from Rational_num.rational import Rational
from RationalList import RationalList

def parse_rational(token):
    if '/' in token:
        return Rational(token)
    elif token.strip():
        return Rational(int(token), 1)
    return None

def process_file(filename, output_lines):
    rl = RationalList()
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            for token in line.strip().split():
                try:
                    r = parse_rational(token)
                    if r:
                        rl += r
                except Exception as e:
                    print(f"Пропущено '{token}': {e}")
    output_lines.append(f"{filename}:")
    output_lines.append(" ".join(str(r) for r in rl))
    output_lines.append("")


if __name__ == "__main__":
    input_files = ["test_files/input01.txt",
                   "test_files/input02.txt",
                   "test_files/input03.txt"]
    output_lines = []

    for filename in input_files:
        process_file(filename, output_lines)

    with open("test_files/=output.txt", "w", encoding="utf-8") as out:
        out.write("\n\n")
        out.write("\n".join(output_lines))


