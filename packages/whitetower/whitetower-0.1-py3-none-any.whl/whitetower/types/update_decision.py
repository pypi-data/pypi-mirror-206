import enum

class UpdateDecision(enum.Enum):
    perform_update = 1
    """Update as soon as possible"""

    postpone_update = 2
    """Perform pre-update checks again"""

    skip_this_version = 3
    """Do not update to this version"""
