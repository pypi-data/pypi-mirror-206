# scriptgen_py

_ScriptGenPy_ is a command-line based script generator tool that simplifies the process of running scripts in any language.

## Introduction

When a script is executed using an interpreter, the command line statement can become quite long as it includes the interpreter path, script path, and all required arguments. _ScriptGenPy_ addresses this issue by consolidating the interpreter and script paths into a short command that can be easily accessed from anywhere in the system. This means that when calling the script via command, only the arguments need to be passed.

_ScriptGenPy_ generates commands for all operating systems. For Windows, it generates batch and PowerShell scripts. For macOS, it generates Shell scripts and PowerShell scripts which can be used if PowerShell is installed. For Linux, it generates Shell scripts. This makes it easy to run scripts on any platform without having to manually create the appropriate command.

### Working

Here's a Python script that takes two positional arguments: `interpreter` and `script_path`. It also has a `-v`/`--version` option to show the version information. You can run it with `python scriptgen.py <interpreter> <script_path>`.

## Build

To setup _ScriptGenPy_, you need to clone the repository from GitHub.

```sh
git clone https://github.com/isurfer21/scriptgen_py.git
```

After running these commands, you should have a local copy of _ScriptGenPy_ that is ready to use.

To use _ScriptGenPy_, navigate to the project directory and run the appropriate command.

```sh
cd scriptgen_py
python src/scriptgen.py -h
```

If it displays the help menu, the script is working!

## Usage

_ScriptGenPy_ is a command-line tool for creating script files. To use _ScriptGenPy_, you need to specify the interpreter to use and the path to the script.

```sh
scriptgenpy [interpreter] [script_path]
```

For example, to create a Python script at `/path/to/script.py`, you would run the following command:

```sh
scriptgenpy python /path/to/script.py
```

ScriptGen also supports several options:

- `-h`, `--help`: Show the help message and exit.
- `-v`, `--version`: Show the program's version number and exit.

For example, to show the version number of ScriptGen, you would run the following command:

```sh
scriptgenpy -v
```

This would output the version number of ScriptGen, which is currently `1.0.0`.

### Examples

Here are some additional examples of how to use _ScriptGenPy_:

- To create a Bash script at `/path/to/script.sh`, you would run the following command:

```sh
scriptgenpy bash /path/to/script.sh
```

- To create a Ruby script at `/path/to/script.rb`, you would run the following command:

```sh
scriptgenpy ruby /path/to/script.rb
```

- To create a Perl script at `/path/to/script.pl`, you would run the following command:

```sh
scriptgenpy perl /path/to/script.pl
```

## Publish

Here is the process to make the app ready for distribution.

### Generating distribution archives

To generate distribution packages for the package. Make sure you have the latest version of PyPA’s build installed:

```sh
python3 -m pip install --upgrade build
```

Now run this command from the same directory where `pyproject.toml` is located:

```sh
python3 -m build
```

### Uploading the distribution archives to Test PyPi

Finally, it’s time to upload your package to the Python Package Index!

Ensure to have an independent account on both platforms:

- [Test PyPI](https://test.pypi.org/)
- [PyPI](https://pypi.org/)

After that, you can use twine to upload the distribution packages. You’ll need to install Twine:

```sh
python3 -m pip install --upgrade twine
```

Once installed, run Twine to upload all of the archives under dist:

```sh
python3 -m twine upload --repository testpypi dist/*
```

You will be prompted for a _username_ and _password_. For the _username_, use `__token__`. For the _password_, use the token value, including the `pypi-` prefix.

### Installing the uploaded package from Test PyPi

You can use [pip](https://pip.pypa.io/en/stable/installation/) to install your package.

```sh
pip install -i https://test.pypi.org/simple/ scriptgenpy
```

### Uploading the package to PyPI

Similar to Test PyPI, uploading to PyPI. Put this command into action:

```sh
python -m twine upload dist/*
```

Upon successful upload, your package will be visible on the PyPI website. You may discover the uploaded package by searching the 'scriptgenpy' at PyPI.

### Installing the package from PyPi

Now that the app is public, anyone may download it and install it by using the following command.

```sh
pip install scriptgenpy
```