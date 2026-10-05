from batch_processor_invoker import BatchProcessor
from file_system_receiver import FileSystem
from command_interface_and_concrete_commands import CreateFolderCommand
from command_interface_and_concrete_commands import CreateFileCommand
from command_interface_and_concrete_commands import RenameFileCommand
from command_interface_and_concrete_commands import MoveFileCommand

# Example banking workflow
# Daily Transaction Processing System

fs = FileSystem()
processor = BatchProcessor()

# 1. Create a daily processing folder
processor.add_command(CreateFolderCommand(fs, "processing/2026-05-28"))

# 2. Create a transaction file in a specified folder
processor.add_command(CreateFileCommand(fs, "transactions.txt"))

# 3. Rename raw transaction file
processor.add_command(RenameFileCommand(fs, "transactions.txt", "transactions_2026-05-28.txt"))

# 4. Move file into processing folder
processor.add_command(MoveFileCommand(
    fs,
    "transactions_2026-05-28.txt",
    "processing/2026-05-28/transactions_2026-05-28.txt"
))

# Execute all steps
processor.run()