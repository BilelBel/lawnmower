# Table of Contents #
- [Prerequisites](#prerequisites)
- [Features](#features)
- [Basic usage](#basic-usage)
- [Examples](#examples)
- [Unit test](#unit-test)


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
```raw
$python lawn_mawer.py <input_file_path>
```

# Examples #
```raw
$python lawn_mawer.py input_file
```


## Example 1 ##
* Content of the input file

```raw
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

```raw
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

```raw
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

```raw
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

```raw
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


# Unit test #
Running the doctest file <test_lawn_mower.txt>:

## Command ##

```raw
$python -m doctest -v  test_lawn_mower.txt
```

## Result ##
```console
Trying:
    from lawn_mower import Action
Expecting nothing
ok
Trying:
    Action.validate_actions("AGD")
Expecting:
    True
ok
Trying:
    Action.validate_actions("AGFSD")
Expecting:
    False
ok
Trying:
    from lawn_mower import Direction
Expecting nothing
ok
Trying:
    Direction('N').turn_left().value
Expecting:
    'O'
ok
Trying:
    Direction('E').turn_right().value
Expecting:
    'S'
ok
Trying:
    from lawn_mower import Position
Expecting nothing
ok
Trying:
    pos = Position (1,"2F")
Expecting nothing
ok
Trying:
    pos.is_int()
Expecting:
    False
ok
Trying:
    pos = Position (1,2)
Expecting nothing
ok
Trying:
    pos.is_int()
Expecting:
    True
ok
Trying:
    pos.move(Direction('N'),1).y
Expecting:
    3
ok
Trying:
    pos.move(Direction('N'),1).x
Expecting:
    1
ok
Trying:
    from lawn_mower import LawnMower
Expecting nothing
ok
Trying:
    lawn_mower1 = LawnMower (Position(1,2),Direction('N'))
Expecting nothing
ok
Trying:
    lawn_mower1.execute_actions("GAGAGAGAA",Position(5,5))
Expecting:
    True
ok
Trying:
    lawn_mower1.position.y
Expecting:
    3
ok
Trying:
    lawn_mower1.position.x
Expecting:
    1
ok
Trying:
    lawn_mower1.direction.value
Expecting:
    'N'
ok
Trying:
    lawn_mower2 = LawnMower (Position(3,3),Direction('E'))
Expecting nothing
ok
Trying:
    lawn_mower2.execute_actions("AADAADADDA",Position(5,5))
Expecting:
    True
ok
Trying:
    lawn_mower2.position.y
Expecting:
    1
ok
Trying:
    lawn_mower2.position.x
Expecting:
    5
ok
Trying:
    lawn_mower2.direction.value
Expecting:
    'E'
ok
1 items passed all tests:
  24 tests in test_lawn_mower.txt
24 tests in 1 items.
24 passed and 0 failed.
Test passed.
```
