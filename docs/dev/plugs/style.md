# Plugin `style`: Per Tag CSS Object

## General Functionality

Provides normalized CSS information for each html tag.

Called by: [`term_render`](./render.md)

## Default Implementation: :srcref:fn=src/mdv/plugins/style.py,t=style.py

Works via decorators which calculate the wanted style.

## Custom Implementation

Would have to provide the same API. Extensions for further CSS attributes via inheritance.
