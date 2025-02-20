import pytest
from script.deploy import deploy_coffee
from script.deploy_mocks import deploy_feed
from moccasin.config import get_active_network

@pytest.fixture
def account():
    return get_active_network()

@pytest.fixture(scope="session")
def eth_usd():
    return deploy_feed()

@pytest.fixture(scope="function")
def coffee(eth_usd):
    return deploy_coffee(eth_usd)