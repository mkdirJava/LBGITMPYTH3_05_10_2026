from eiscdChangeNotifier import EISCDChangeNotifier
from user import User
from authorization_methods import authorize_email, authorize_mobile, authorize_none
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

    # Remove the mobile user from the business unit
    notifier.unsubscribe(mobile_user)

    # Second notification
    notifier.notify(
        "EISCD weekly refresh has been loaded: 7 sort codes updated, 1 CHAPS flag changed."
    )

if __name__ == "__main__":
    main()
