# from account import Account
# from currentaccount import CurrentAccount
# from isaaccount import ISAAccount
from factory import Factory

# Example usage
if __name__ == "__main__":

    current = Factory.create("CurrentAccount", "CA123", 100, overdraft_limit=300)
    isa = Factory.create("ISAAccount", "ISA456", 500, max_balance=20000)

    current.withdraw(350)   # allowed within overdraft
    current.withdraw(100)   # exceeds overdraft

    isa.deposit(19000)      # may exceed limit
    isa.withdraw(100)


    current = Factory.create_generic("CurrentAccount", "GCA123", 100, overdraft_limit=300)
    isa = Factory.create_generic("ISAAccount", "GISA456", 10000, max_balance=20000)

    current.withdraw(350)   # allowed within overdraft
    current.withdraw(100)   # exceeds overdraft

    isa.deposit(19000)      # may exceed limit
    isa.withdraw(100)