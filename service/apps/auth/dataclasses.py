from dataclasses import dataclass
from typing import List, Optional

from rest_framework_simplejwt.tokens import RefreshToken


@dataclass
class AuthenticationResult:
    errors: Optional[List[str]] = None
    token: Optional[RefreshToken] = None

    def has_errors(self) -> bool:
        return bool(self.errors)

    def refresh_token(self) -> str:
        return str(self.token)

    def access_token(self) -> str:
        return str(self.token.access_token)
