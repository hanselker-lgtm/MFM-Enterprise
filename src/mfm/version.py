"""
Version information.
"""

__version__ = "0.3.0-rc1"

#: Release channel for this build. One of "dev", "rc", "stable".
__build_channel__ = "rc"

#: Build/release identifier. Overridable via the MFM_BUILD_ID environment
#: variable by packaging tooling; falls back to the version string so a
#: source checkout still reports something meaningful.
import os as _os

__build_id__ = _os.environ.get("MFM_BUILD_ID", f"{__version__}-local")
