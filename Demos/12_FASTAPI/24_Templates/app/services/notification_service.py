from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")

def generate_overdraft_email_text(customer_name: str, account_id: int, balance: float) -> str:
    template = templates.get_template("emails/overdraft_warning.txt")

    return template.render(
        customer_name=customer_name,
        account_id=account_id,
        balance=balance
    )


def generate_overdraft_email_html(customer_name: str, account_id: int, balance: float) -> str:
    template = templates.get_template("emails/overdraft_warning.html")

    return template.render(
        customer_name=customer_name,
        account_id=account_id,
        balance=balance
    )

