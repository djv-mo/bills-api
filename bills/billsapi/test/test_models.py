from .factories import BillsFactory, BillsItemsFactory

def test_Bills___str___():
    bill = BillsFactory()
    assert bill.__str__() == bill.name + " by " + str(bill.user)
    assert str(bill) == bill.name + " by " + str(bill.user)


def test_BillsItems___str___():
    itemsfactory = BillsItemsFactory()
    assert itemsfactory.__str__() == itemsfactory.item + " - " + str(itemsfactory.bill)
    assert str(itemsfactory) == itemsfactory.item + " - " + str(itemsfactory.bill)
