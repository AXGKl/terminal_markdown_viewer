# Plugin `log`: Provides Logging

## General Functionality

Provides the usual log methods throughout the application.


## Default Implementation: :srcref:fn=src/mdv/plugins/structlog.py,t=structlog.py

See [here](https://www.structlog.org/en/stable/)

## Custom Implementation

Logging system must support `**kw` style logging, e.g. `log.debug("foo", bar=42)` 
