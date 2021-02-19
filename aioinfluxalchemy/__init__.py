"""
InfluxDB Alchemy.
"""
import pkg_resources

from aioinfluxalchemy.client import AioInfluxAlchemy     # noqa: F401
from aioinfluxalchemy.measurement import Measurement  # noqa: F401


try:
    __version__ = pkg_resources.get_distribution(__package__).version
except pkg_resources.DistributionNotFound:  # pragma: no cover
    __version__ = None
