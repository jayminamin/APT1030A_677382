import re

def parse_command(command: str) -> dict:
    pattern = r"""
        ^TRANSFER\s+(?P<amount>\d+)
        \s+FROM\s+(?P<sender>[A-Z]+)
        \s+TO\s+(?P<receiver>[A-Z]+)
        \s+IF\s+BALANCE\s*(?P<op>[><=!]+)\s*(?P<threshold>\d+)$
    """
    match = re.match(pattern, command.strip(), re.IGNORECASE | re.VERBOSE)
    if not match:
        raise SyntaxError(f"Invalid DSL syntax: '{command}'")
    return {
        "amount":    int(match.group("amount")),
        "sender":    match.group("sender").upper(),
        "receiver":  match.group("receiver").upper(),
        "op":        match.group("op"),
        "threshold": int(match.group("threshold")),
    }
# Inteprator Logic

def eval_condition(balance: int, op: str, threshold: int) -> bool:
    ops = {">": lambda a, b: a > b, ">=": lambda a, b: a >= b,
           "<": lambda a, b: a < b, "<=": lambda a, b: a <= b,
           "==": lambda a, b: a == b, "!=": lambda a, b: a != b}
    if op not in ops:
        raise ValueError(f"Unsupported operator: {op}")
    return ops[op](balance, threshold)

def execute(command: str, accounts: dict) -> None:
    ast = parse_command(command)
    amount, sender, receiver = ast["amount"], ast["sender"], ast["receiver"]
    op, threshold = ast["op"], ast["threshold"]

    print(f"\n[PARSED]  Amount={amount}, From={sender}, To={receiver}, Cond=BALANCE {op} {threshold}")

    if sender not in accounts:
        print(f"[ERROR]  Account '{sender}' does not exist.")
        return
    if receiver not in accounts:
        print(f"[ERROR]  Account '{receiver}' does not exist.")
        return

    balance = accounts[sender]
    print(f"[CHECK]  {sender} balance = {balance}")

    if not eval_condition(balance, op, threshold):
        print(f"[REJECT] Condition BALANCE {op} {threshold} not satisfied.")
        return

    if amount > balance:
        print(f"[REJECT] Insufficient funds. Need {amount}, have {balance}.")
        return

    accounts[sender] -= amount
    accounts[receiver] += amount
    print(f"[OK]     Transferred {amount} from {sender} to {receiver}.")
    print(f"         {sender}: {accounts[sender]}  |  {receiver}: {accounts[receiver]}")

accounts = {"A": 8500, "B": 3200, "C": 1750}

execute("TRANSFER 5000 FROM A TO B IF BALANCE > 1000", accounts)
execute("TRANSFER 99999 FROM B TO C IF BALANCE > 500", accounts)
execute("TRANSFER 200 FROM B TO C IF BALANCE > 50",   accounts)
