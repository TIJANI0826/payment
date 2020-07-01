from paystack.resource import TransactionResource

import random
import string

def main():
    rand = ''.join(
        [random.choice(
            string.ascii_letters + string.digits) for n in range(16)])
    secret_key = 'sk_test_6ca6fa242c3af8287dc6b024710ad8ca4f6a4ae8'
    random_ref = rand
    test_email = 'ibrahimtijani08@gmail.com'
    test_amount = '1000'
    plan = 'Basic'
    client = TransactionResource(secret_key, random_ref)
    response = client.initialize(test_amount,
                                 test_email,
                                 )
    print(response)
    client.authorize() # Will open a browser window for client to enter card details
    verify = client.verify() # Verify client credentials
    print(verify)
    print(client.charge()) # Charge an already exsiting client
    
main()
