# Table of Contents #
- [Prerequisites](#prerequisites)
- [Features](#features)
- [Basic usage](#basic-usage)
- [Examples](#examples)
 - [Example 1](##example 1)


# Prerequisites #

Install python 3

# Features #
This program implements an automatic lawn mowing for rectangular surfaces.
* Each mower can be programmed to cover the entire surface.
* The position of the mower is represented by a combination of coordinates (x, y) and a letter indicating the orientation according to the English cardinal notation (N, E, W, S). The lawn is divided into a grid to simplify navigation.
* To control the mower, we send him a simple sequence of letters. The possible letters are "D", "G" and "A". "D" and "G" rotate the mower 90 ° right or left respectively, without moving it. "A" means that the mower is moved one step in the direction it faces, and without changing its orientation.
* If the position after movement is outside the lawn, the mower will not move, keep its orientation and process the next command.
* Each mower moves sequentially, which means that the second mower moves only when the first mower has performed its entire series of instructions.
* When a mower completes a series of instructions, it communicates its position and orientation.

# Input file #
To program the mower, it is provided with an input file built as follows: 
* The first line corresponds to the coordinates of the upper right corner of the lawn, those of the lower left corner are supposed to be (0,0) The continuation of the file allows to pilot all mowers that have been deployed.
* Each mower has two lines: the first line gives the starting position of the mower, as well as its orientation. 
* The position and orientation are provided in the form of 2 digits and a letter,  separated by a space the second line is a series of instructions ordering the mower to explore the lawn. 
* The instructions are a sequence of characters without spaces.


# Basic usage #
python lawn_mawer.py <input_file_path>

# Examples #
python lawn_mawer.py input_file

## Example 1 ##
* Content of the input file

```console
5 5
1 2 N
GAGAGAGAA
3 3 E
AADAADADDA
```

  * Results:

```console
New lawnmowers positions:
1 3 N
5 1 E
```

## Example 2 ##
* Content of the input file

```console
5 5
1 2 F
GAGAGAGAA
3 3 E
AADAADADDA
```

  * Results:

```console
Wrong direction for the lawn mower number  1
New lawnmowers positions:
5 1 E
```
## Example 3 ##
* Content of the input file

```console
5 5
1 2 N
GAGAGAGAA
3 3 E
AADAADADKA
```

* Results:

```console
New lawnmowers positions:
1 3 N
Wrong actions for the lawnmower number 2
```

## Example 4 ##
* Content of the input file

```console
55
1 2 N
GAGAGAGAA
3 3 E
AADAADADDA
```

* Results:

```console
Wrong file: Not complete garden coordinates
```
## Example 5 ##
* Content of the input file

```console
5 5D
1 2 N
GAGAGAGAA
3 3 E
AADAADADDA
```

* Results:

```console
Wrong file: Garden coordinates should be of type integer
```
