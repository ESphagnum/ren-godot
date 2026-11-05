















init:

    image zigzag_bg = "minigame/ss/fon.png"
    image zz01 = "minigame/ss/1.png"
    image zz02 = "minigame/ss/2.png"
    image zz03 = "minigame/ss/3.png"
    image zz04 = "minigame/ss/4.png"
    image zz05 = "minigame/ss/5.png"
    image zz06 = "minigame/ss/6.png"
    image zz07 = "minigame/ss/7.png"
    image zz08 = "minigame/ss/8.png"
    image zz09 = "minigame/ss/9.png"
    image zz10 = "minigame/ss/10.png"
    image zz11 = "minigame/ss/11.png"
    image zz12 = "minigame/ss/12.png"
    image zz13 = "minigame/ss/13.png"

label zigzag_prepare:
    python:
        eps = 45            
        pieces = [
    PuzzlePiece(
        key = 1,
        img = "zz01",
        size = (610, 234)
        ),
    PuzzlePiece(
        key = 2,
        img = "zz02",
        size = (259, 544),
        link = 1,
        target = (1, 191-48),
        eps = eps
        ),
    PuzzlePiece(
        key = 3,
        img = "zz03",
        size = (537, 511),
        link = 1,
        target = (385-223, 55-48),
        eps = eps
        ),
    PuzzlePiece(
        key = 4,
        img = "zz04",
        size = (602, 577),
        link = 2,
        target = (226-224, 414-191),
        eps = eps
        ),
    PuzzlePiece(
        key = 5,
        img = "zz05",
        size = (426, 409),
        link = 3,
        target = (664-385, 57-55),
        eps = eps
        ),
    PuzzlePiece(
        key = 6,
        img = "zz06",
        size = (465, 612),
        link = 5,
        target = (860-664, 60-57),
        eps = eps
        ),
    PuzzlePiece(
        key = 7,
        img = "zz07",
        size = (824, 827),
        link = 6,
        target = (867-860, 58-60),
        eps = eps
        ),
    PuzzlePiece(
        key = 8,
        img = "zz08",
        size = (608, 637),
        link = 7,
        target = (1136-867, 58-58),
        eps = eps
        ),
    PuzzlePiece(
        key = 9,
        img = "zz09",
        size = (446, 532),
        link = 12,
        target = (1303-785, 325-535),
        eps = eps
        ),
    PuzzlePiece(
        key = 10,
        img = "zz10",
        size = (308, 410),
        link = 11,
        target = (1442-952, 583-804),
        eps = eps
        ),
    PuzzlePiece(
        key = 11,
        img = "zz11",
        size = (644, 189),
        link = 12,
        target = (952-785, 804-535),
        eps = eps
        ),
    PuzzlePiece(
        key = 12,
        img = "zz12",
        size = (650, 461),
        link = 7,
        target = (785-867, 535-58),
        eps = eps
        ),
    PuzzlePiece(
        key = 13,
        img = "zz13",
        size = (459, 578),
        link = 4,
        target = (473-226, 416-414),
        eps = eps
        ),
    ]

        puzzle = PuzzleCipher(
    victory_label = "d4_polhouse_followup2.solved",
    skip_label = "d4_polhouse_followup2.solved",
    background = "zigzag_bg",
    pieces = pieces
    )

    $ puzzle.shuffle()

    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
