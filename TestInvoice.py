import pytest


@pytest.fixture()
def products():
    products = {'pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}
    return products

def test_CanFindInvoiceClass():
    invoice = Invoice()