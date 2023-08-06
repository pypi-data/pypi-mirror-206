from eulith_web3.eulith_web3 import EulithWeb3
from eulith_web3.signing import construct_signing_middleware, LocalSigner

AUTHORIZED_ADDRESS = '0x00a329c0648769A73afAc7F9381E08FB43dBEA72'

OWNER_KEYS = ['cf9ac1ec7666006d91173960ede131cc01f1a11eccdfa1ab593385da04878721', '2f2073f613ff2651f2114e26e8cca6e49a73b719dd728c6915eeb0c20534c32e', '1e780eaf6fed0ce7aca07418d97df74d5a004e394851b127b8c701b725e8400d']

if __name__ == '__main__':
    wallet = LocalSigner('4d5db4107d237df6a3d58ee5f70ae63d73d7658d4026f2eefd2f204c81682cb7')
    ew3 = EulithWeb3(eulith_url="http://localhost:7777/v0",
                     eulith_refresh_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NksifQ."
                                          "eyJzdWIiOiJsaWJ0ZXN0IiwiZXhwIjoxODQ0Njc"
                                          "0NDA3MzcwOTU1MTYxNSwic291cmNlX2hhc2giOiI"
                                          "qIiwic2NvcGUiOiJBUElSZWZyZXNoIn0.G87Tv9L"
                                          "wLH8SRgjlVKIAPk1pdavVS0xwz3fuB7lxP0Et-pP"
                                          "M7ojQkjC1zlC7zWYUdh9p3GvwX_ROfgSPJsw-Qhw",
                     signing_middle_ware=construct_signing_middleware(wallet))

    ew3.v0.deploy_new_armor(ew3.to_checksum_address(AUTHORIZED_ADDRESS), {
        'from': wallet.address,
        'gas': 3000000
    })

    owner_addresses = []
    for o in OWNER_KEYS:
        o_wal = LocalSigner(o)
        owner_addresses.append(o_wal.address)
        status = ew3.v0.submit_enable_module_signature(AUTHORIZED_ADDRESS, o_wal)

    status = ew3.v0.enable_armor(2, owner_addresses, {
        'gas': 5000000,
        'from': wallet.address
    })

    print(status)


