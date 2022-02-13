# Decision register

Here is the space to record any decisions of significance, and the surrounding details. This project uses [templated Y-statements](/templates/y-statements.md) for brevity and structure.

![Y-statement](https://miro.medium.com/max/875/1*1iYhZi6l7J-_q0LAiTHGJA.png)

## 00. Testing framework

In the context of having to select an initial testing framework, facing no code and no peer guidance, we decided for pytest to achieve a well-supported framework that we shared with our dependency project, accepting that it may not be as modern or legible as other projects like nose2 and behave.

## 01. Argument module

In the context of selecting an argument parsing module, facing our requirements and time shortage we decided for typer to achieve speed from intuitive syntax allowing subcommands, accepting that environment variables and configuration files will not make this iteration.

Notes:

- jsonargparse - imperative definition, unintuitive syntax, focus on configuration files, not super mature or popular. Might use it for the config file reading.
- configargparse - supports a lot of what we want, just still imperative argument declaration. Look into this one eventually
- click - really nice and mature, plenty popular, company support even! might use this one
- typer - built ontop of click so all those benefits + some additional features, not super mature though popular and supports subcommands while using annotations and typing.

## 02. Configuration management and storage

In the context of features around storing, using, and modifying configuration, facing the option to implement we decided not to implement to achieve focus on core functionality, accepting that only a handful of values would go into the configuration and it wouldn't save much over supporting `.env` files. See #14 for some more thoughts
