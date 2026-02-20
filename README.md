# StartGGTools

Tiny module for various startgg functionalities for TO'ing.

Currently only one functionality is implemented: `fetch-players`

Usage:

```
startgg-tools --config [config-path] fetch-players [bracket-url] [out-path]
```

Code is a little over-complicated because it's extracted from a FAR far more complicated project. Uh, enjoy!

## Fetch-Players

Outputs a csv of registered players, in the following format:

```
"start.gg name","prefix","discord name","pronouns"
```

prefix, discord name, and pronouns are empty if not present, such as:

```
"systemagical",,,
```

This CSV can be provided to streamcontrol in place of its players.csv -- DEPENDING ON HOW YOURS IS CUSTOMIZED.

## Options

### CONFIG file

Config file should look as follows:
```
[default]
Authorization = Bearer [token]
```

Token should be taken from start.gg. See the API help [here](https://developer.start.gg/docs/authentication) for more information.

### Bracket URL

Path to the literal bracket -- not the tournament, the specific event in the overall tournament.

### Out Path

Where to save the output csv.
