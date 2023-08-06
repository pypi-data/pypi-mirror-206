"""sbioapputils"""

import logging

from . import app_runner, file_process
from importlib.metadata import version

package_name = 'sbioapputils'
__version__ = version(package_name)