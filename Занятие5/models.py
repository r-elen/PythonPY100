# models
from conf import EMPTY_SYMBOL, SIZE_FIELD


def init_field(size: int = SIZE_FIELD) -> list[list]:
    return [
        [EMPTY_SYMBOL for _ in range(size)]
        for _ in range(size)
    ]


def is_empty_cell(field: list[list], row_index: int, col_index: int) -> bool:
    return field[row_index][col_index] == EMPTY_SYMBOL


def has_empty_cell(field: list[list]) -> bool:
    for row in field:
        for cell in row:
            if cell == EMPTY_SYMBOL:
                return True
    return False


def is_win(field: list[list]) -> bool:
    win_combinations = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],

        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],

        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]
    for win_comb in win_combinations:
        cell1_coord, cell2_coord, cell3_coord = win_comb

        cell_1 = get_cell(field, cell1_coord[0], cell1_coord[1])
        cell_2 = get_cell(field, cell2_coord[0], cell2_coord[1])
        cell_3 = get_cell(field, cell3_coord[0], cell3_coord[1])

        if cell_1 == cell_2 == cell_3 != EMPTY_SYMBOL:
            return True

    return False


def get_cell(field: list[list], row_index: int, col_index: int):  # получить ячейку
    return field[row_index][col_index]


def set_cell(field: list[list], row_index: int, col_index: int, player_symbol) -> None:  # установить ячейку
    field[row_index][col_index] = player_symbol


def test_empty_field(field):
    empty_field = init_field()
    assert is_win(empty_field) == False


if __name__ == '__main__':
    test_empty_field()
