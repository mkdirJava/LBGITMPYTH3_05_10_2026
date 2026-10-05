# Invoker
class BankInvoker:
    def __init__(self):
        self._commands = []

    def add_command(self, command):
        self._commands.append(command)

    def run(self):
        for command in self._commands:
            command.execute()
