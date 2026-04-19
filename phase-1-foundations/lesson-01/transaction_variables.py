#------------------------------------------------
# Lesson 1 Exercise - Declined Transaction
# Phase 1: Foundations
#------------------------------------------------
# Amount in minor units (kobo) - N12,000 = 1,200,000 kobo
transaction_amount = 1200000

# Currency as ISO code
currency = "NGN"

# Merchant ID
merchant_id = "MID:90210"

# Response code for insufficient funds
response_code = "51"

# Approval flag - declined
is_approved = False

# Human readable decline reason
decline_reason = "Insufficient funds"

#--------------------------------------------------
# Print the transaction summary
#--------------------------------------------------
print("===== Transaction Summary =====")
print(f"Amount: {transaction_amount} {currency}")
print(f"Merchant ID: {merchant_id}")
print(f"Response Code: {response_code}")
print(f"Is Approved: {is_approved}")
print(f"Decline Reason: {decline_reason}")