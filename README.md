### Hexlet tests and linter status:
[![Actions Status](https://github.com/Osayanny/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Osayanny/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/e8b0d54a85c32b584e93/maintainability)](https://codeclimate.com/github/Osayanny/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/e8b0d54a85c32b584e93/test_coverage)](https://codeclimate.com/github/Osayanny/python-project-50/test_coverage)
---

### Description
---
This project is a difference calculator for files. Supported files format: Json and yaml.

Difference calculator supported three formats of view (default stylish):
* [![Stylish](https://asciinema.org/a/xtv4kms6Irv01zshl3FHawOkQ)](https://asciinema.org/a/xtv4kms6Irv01zshl3FHawOkQ)
* [![Plain](https://asciinema.org/a/2xYeuAkSHq7pzNBBebkM4i8OH)](https://asciinema.org/a/2xYeuAkSHq7pzNBBebkM4i8OH)
* [![json for import](https://asciinema.org/a/lLjYKvabKqw2jq60LrExPVsW4)](https://asciinema.org/a/lLjYKvabKqw2jq60LrExPVsW4)

### How to install
---
To install the package you need pipx version 1.4.3 and python 3.12 or highest.

1. Clone this repository and install manually:
```bash
$ git clone https://github.com/Osayanny/python-project-50.git
$ cd python-project-50 && make build && make package-install
```

### How it work:
---
To start working with the difference calculator, you need to write the command:
```bash
$ gendiff <path_to_file_1> <path_to_file_2> [optional -f, --format]
```