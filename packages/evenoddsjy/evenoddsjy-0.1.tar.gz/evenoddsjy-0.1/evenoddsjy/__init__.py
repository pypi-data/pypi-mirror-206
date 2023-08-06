from importlib.metadata import PackageNotFoundError, version

from . import utils

try:
    __version__ = version('evenoddsjy')
except PackageNotFoundError:
    __version__ = '(local)'

del PackageNotFoundError
del version
