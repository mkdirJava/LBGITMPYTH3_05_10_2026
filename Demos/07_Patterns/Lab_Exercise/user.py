from dataclasses import dataclass

@dataclass(eq=True, frozen=True)
class User:
    name: str
    subscription_type: str  # "email", "mobile", or "none"
    destination: str | None = None