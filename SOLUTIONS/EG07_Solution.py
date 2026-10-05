#from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable


# Subscriber model
AuthCallback = Callable[[str], None]

@dataclass(eq=True, frozen=True)
class User:
    name: str
    subscription_type: str  # "email", "mobile", or "none"
    destination: str | None = None


# Notification authorization / delivery callbacks
def authorize_email(message: str) -> None:
    print(f"[EMAIL AUTH] Email notification authorized for message: {message}")

def authorize_mobile(message: str) -> None:
    print(f"[MOBILE AUTH] Mobile notification authorized for message: {message}")

def authorize_none(message: str) -> None:
    print(f"[NO AUTH] User has opted out of all communication channels. No notification sent for message: {message}")

# Publisher
@dataclass
class EISCDChangeNotifier:
    """
    Publisher in a simple subscriber pattern.

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
        print("\n" + "=" * 72)
        print(f"[PUBLISH] Weekly EISCD update: {message}")
        print("=" * 72)

        if not self._subscribers:
            print("[PUBLISH] No active subscribers")
            return

        for user, callback in self._subscribers.items():
            print(
                f"[CALLBACK] Triggering callback for {user.name} "
                f"({user.subscription_type})"
            )
            callback(message)


# Test
def main() -> None:
    notifier = EISCDChangeNotifier()

    # Register 3 different users: one email, one mobile, one none
    email_user = User(
        name="Frank",
        subscription_type="email",
        destination="frank.boifur@qa.com",
    )
    mobile_user = User(
        name="Jess",
        subscription_type="mobile",
        destination="+44712900123",
    )
    none_user = User(
        name="Phil",
        subscription_type="none",
        destination=None,
    )

    notifier.subscribe(email_user, authorize_email)
    notifier.subscribe(mobile_user, authorize_mobile)
    notifier.subscribe(none_user, authorize_none)

    # First notification
    notifier.notify(
        "EISCD weekly refresh has been loaded: 13 sort codes updated, 2 closed, 1 redirected."
    )

    # Remove the mobile user
    notifier.unsubscribe(mobile_user)

    # Second notification
    notifier.notify(
        "EISCD weekly refresh has been loaded: 7 sort codes updated, 1 CHAPS flag changed."
    )


if __name__ == "__main__":
    main()