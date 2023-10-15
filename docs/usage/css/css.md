# Styling with CSS

You can use a restricted set of CSS to style the output.

## Supported Selectors

We use [SoupSieve][SS] for matching CSS selectors with the html to be styled. See it's [extensive documentation][SS] for all supported mechanics. 

## Supported [CSS Shorthands][CSH].

These are expanded into specific attributes, if those are missing.

- border (e.g. `border: 2.2em dashed hsl(40, 100%, 50%)`)
- border[-`<direction>`]
- margin[-`<direction>`]
- padding[-`<direction>`]



## Supported CSS Functions

### mdv's CSS Color Functions

In stylesheets you can express the foreground and background colors of text and borders. I.e. you have:

- `{color: <C>}`
- `{background-color: <C>}` (css shorthand `background` with only color is an alias)
- `{border: 1em solid <C>}` or `{border-<direction>-color: <C>}`

where `<C>` can be (with examples):

- For **fixed colors**:
    - a hex code (e.g. `#FF0000`)
    - a css color function
        - rgb(255, 0, 0)
        - hsl(50, 100%, 100%) (also: hls)
        - hsv(50, 50%, 50%) 
        - yiq(#ff0000)
        - ansi(<16-255>)  (below 16 we have the system colors), mapped to \x1b[38;5;<nr>m`

- For **system colors**:
    - ansi(6), ansi(1, 4, 38, 5, 6) (which would not only define to use foreground base color 6 but also [set](./ansi.md) underline and bold (4 and 1) 
    - mdv uses by default themable system colors, when you specify their [standarized](<{config.repo_url}>src/mdv/plugins/color_table_256.py) names. You can switch this to using true colors by setting `colors_256` to "color_table_256_true".

The `ansi` function is not a standard css function - you can provide any [ANSI](./ansi.md) sequence
here.



## Supported CSS Attributes

### background-color



### color

Foreground text or border color


[SS]: https://facelessuser.github.io/soupsieve/selectors/
[CSH]: https://developer.mozilla.org/en-US/docs/Web/CSS/Shorthand_properties
