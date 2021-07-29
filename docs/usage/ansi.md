# ANSI Escape Codes Primer

(Shameless copy from [here](https://notes.burke.libbey.me/ansi-escape-codes/))

Subsequently you'll understand the basics of terminal output in the Unix world.


!!! note "Already Known?"

    If you understand what this is doing, you can definitely skip this section.

    `\x1b[A\r\x1b[K\x1b[1;32mopened \x1b[1;4;34m%s\x1b[0;1;32m in your browser.\x1b[0m\n`

If you’re like most people, your face just melted, but it’s actually really simple. This page is a
crash course in what all of these things mean, and how to learn to read and write them effectively.


## Basic Mechanics

The terminal outputs *streams*, stateless. I.e. there is no selector based output control, like in browsers.

Rather there are escaped instructions defined, which, when contained in the output stream, make the
terminal apply various operations, like switching to a foreground or background color for
*subsequent output* - or start blinking. Appropriate reset codes are also standardized.   In the
Unix world, these instructions are the famous ["ANSI escape codes"][AE]. They start with `\x1b[` or
`\033[` or '\e' (i.e. `ESC` (0x1b) + `[`) and end with a letter (`m` for colors), in between control
sequences ([CSI sequences](https://en.wikipedia.org/wiki/ANSI_escape_code)).

- Applications can know if their output goes to the terminal or into a file or pipe (python:
  `sys.stdout.isatty()`), so they can opt to include those terminal control sequences or not, within
  their output.
- Many apps offer switches, changing their default behaviour, i.e. you can "see" the ANSI codes e.g.
  by redirecting colorized app output into a file and open it with an editor:  `ls --color=always >
  myfile`.
- There is no way to change the output *after the fact* - except by using again ANSI escape
  instructions to change the current output position - but it's up to the application to remember
  what text was there before, should e.g. only the color be required to change.

You can simulate your own "hello world app", by typing

    echo -e "\x1b[38;5;124mHello Red World\x1b[0m"

in the terminal, then hit enter.

Why was the text red?


## `\x1b`

ANSI escapes always start with `\x1b`, or `\e`, or `\033`. These are all the same thing: they’re
just various ways of inserting the byte 27 into a string. If you look at an [ASCII
table](http://www.asciitable.com/), `0x1b` is literally called `ESC`, and this is basically why.

## Control sequences

The majority of these escape codes start with `\x1b[`. This pair of bytes is referred to as `CSI`,
or “Control Sequence Introducer”. By and large, a control sequence looks like:

    0x1B + "[" + <zero or more numbers, separated by ; + <a letter>

It’s helpful to think of it this way: the terminating letter is a *function name*, and the intervening
numbers as function arguments, delimited by semicolons rather than the typical commas.

If you see `\x1b[0;1;34m`, you can read it like this:

    \x1b[  # call a function 0;1;34 # function arguments (0, 1, 34) m      # function name

In effect, this is `m(0, 1, 34)`. Similarly, `\x1b[A` is just `A()`.

## Available functions

So with that mental model—reading escape sequences as function invocations—here’s an abridged documentation of the “standard library”, as it were:

|   | name                       | signature  | description                                                               |
| - | -------------------------- | ---------- | ------------------------------------------------------------------------- |
| A | Cursor Up                  | (n=1)      | Move cursor up by `n`                                                     |
| B | Cursor Down                | (n=1)      | Move cursor down by `n`                                                   |
| C | Cursor Forward             | (n=1)      | Move cursor forward by `n`                                                |
| D | Cursor Back                | (n=1)      | Move cursor back by `n`                                                   |
| E | Cursor Next Line           | (n=1)      | Move cursor to the beginning of the line `n` lines down                   |
| F | Cursor Previous Line       | (n=1)      | Move cursor to the beginning of the line `n` lines up                     |
| G | Cursor Horizontal Absolute | (n=1)      | Move cursor to the the column `n` within the current row                  |
| H | Cursor Position            | (n=1, m=1) | Move cursor to row `n`, column `m`, counting from the top left corner     |
| J | Erase in Display           | (n=0)      | Clear part of the screen. 0, 1, 2, and 3 have various specific functions  |
| K | Erase in Line              | (n=0)      | Clear part of the line. 0, 1, and 2 have various specific functions       |
| S | Scroll Up                  | (n=1)      | Scroll window up by `n` lines                                             |
| T | Scroll Down                | (n=1)      | Scroll window down by `n` lines                                           |
| s | Save Cursor Position       | ()         | Save current cursor position for use with `u`                             |
| u | Restore Cursor Position    | ()         | Set cursor back to position last saved by `s`                             |
| f | …                          | …          | (same as G)                                                               |
| m | SGR                        | ()        | Set graphics mode. More below                                             |


## SGR

The SGR (“Select Graphics Rendition”) function (`m`) has a much more complex signature than the other functions. An—again, abridged—guide to SGR arguments:

| value                  | name / description                                                                                                                                        |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0                      | Reset: turn off all attributes                                                                                                                            |
| 1                      | Bold (or bright, it’s up to the terminal and the user config to some extent)                                                                              |
| 3                      | Italic                                                                                                                                                    |
| 4                      | Underline                                                                                                                                                 |
| 30–37                  | Set text color from the basic color palette of 0–7                                                                                                      |
| 38;5;_n_               | Set text color to index `n` in a [256-color palette][W] (e.g. `x1b[38;5;34m`)                                                                           |
| 38;2;_r_;_g_;_b_       | Set text color to an RGB value (e.g. `x1b[38;2;255;255;0m`)                                                                                              |
| 40–47                  | Set background color                                                                                                                                     |
| 48;5;_n_               | Set background color to index `n` in a 256-color palette                                                                                                |
| 48;2;_r_;_g_;_b_       | Set background color to an RGB value                                                                                                                     |
| 90–97                  | Set text color from the **bright** color palette of 0–7                                                                                                 |
| 100–107                | Set background color from the **bright** color palette of 0–7                                                                                           |

[W]: https://robotmoon.com/256-colors/

Multiple SGR arguments can always be concatenated using another `;`, and they will be applied in the
order they are encountered. It’s especially common to see `0;` before some other argument, in order
to reset the state before applying our own.

## Basic Color Palettes

The basic color palette has 8 entries:

-   0: black
-   1: red
-   2: green
-   3: yellow
-   4: blue
-   5: magenta
-   6: cyan
-   7: white

A useful way to help remember this, or at least to select colours for use, is that, with the
exception of 0/black, the colours are ordered by usefulness, with highest first: red text is very
useful for indicating failures, green is useful for indicating extreme success, yellow for warnings,
and then blue, magenta, and cyan for progressively more obscure conditions or decoration.

0 and 7 are less useful for text because one or the other will generally look nearly-unreadable
depending on whether the user has a light or a dark background.

Terminals will also have a “bright” version of this palette (activated using 90–97 / 100–107). These
are the same (black/red/green/etc.) but generally noticeably brighter than their regular
counterparts.

(Much) more about colors is [here](./colors.md).

## Summary

That was a lot of information, but that’s essentially everything you need to know in order to
competently read and write ANSI escape codes in a terminal.


