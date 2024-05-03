from dataclasses import dataclass, field, fields
from functools import cache

GRID = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1],
]
GRID = [
    [1, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 1, 0],
    [1, 1, 0, 0, 1, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 1, 0, 0, 1, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 0, 0],
]


LENGTH = len(GRID)


def in_range(i, j, lower=0, upper=LENGTH):
    return (lower <= i < upper) and (lower <= j < upper)


def check_grid(i, j, x, y):
    if GRID[x][y] == 1:
        ret = bfs(x, y)
        if ret:
            GRID[i][j] = 1
        return ret


def bfs(i, j):
    if not in_range(i, j, lower=1, upper=LENGTH - 1):
        return True

    GRID[i][j] = 2

    x, y = i + 1, j
    ret1 = check_grid(i, j, x, y)

    x, y = i - 1, j
    ret2 = check_grid(i, j, x, y)

    x, y = i, j + 1
    ret3 = check_grid(i, j, x, y)

    x, y = i, j - 1
    ret4 = check_grid(i, j, x, y)

    return ret1 or ret2 or ret3 or ret4


def print_grid():
    for row in GRID:
        for elem in row:
            print(elem, end="  ")
        print()
    print("=" * 80)


def main():
    print_grid()
    for i in range(1, LENGTH - 1):
        for j in range(1, LENGTH - 1):
            if GRID[i][j] == 1:
                # pass
                bfs(i, j)
    print_grid()


class hlist:
    l = []

    def __eq__(self, __value: object) -> bool:
        return self.l == __value

    def __hash__(self) -> int:
        return hash(tuple(self.l))

    def __str__(self) -> str:
        return str(self.l)

    def __repr__(self) -> str:
        return f"xxx{self.l}"


@dataclass(slots=True, order=True)
class Myclass:
    x: int
    y: str = field()
    z: float = 0.4
    qqq: list[int] = field(default_factory=list, metadata={"type": "my"})

    SLOT_DICT: dict = field(default_factory=dict)

    def __post_init__(self):
        self.SLOT_DICT = {value: index for index, value in enumerate(self.__slots__)}

    def get_metadata_type(self, variable_name):
        index = self.SLOT_DICT.get(variable_name)
        if not index:
            return

        meta_type = fields(self)[index].metadata.get("type")
        return meta_type


if __name__ == "__main__":
    main()
    print(Myclass.__slots__)
    x = Myclass(1, "2")
    print(x.get_metadata_type("y"))
