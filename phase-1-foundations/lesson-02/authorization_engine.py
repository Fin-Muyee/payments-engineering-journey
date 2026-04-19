card_status = "active"
pin_correct = True
fraud_score = 45
available_balance = 100000    # ₦5,000.00
transaction_amount = 150000   # ₦1,500.00
daily_limit = 300000          # ₦3,000.00
spent_today = 100000          # ₦1,000.00 already spent

if card_status != "active":
    print("DECLINED — Response Code: 41")
    print("Reason: Card not active")

if pin_correct == False:
    print("DECLINED — Response Code: 55")
    print("Reason: Incorrect PIN")

elif fraud_score >= 80:
    print("DECLINED — Response Code: 59")
    print("Reason: Suspected fraud")

elif available_balance < transaction_amount:
    print("DECLINED — Response Code: 51")
    print("Reason: Insufficient funds")

elif (spent_today + transaction_amount) > daily_limit:
    print("DECLINED — Response Code: 61")
    print("Reason: Daily limit exceeded")

else:
    print("APPROVED — Response Code: 00")
    print("Reason: All checks passed")