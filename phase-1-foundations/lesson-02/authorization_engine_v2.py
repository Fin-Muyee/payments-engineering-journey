# ─────────────────────────────────────────────────────────────
# Authorization Engine — Phase 1, Lesson 2
# A reusable function that processes any transaction
# ─────────────────────────────────────────────────────────────

def authorize_transaction(
    card_status,
    pin_correct,
    fraud_score,
    available_balance,
    transaction_amount,
    daily_limit,
    spent_today
):
    """
    Processes an authorization request through 6 sequential checks.
    Returns a tuple of (response_code, decision, reason).
    """

    # Check 1 — Card status
    if card_status != "active":
        return ("41", "DECLINED", "Card not active")

    # Check 2 — PIN verification
    if pin_correct == False:
        return ("55", "DECLINED", "Incorrect PIN")

    # Check 3 — Fraud screening
    if fraud_score >= 80:
        return ("59", "DECLINED", "Suspected fraud")

    # Check 4 — Sufficient balance
    if available_balance < transaction_amount:
        return ("51", "DECLINED", "Insufficient funds")

    # Check 5 — Daily limit
    if (spent_today + transaction_amount) > daily_limit:
        return ("61", "DECLINED", "Daily limit exceeded")

    # All checks passed
    return ("00", "APPROVED", "All checks passed")


def print_authorization_result(transaction_id, amount, currency, result):
    """
    Prints a formatted authorization response.
    """
    response_code, decision, reason = result
    print(f"\n{'='*45}")
    print(f"  Transaction ID : {transaction_id}")
    print(f"  Amount         : {amount/100:.2f} {currency}")
    print(f"  Decision       : {decision}")
    print(f"  Response Code  : {response_code}")
    print(f"  Reason         : {reason}")
    print(f"{'='*45}")


# ─────────────────────────────────────────────────────────────
# Test the engine with multiple transactions
# ─────────────────────────────────────────────────────────────

# Transaction 1 — Should be APPROVED
result1 = authorize_transaction(
    card_status="active",
    pin_correct=True,
    fraud_score=30,
    available_balance=500000,
    transaction_amount=150000,
    daily_limit=300000,
    spent_today=100000
)
print_authorization_result("TXN-001", 150000, "NGN", result1)


# Transaction 2 — Should DECLINE: Insufficient funds
result2 = authorize_transaction(
    card_status="active",
    pin_correct=True,
    fraud_score=30,
    available_balance=100000,
    transaction_amount=150000,
    daily_limit=300000,
    spent_today=0
)
print_authorization_result("TXN-002", 150000, "NGN", result2)


# Transaction 3 — Should DECLINE: Suspected fraud
result3 = authorize_transaction(
    card_status="active",
    pin_correct=True,
    fraud_score=92,
    available_balance=500000,
    transaction_amount=150000,
    daily_limit=300000,
    spent_today=0
)
print_authorization_result("TXN-003", 150000, "NGN", result3)


# Transaction 4 — Should DECLINE: Daily limit exceeded
result4 = authorize_transaction(
    card_status="active",
    pin_correct=True,
    fraud_score=20,
    available_balance=500000,
    transaction_amount=150000,
    daily_limit=300000,
    spent_today=200000
)
print_authorization_result("TXN-004", 150000, "NGN", result4)


# Transaction 5 — Should DECLINE: Card not active
result5 = authorize_transaction(
    card_status="blocked",
    pin_correct=True,
    fraud_score=20,
    available_balance=500000,
    transaction_amount=150000,
    daily_limit=300000,
    spent_today=0
)
print_authorization_result("TXN-005", 150000, "NGN", result5)