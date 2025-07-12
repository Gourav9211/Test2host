from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from core import Quotient

from tortoise import models
from tortoise.models import Model

class BaseDbModel(Model):
    class Meta:
        abstract = True

# Note: BaseDbModel is kept for compatibility but will be phased out
# as we migrate to Replit DB

from .esports import *
from .misc import *