from bank_account_receiver import BankAccount
from bank_invoker import BankInvoker
from command_interface_and_concrete_commands import DepositCommand
from command_interface_and_concrete_commands import WithdrawCommand

account = BankAccount("Peter", 1000)

invoker = BankInvoker()

# Create commands
invoker.add_command(DepositCommand(account, 200))
invoker.add_command(WithdrawCommand(account, 150))
invoker.add_command(WithdrawCommand(account, 2000))  # insufficient funds

# Execute all commands
invoker.run()