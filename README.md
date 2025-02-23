# nt_py_scripts

This repository offers Python implementations of various numerical methods for finding roots of equations.

## Contents

- **bisection.py**: Implements the **Bisection Method**, a bracketing technique that repeatedly halves an interval to locate a root.

- **falseposition.py**: Implements the **False Position (Regula Falsi) Method**, which uses a secant line within a bracketing interval to approximate the root.

- **newton_raphson.py**: Implements the **Newton-Raphson Method**, an open method that utilizes tangents to find successively better approximations of a root.

- **secant.py**: Implements the **Secant Method**, similar to Newton-Raphson but avoids the need for derivative computation by using secant lines.

## Usage

Each script is standalone and can be executed directly. They include example functions demonstrating how to use the implemented methods.  

To run a script, use:

```bash
python script_name.py
```
just replace ``` script_name.py``` to one of the chosen scripts to be executed.