from dataclasses import dataclass, replace, field
from datetime import datetime
from copy import deepcopy
from typing import Optional

from data.models.user_role import UserRole


@dataclass(frozen=True)
class User:
    full_name: str
    aliases: list[str] = field(default_factory=list)
    role: UserRole = UserRole.CHAMPION
    telegram_username: str = ''
    birthday: Optional[str] = None
    telegram_id: Optional[int] = None
    loyverse_id: Optional[str] = None
    last_private_chat: Optional[datetime] = None
    last_visit: Optional[datetime] = None
    recent_visits: int = 0

    @property
    def first_name(self) -> str:
        return self.full_name.split(' ')[0]

    @property
    def main_alias(self) -> Optional[str]:
        return self.aliases[0] if self.aliases else None

    def __eq__(self, other):
        return self.full_name == other.full_name

    def __hash__(self):
        return hash(self.full_name)

    def copy(self, **changes) -> 'User':
        return replace(deepcopy(self), **changes)
