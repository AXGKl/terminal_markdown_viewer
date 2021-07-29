# Colors

Colors are the most important expressive possibility we have, especially in the terminal.

mdv offers a lot of possibilities to parametrize coloring, but there are some basic things to
know.

!!! tip "Terminal Colors"
    There [lots of good resources][TC] about terminal colors out there, so we only provide the minimum
    information here how terminals render colors.

[Here](./ansi.md) is a very concise description about the base mechanics.

## True Colors: Expressive Freedom / Deterministic Output

!!! important "True Colors Are Fixed"
    Using true colors is comparable to the web: The author defines
    how the content should look, colorwise and that's what the user gets - with the exception of the
    recently popular dark/light mode support of many web pages, or artifical, [more or
    less](https://darkreader.org/) awkward ways of applying personal styles to content, after the fact.

Users of mdv most probably run a true color capable (24-bit color) terminal. [Most]() terminals today
support this. 

Quick Test: 

```bash lp fmt=xt_flat
mdv2 colortables --max=30
```
If you get output like above you are good. Now you need to know about Base16, the 16 base colors.


## Base16: Consistency

Many users love the terminal because of [consistent
looks](https://www.reddit.com/search/?q=dwm%20rice) between apps. There are even
[applications](https://github.com/dylanaraps/pywal), which can set the looks cross-app, consistent
with the dominant colors of your current wallpaper...

How can this work.

Answer (like for any problem in software): An indirection.

!!! note
    There is a special set of 16 "base" or "system" color ANSI codes, where most terminals offer an indirection
    feature, through which the user can configure, which *actual* color the terminal should use.
    Escape sequence for those: `\x1b[<30-37>m` (3/4 bit) and `\x1b[38;5;<0-15>m` (for background:
    40-47 and 48;5;...). See [here](./ansi.md).

Here the output of the `mdv2 colortables` command again - while changing the terminal base16 color mapping configuration, using a little [fzf based tool](https://github.com/axiros/suckless-add-ons), which changes the config and sig-reloads the terminal.

You notice that the 16 base colors change, while the other colors remain fixed (except the text,
which is usually set to be a base color).

![colorcycle](./img/colors.gif)


!!! important "Base Colors Should Be Default"
    === "Use the Base Colors"
        Terminal application authors are therefore encouraged to default to using those 16 base colors, when
        generating output - and NOT the other 8 bit or true colors - and let the user decide how we
        wants them displayed. 

        > If every terminal application defaulted to the author's fixed color preferences, we would get the
        same stylisitic mess than in the web.

        The [base16 suite](http://chriskempson.com/projects/base16/) provides styling guidelines and
        a ton of themes, i.e. actual color mappings, for the 16 base color codes.

    === "Example: htop and vim"
        ![](./img/theme_sel.gif)


Having said that, there are valid exceptions to using base16, i.e. reasons to use fixed colors:

- Terminal based Presentations 
- Getting visually distinct output
- Compliance with CI rules 
- (...)


## mdv's Color Functions

You can express the foreground and background colors of text and borders. I.e. you have:

- `{color: <C>}`
- `{background-color: <C>}`
- `{border: 1em solid <C>}` or `{border-<direction>-color: <C>}`

where `<C>` can be (with examples):

- a hex code (e.g. `#FF0000`)
- a css color function
    - rgb(255, 0, 0)
    - hsl(50, 100%, 100%) (also: hls)
    - hsv(50, 50%, 50%) 
    - yiq(#ff0000)
    - ansi(124), ansi(1, 38, 4, 124, 4)

The `ansi` function is not a standard css function - you can provide any [ANSI](./ansi.md) sequence
here.




## Windows

We currently have not possibilty to test mdv on windows and are not sure about the state of ANSI
support there. But: At mdv startup, when we detect we are on windows we try:

```python
import colorama;
colorama.init()
```

This intercepts sys.stdout and maps ANSI Escape codes to windows compliant control sequences.

!!! important "Windows Support"
    pip install colorama and use only supported (coloroma mapped or natively supported) colors in
    mdv.



## Further Reading

(many taken from: [pastel][P])

Interesting Software:

* [pastel](https://github.com/sharkdp/pastel)

Interesting Wikipedia pages:

* [Color difference](https://en.wikipedia.org/wiki/Color_difference)
* [CIE 1931 color space](https://en.wikipedia.org/wiki/CIE_1931_color_space)
* [CIELAB color space](https://en.wikipedia.org/wiki/CIELAB_color_space)
* [Line of purples](https://en.wikipedia.org/wiki/Line_of_purples)
* [Impossible color](https://en.wikipedia.org/wiki/Impossible_color)
* [sRGB](https://en.wikipedia.org/wiki/SRGB)
* [Color theory](https://en.wikipedia.org/wiki/Color_theory)
* [Eigengrau](https://en.wikipedia.org/wiki/Eigengrau)

Color names:

* [XKCD Color Survey Results](https://blog.xkcd.com/2010/05/03/color-survey-results/)
* [Peachpuffs and Lemonchiffons - talk about named colors](https://www.youtube.com/watch?v=HmStJQzclHc)
* [List of CSS color keywords](https://www.w3.org/TR/SVG11/types.html#ColorKeywords)

Maximally distinct colors:

* [How to automatically generate N "distinct" colors?](https://stackoverflow.com/q/470690/704831)
* [Publication on two algorithms to generate (maximally) distinct colors](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.65.2790)

Other articles and videos:

* [Color Matching](https://www.youtube.com/watch?v=82ItpxqPP4I)
* [Introduction to color spaces](https://ciechanow.ski/color-spaces/)

[TC]: https://www.google.com/search?q=terminal+colors
[P]: https://github.com/sharkdp/pastel
[AE]: https://en.wikipedia.org/wiki/ANSI_escape_code
