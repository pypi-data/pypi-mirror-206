from enum import Enum


class Shell(Enum):
    """Available executable for console.

    See :meth:`pawapi.api.Console.create()`
    """

    BASH = "bash"
    MYSQL = "mysql"
    PYTHON310 = "python3.10"
    PYTHON39 = "python3.9"
    PYTHON38 = "python3.8"
    PYTHON37 = "python3.7"
    PYTHON36 = "python3.6"
    IPYTHON310 = "ipython3.10"
    IPYTHON39 = "ipython3.9"
    IPYTHON38 = "ipython3.8"
    IPYTHON37 = "ipython3.7"
    IPYTHON36 = "ipython3.6"
    PYPY2 = "pypy2"
    PYPY3 = "pypy3"
