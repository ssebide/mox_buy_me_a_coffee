from moccasin.config import get_active_network
from src import buy_me_a_coffee
from script.deploy_mocks import deploy_feed
from moccasin.boa_tools import VyperContract

# def deploy_coffee(price_feed: str):
#     buy_me_a_coffee(price_feed)

def moccasin_main():
    active_network = get_active_network()
    
    price_feed: VyperContract = active_network.manifest_named("price_feed")
    printf("On network {active_network.name}, using price feed at {price_feed.address}")
    # price_feed: VyperContract = deploy_feed()
    # coffee = buy_me_a_coffee.deploy(price_feed.address)
    # print("Coffee deployed at ", coffee.address)
    