class BatchProcessor:
    def __init__(self):
        self.commands = []

    def add_command(self, cmd):
        self.commands.append(cmd)

    def run(self):
        for cmd in self.commands:
            cmd.execute()
