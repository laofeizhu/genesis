Cell with sugar

This simulation is to play with the most basic scenario of a cell in a 2D plane. The cell will have the following attributes:
* It has HP
* It has position
* It can move and it somehow can control the direction of move. Hopefully it can improve its algorithm of moving in its life or in the next generation.
* There's a map (world) that the cells lives in, they have some limitation in the action area, but there's a large sugar source that keeps the sugar distribution.
* It consumes sugar near it to keep alive
* It has a penalty function that if losing HP, it will die. And the cell's target is try not to los HP.
* The cell can reproduce new cells if it takes enought sugar. Another penalty function will make the cell happy if it does reproduction.
* The new generation of cell inherites all the properties of the cell except that the parameters are changed a little bit.
** These parameters might be encoded in gene.
* (maybe) The new generation might get new functions/penalty functions by some chance.
