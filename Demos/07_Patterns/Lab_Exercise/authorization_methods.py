# Notification authorization / delivery callback methods
def authorize_email(message: str) -> None:
    print(f"[EMAIL AUTH] Email notification authorized for message: {message}")

def authorize_mobile(message: str) -> None:
    print(f"[MOBILE AUTH] Mobile notification authorized for message: {message}")

def authorize_none(message: str) -> None:
    print(f"[NO AUTH] User has opted out of all communication channels. No notification sent for message: {message}")

