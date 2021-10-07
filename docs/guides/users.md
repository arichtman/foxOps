# User guide

This file is intended to give a brief overview of the overall structure and use of foxOps. At this time the guide is aspirational and many features will still need to be developed and the design refined. Please see contributing documentation if you wish to assist with this.

## Basic structure

The primary syntax will be "foxops $object $verb". Config will be managed via a config object similar to `git` and `pip`. Configuration will be used to avoid repetition in supplying arguments e.g. Gitlab URL, access token. The primary method of nominating or identifying a gitlab project or group will be it's handle, as this is human-readable and trivial to resolve to an id. For a project this is the attribute `path_with_namespace`, though configuration will allow for a default namespace to fall back to.

Pull config `foxops project get arichtman/foxops-testing)` should return a structured dump of a project.

Compare objects `foxops project diff $contentFoo $contentBar` (I'm still thinking about whether this one should accept ids or addresses or straight json/yaml...)

Plan transition `foxops plan $contentFoo $contentBar` should return a structured output outlining what specific actions would be undertaken to transition each diff finding to the target state, as well as any transitions that were unable to be planned (as warnings? errors?).

## Differentials

There are some fields that would show in a raw differential that would be type 1 errors - one example is a sysmod or modified datetime value. There's not only no point updating this if it's the only property that's different, but it's impossible to actually set to a target state (barring a very broken gitlab instance). Further to this, there are some values that form the "core" of the attribute, such that we could identify settings that have not been removed, but rather renamed or moved. In the situation inline, the tool will identify that the rule object has not been removed, but rather renamed. The tool will also ignore the `added` attribute, as this cannot and should not be set external to Gitlab. In the example inline, it's likely that removal and re-addd of rules would be fine, but there will be other scenarios where this would destroy history or potentially leave objects in deadlocked states.

Existing state
```Yaml
project:
  rules:
    sqa_review:
      requires_users:
        - Andy
        - Jane
      quorum: 1
      added: 20211007T00:00:00Z
```

Target state
```Yaml
project:
  rules:
    quality_approval:
      requires_users:
        - Andy
        - Jane
      quorum: 1
      added: 20001231T12:12:12Z
```
