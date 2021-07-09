"""
*Assignment: About Environment
*Complexity: easy
*Lines of code: 0 lines

Requirements
    1. Create file `about_env.py`
    2. Run file in your IDE
    3. Where Python is installed?
    4. Are you using "venv"?
    5. Make sure, `venv` is not `None`
    6. Run Doctests - ass must succeed

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert python_executable
    >>> assert python_version
"""
import sys
import os

python_executable = sys.executable
python_version = tuple(sys.version_info)
venv = os.getenv("VIRTUAL_ENV")

# print(python_executable + "\n" + venv)
print(f"{python_executable} \n + {venv} \n + {python_version}")
# print(python_version)
