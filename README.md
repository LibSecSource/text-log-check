# TextLogCheck

A Python package for analyzing, verifying, and monitoring text-based log files. 
Includes tools for file existence checks, log tail analysis, text searches, and more. 

You can find **Full Project Documentation** [here][documentation_path]

<hr>

#### Workflows
[![Tests](https://github.com/LibSecSource/text-log-check/actions/workflows/run-tests.yml/badge.svg?branch=main)](https://github.com/LibSecSource/text-log-check/actions/workflows/run-tests.yml)
[![Pylint](https://github.com/LibSecSource/text-log-check/actions/workflows/lint.yml/badge.svg?branch=main)](https://github.com/LibSecSource/text-log-check/actions/workflows/lint.yml)

#### Package
[![Version](https://img.shields.io/pypi/v/text-log-check.svg)](https://pypi.python.org/pypi/text-log-check/)
[![Development Status](https://img.shields.io/pypi/status/text-log-check.svg)](https://pypi.python.org/pypi/text-log-check)
[![Python version](https://img.shields.io/pypi/pyversions/text-log-check.svg)](https://pypi.python.org/pypi/text-log-check/)
[![License](https://img.shields.io/pypi/l/text-log-check)](https://github.com/LibSecSource/text-log-check/blob/main/LICENSE)
[![Wheel](https://img.shields.io/pypi/wheel/text-log-check.svg)](https://pypi.python.org/pypi/text-log-check/)

#### Support
[![Documentation](https://img.shields.io/badge/docs-0094FF.svg)][documentation_path]
[![Discussions](https://img.shields.io/badge/discussions-ff0068.svg)](https://github.com/LibSecSource/text-log-check/discussions/)
[![Issues](https://img.shields.io/badge/issues-11AE13.svg)](https://github.com/LibSecSource/text-log-check/issues/)

#### Downloads
[![Day Downloads](https://img.shields.io/pypi/dd/text-log-check)](https://pepy.tech/project/text-log-check)
[![Week Downloads](https://img.shields.io/pypi/dw/text-log-check)](https://pepy.tech/project/text-log-check)
[![Month Downloads](https://img.shields.io/pypi/dm/text-log-check)](https://pepy.tech/project/text-log-check)
[![All Downloads](https://img.shields.io/pepy/dt/text-log-check)](https://pepy.tech/project/text-log-check)

#### Languages
[![Languages](https://img.shields.io/github/languages/count/LibSecSource/text-log-check)](https://github.com/LibSecSource/text-log-check)
[![Top Language](https://img.shields.io/github/languages/top/LibSecSource/text-log-check)](https://github.com/LibSecSource/text-log-check)

#### Development
- [![Release date](https://img.shields.io/github/release-date/LibSecSource/text-log-check
)](https://github.com/LibSecSource/text-log-check/releases)
[![Last Commit](https://img.shields.io/github/last-commit/LibSecSource/text-log-check/main
)](https://github.com/LibSecSource/text-log-check)
- [![Issues](https://img.shields.io/github/issues/LibSecSource/text-log-check
)](https://github.com/LibSecSource/text-log-check/issues/)
[![Closed Issues](https://img.shields.io/github/issues-closed/LibSecSource/text-log-check
)](https://github.com/LibSecSource/text-log-check/issues/)
- [![Pull Requests](https://img.shields.io/github/issues-pr/LibSecSource/text-log-check
)](https://github.com/LibSecSource/text-log-check/pulls)
[![Closed Pull Requests](https://img.shields.io/github/issues-pr-closed-raw/LibSecSource/text-log-check
)](https://github.com/LibSecSource/text-log-check/pulls)
- [![Discussions](https://img.shields.io/github/discussions/LibSecSource/text-log-check
)](https://github.com/LibSecSource/text-log-check/discussions/)

[//]: # (#### Repository Stats)

[//]: # ([![Stars]&#40;https://img.shields.io/github/stars/LibSecSource/text-log-check)

[//]: # (&#41;]&#40;https://github.com/LibSecSource/text-log-check&#41;)

[//]: # ([![Contributors]&#40;https://img.shields.io/github/contributors/LibSecSource/text-log-check)

[//]: # (&#41;]&#40;https://github.com/LibSecSource/text-log-checkgraphs/contributors&#41;)

[//]: # ([![Forks]&#40;https://img.shields.io/github/forks/LibSecSource/text-log-check)

[//]: # (&#41;]&#40;https://github.com/LibSecSource/text-log-check&#41;)

<hr>

## Menu

- [Mission](#mission)
- [Open Source Project](#open-source-project)
- [Features](#features)
- [Requirements](#requirements)
- [Development Status](#development-status)
- [Install](#install)
- [Quickstart](#quickstart)
- [Contributing](#contributing)

## Mission

To provide a reliable, open-source Python solution for managing and analyzing text-based log files, 
empowering developers, system administrators, and security professionals with tools to 
ensure log integrity, streamline troubleshooting, and enhance system monitoring practices.

## Open Source Project

This is the open source project with [Happy Code](LICENSE) license.
Be free to use, fork, clone and contribute.

## Features

- Check if log file exists
- Check if user can change log file (Plan)
- Check if user can delete log file (Plan)
- Check if user can clear log file (Plan)
- Search text in log file (Plan)
- Read tail of log file (Plan)
- Modify log file (Plan)
- Clear log file (Plan)

## Requirements

- python >= 3
- See more in [Full Documentation](https://libsecsource.github.io/text-log-check/about.html#requirements)

## Development Status

- Package already available on [PyPi](https://pypi.org/project/text-log-check/)
- See more in [Full Documentation](https://libsecsource.github.io/text-log-check/about.html#development-status)

## Install

### with pip

```commandline
pip install text-log-check
```

See more in [Full Documentation](https://libsecsource.github.io/text-log-check/install.html)

## Quickstart

```python
from text_log_check import exists

print(exists('/var/log/auth.log'))
```

### More examples in [Full Documentation][documentation_path]

## Contributing

You are welcome! To easy start please check:
- [Full Documentation][documentation_path]
- [Contributing](CONTRIBUTING.md)
- [Developer Documentation](https://libsecsource.github.io/text-log-check/dev_documentation.html)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Security Policy](SECURITY.md)
- [Governance](GOVERNANCE.md)
- [Support](SUPPORT.md)

[documentation_path]: https://libsecsource.github.io/text-log-check/