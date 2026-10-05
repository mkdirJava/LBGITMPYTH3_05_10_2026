from user import User
from dataclasses import dataclass, field
from typing import Callable

# Subscriber model
AuthCallback = Callable[[str], None]

# Publisher
@dataclass
class EISCDChangeNotifier:
    """
    Publisher in a simple subscriber design pattern.

    Each subscriber is associated with a callback that is executed
    automatically when a weekly EISCD change notification is published.
    """
    _subscribers: dict[User, AuthCallback] = field(default_factory=dict)

    def subscribe(self, user: User, callback: AuthCallback) -> None:
        self._subscribers[user] = callback
        print(
            f"[SUBSCRIBE] {user.name} registered with type={user.subscription_type!r}"
        )

    def unsubscribe(self, user: User) -> None:
        removed = self._subscribers.pop(user, None)
        if removed is not None:
            print(f"[UNSUBSCRIBE] {user.name} removed from notifications")
        else:
            print(f"[UNSUBSCRIBE] {user.name} was not subscribed")

    def notify(self, message: str) -> None:
        print("\n" + "=" * 80)
        print(f"[PUBLISH] Weekly EISCD update: {message}")
        print("=" * 80)

        if not self._subscribers:
            print("[PUBLISH] No active subscribers")
            return

        for user, callback in self._subscribers.items():
            print(
                f"[CALLBACK] Triggering callback for {user.name} "
                f"({user.subscription_type})"
            )
            callback(message)
