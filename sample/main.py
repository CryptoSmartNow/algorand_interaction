from sample.utils import (
    getAlgodClient, 
    getFundedAccount, 
    contract_app, 
    app_id
)
from beaker.client import ApplicationClient


client = getAlgodClient()

acct = getFundedAccount(client=client)

appl_client = ApplicationClient(
    client=client, 
    app=contract_app, 
    signer=acct.signer
)

appl_client.call(
    "create_user", # the contract method to call
    user_name="a user",
    user_age=16,
    foreign_boxes=[], # boxes the contract might interact with
    foreign_apps=[app_id]
    # other fields
)


