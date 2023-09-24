@contract_app.external
def create_user(
    user_name: abi.String, 
    user_age: abi.Uint64,
    *,
    output: abi.Uint8
):
    return Seq(
        # implementations
        output.set(Int(1)),
    )
