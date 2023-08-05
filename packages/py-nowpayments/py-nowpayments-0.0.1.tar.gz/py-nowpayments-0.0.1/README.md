A simple Python library for interacting with NowPayments API, with methods for authentication, getting currency info, and creating payments/invoices.
First you need an api-key from [nowpayments](https://nowpayments.io/). 

Register and verify your account, then generate an API key on the NowPayments dashboard for API authentication.

To use this Library follow the next example:

from py-nowpayments import Nowpayments
nowpayments = Nowpayments('your-api-key')

To create a payment use:

nowpayments.create_payment(399, 'USD', 'BTC')

to check payment status use:

nowpayments.get_payment_status(payment_id).