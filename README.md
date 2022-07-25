# aws-ami-delete

[![build and publish](https://github.com/lifeofguenter/aws-ami-delete/actions/workflows/build-and-publish.yml/badge.svg)](https://github.com/lifeofguenter/aws-ami-delete/actions/workflows/build-and-publish.yml)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/lifeofguenter/aws-ami-delete.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/lifeofguenter/aws-ami-delete/context:python)
[![PyPI](https://img.shields.io/pypi/v/aws-ami-delete.svg)](https://pypi.org/project/aws-ami-delete/)
[![License](https://img.shields.io/github/license/lifeofguenter/aws-ami-delete.svg)](LICENSE)

A simple CLI tool to delete AMIs (including their corresponding snapshots),
optionally read from a [packer manifest](https://www.packer.io/docs/post-processors/manifest).

## Install

```bash
$ pip install --user aws-ami-delete
```

## Usage

Either specify AMI IDs as args:

```bash
$ aws-ami-delete i-124566 i-56789
```

Or, specify the path to the manifest file:

```bash
$ aws-ami-delete ./manifest.json
```
