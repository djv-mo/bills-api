from django.urls import reverse, resolve
from .factories import BillsFactory, BillsItemsFactory

# setup our test factories
bill = BillsFactory()
billitem = BillsItemsFactory()

def test_bill_list_reverse():
    assert reverse('bills:bills-list') == '/bills/'

def test_bill_list_resolve():
    assert resolve('/bills/').view_name == 'bills:bills-list'

def test_bill_detail_reverse():
    url = reverse('bills:bills-detail', kwargs={'pk': bill.id})
    assert url == f'/bills/{bill.id}/'

def test_bill_detail_resolve():
    url = f'/bills/{bill.id}/'
    assert resolve(url).view_name == 'bills:bills-detail'

def test_bill_items_list_reverse():
    url = reverse('bills:items-list', kwargs={'pk': bill.id})
    assert url == f'/bills/{bill.id}/items/'

def test_bill_items_list_resolve():
    url = f'/bills/{bill.id}/items/'
    assert resolve(url).view_name == 'bills:items-list'

def test_item_update_reverse():
    url = reverse('bills:items-update', kwargs={'pk': billitem.id})
    assert url == f'/items/{billitem.id}/'

def test_item_update_resolve():
    url = f'/items/{billitem.id}/'
    assert resolve(url).view_name == 'bills:items-update'
