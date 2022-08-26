from doctest import ELLIPSIS_MARKER
from imp import load_source
from ntpath import realpath
from queue import Empty
from threading import local
from unittest import mock
from brownie import FundMe, config, network, MockV3Aggregator
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.helpful_scripts import deploy_mocks
from web3 import Web3


def deploy_fund_me():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    account = get_account()
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get(
            "verify"
        ),  # No sé porque esta , es importante pero la debe de llevar
    )
    # fund_me = FundMe.deploy({"from": account}, publish_source=False)
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()


# Ganache allows us to run a local version of the etherum blockchain.
# We have got a simulated ethereum chain running in our computer.
# A tool kit, basically a framework that allows you to deploy, control,
# and test smart contracts a lot more easy

# FundMe
# []
# That list contains the contract addresses of all of the deployments of this contract
# since we have not deployed yet even once that list is Empty

# brownie networks add live ganache-gui host=http://127.0.0.1:7545 chainid=1337


# brownie pm install OpenZepelin/openzepelin-contracts@4 (doble p)

# then in config you have to add...
# remappings:
#     - "@openzeppelin=OpenZeppelin/openzeppelin-contracts@"


# Fork es interactual con contratos que ya estan desplegados en una mainet o testnet
# para probarlos en nuestro entorno local
# Fork hace una copia de las blockchains que ya existen para poder interactuar con ella
# Asi lograriamos tener una mainet local la cual nos va a permitir interactuar con los
# contratos, con el pricefeed, con un AAVE contract como si estuvieramos en una red real
# mente la blockchain real va a quedar inmutable,
# Brownie ya viene con esta integracion de esta mainet fork que tambien se conecta y trabaja
# con infura
# Entonces lo que nosotros vamos hacer aqui es interactuar con esa mainet fork

# No se para que es esto, pero parte de esto lo obtuve de alchemy.com
# brownie networks add development mainnet-fork-dev cmd=ganache host=http://127.0.0.1 fork=https://eth-mainnet.g.alchemy.com/v2/kZWoInEErwBq7qkfj2ivNyTgtEPf4BGi accounts=10 mnemonic=brownie port=8545
# A new network 'mainnet-fork-dev' has been added
