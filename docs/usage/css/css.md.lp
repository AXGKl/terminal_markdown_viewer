# Styling with CSS

You can use a restricted set of CSS to style the output.

## Supported Selectors

We use [SoupSieve][SS] for matching CSS selectors with the html to be styled. See it's [extensive documentation][SS] for all supported mechanics. 

## Supported [CSS Shorthands][CSH].

These are expanded into specific attributes, if those are missing.

- border (e.g. `border: 2.2em dashed hsl(40, 100%, 50%)`)
- border-`<direction>`
- margin
- padding


## Supported CSS Functions

### Color Functions

=== "foo"
    bar


## Supported CSS Attributes

### color

Foreground text or border color


[SS]: https://facelessuser.github.io/soupsieve/selectors/
[CSH]: https://developer.mozilla.org/en-US/docs/Web/CSS/Shorthand_properties
