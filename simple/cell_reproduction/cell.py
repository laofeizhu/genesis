"""
Cell class with properties:
    cell grows and eats more food
    if food is not sufficient, cell shrinks
    cell reproduces as it reaches some size
    reproduction generates a new cell with small size
    reproduction reduces mother cell's size
    cell growth has a limit in size
    cell growth has a limit in cycles, insufficient food will also reduce life
    dead cell will get no size and free the space
    food supply per cycle is limited, cells will share with some strategy when food is insufficient (proportional to size for now).
"""
    
