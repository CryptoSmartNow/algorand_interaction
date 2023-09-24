# Interacting with an algorand contract using the beaker package

## Structure of an algorand contract
An algorand contract written with beaker makes interaction easy and straight 
forward. The contract is written and compiled with beaker. Then the ABI is
generated. 

There are two main ways of interacting with a deployed algorand contract.
1. Through a transaction which includes a payment.
2. Through an application call method.
3. A combination of both payment and application transaction.

Note: Txn fees are payed for both.

## Interaction flow
To interact with a contract using beaker, an application client has to be created. To create one, the following are required
1. Algod client: This is a client which can interact with the algorand's blockchain. It's an instance of AlgodClient sdk. The api key, headers can be gotten from several providers.
2. ABI: This is the contract's ABI which will be included in the contract's resources.
3. signer: This is an account's signer. It's responsible for signing transactions. This will be used to interact with the contract. It's constructed from an algorand wallet.

```py
from config import account, client, ABI # not provided here
from beaker.client import ApplicationClient

appl_client = ApplicationClient(
    client=client,
    app=ABI,
    signer=account.signer
)
```

After an application client has been created, the contract can be interacted with. Say we are interacting with a contract and want to call it's method for
creating a new user. If the contract's definition is like this
```py
@bitsave_app.external
def create_user(
    user_name: abi.String, 
    user_age: abi.Uint64,
    *,
    output: abi.Uint8
):
    # implementation
```

This means the contract expects user_name and user_age arguments. The method
can be called with the following structure. The output parameter indicates the 
type of response the contract returns. Mostly an opcode from the agreement between the developers, in this case a uint8


```py
app_id = 39 # The id of the contract; gotten from contract's deployment

appl_client.call(
    "create_user", # the contract method to call
    user_name="a user",
    user_age=16,
    foreign_boxes=[] # boxes the contract might interact with
    foreign_apps=[app_id]
    # other fields
)
```

