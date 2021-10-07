# Requirements register

This document contains requirements for the project.

## Arguments module

This section outlines the needs and wants for a framework or module to manage arguments and configuration of the cli tool. All listed requirements here can be considered as desireable but not must-have. The project is far too nascent to be making hard rules at this stage.

Requirements:

- Can define arguments declaratively using data structures, as opposed to imperatively in code
- Supports coalescing in environment variables
- Supports coalescing in from configuration file
- Supports `@`-notation for reading values from files
- Allows validation of argument types
- Supports cli syntax of both `--long-value` and `-lv`
- Supports cli syntax of both `-v=1234` and `-v 1234`
- Supports cli syntax of both `-v string` and `-v "string"`
- Supports different arguments depending on the first and second e.g. `push (--hands | --feet)` but only `pull --hands` would be valid
