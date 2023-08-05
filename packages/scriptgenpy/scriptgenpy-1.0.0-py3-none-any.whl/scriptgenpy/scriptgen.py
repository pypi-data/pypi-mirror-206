import argparse
import os

def create_script_files(interpreter, script_path):
    script_name = os.path.splitext(os.path.basename(script_path))[0]
    """Tempalte for batch script"""
    cmd_content = f"""@ECHO off
SETLOCAL
SET dp0=%~dp0

SET "_prog={interpreter}"
SET PATHEXT=%PATHEXT:;.{interpreter};=;%

ENDLOCAL & GOTO #_undefined_# 2>NUL || title %COMSPEC% & "%_prog%"  "%dp0%\\{script_path}" %*"""
    """Template for powershell script"""
    ps1_content = f"""#!/usr/bin/env pwsh
$basedir=Split-Path $MyInvocation.MyCommand.Definition -Parent

$exe=""
if ($PSVersionTable.PSVersion -lt "6.0" -or $IsWindows) {{
  $exe=".exe"
}}
$ret=0

# Support pipeline input
if ($MyInvocation.ExpectingInput) {{
  $input | & "{interpreter}$exe"  "$basedir/{script_path}" $args
}} else {{
  & "{interpreter}$exe"  "$basedir/{script_path}" $args
}}
$ret=$LASTEXITCODE

exit $ret"""
    """Template for bash script"""
    sh_content = f"""#!/bin/sh
basedir=$(dirname "$(echo "$0" | sed -e 's,\\,/,g')")

case `uname` in
    *CYGWIN*|*MINGW*|*MSYS*) basedir=`cygpath -w "$basedir"`;;
esac

exec {interpreter}  "$basedir/{script_path}" "$@" """
    with open(f"{script_name}.cmd", "w") as f:
        f.write(cmd_content)
    with open(f"{script_name}.ps1", "w") as f:
        f.write(ps1_content)
    with open(f"{script_name}.sh", "w") as f:
        f.write(sh_content)

def main():
    parser = argparse.ArgumentParser(description="Create script files")
    parser.add_argument("interpreter", help="Interpreter to use")
    parser.add_argument("script_path", help="Path to the script")
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 1.0.0")
    args = parser.parse_args()
    create_script_files(args.interpreter, args.script_path)

if __name__ == "__main__":
    main()