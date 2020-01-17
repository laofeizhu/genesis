from cell import Cell
from matplotlib import pyplot as plt

def main():
    food = 1000
    cells = [Cell()]
    cycles = [0]
    size_history = [1]
    num_cells = [1]
    while cycles[-1] < 1000:
        cycles.append(cycles[-1] + 1)
        new_cells = []
        for cell in cells:
            if cell.is_live():
                new_cells.append(cell)
        total_size = 0
        for cell in new_cells:
            total_size += cell.size
        size_history.append(total_size)
        for cell in new_cells:
            baby = cell.grow(food * cell.size / total_size)
            if baby is not None:
                new_cells.append(baby)
        cells = new_cells
        num_cells.append(len(cells))

    plt.plot(cycles, size_history, 'r', cycles, num_cells, 'k')
    plt.show()


if __name__ == '__main__':
    main()
