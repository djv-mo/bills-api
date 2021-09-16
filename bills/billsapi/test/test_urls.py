from django.urls import reverse, resolve
from .factories import BillsFactory, BillsItemsFactory

# setup our test factories
bill = BillsFactory()
billitem = BillsItemsFactory()


def test_bill_list_reverse():
    assert reverse('bills:bills-list') == '/endpoint/bills/'


def test_bill_list_resolve():
    assert resolve('/endpoint/bills/').view_name == 'bills:bills-list'


def test_bill_detail_reverse():
    url = reverse('bills:bills-detail', kwargs={'pk': bill.id})
    assert url == f'/endpoint/bills/{bill.id}/'


def test_bill_detail_resolve():
    url = f'/endpoint/bills/{bill.id}/'
    assert resolve(url).view_name == 'bills:bills-detail'


def test_bill_items_list_reverse():
    url = reverse('bills:items-list', kwargs={'pk': bill.id})
    assert url == f'/endpoint/bills/{bill.id}/items/'


def test_bill_items_list_resolve():
    url = f'/endpoint/bills/{bill.id}/items/'
    assert resolve(url).view_name == 'bills:items-list'


def test_item_update_reverse():
    url = reverse('bills:items-update', kwargs={'pk': billitem.id})
    assert url == f'/endpoint/items/{billitem.id}/'


def test_item_update_resolve():
    url = f'/endpoint/items/{billitem.id}/'
    assert resolve(url).view_name == 'bills:items-update'


def test_export_bill_reverse():
    url = reverse('bills:items-csv', kwargs={'pk': bill.id})
    assert url == f'/endpoint/bills/{bill.id}/export/'


def test_export_bill_resolve():
    url = f'/endpoint/bills/{bill.id}/export/'
    assert resolve(url).view_name == 'bills:items-csv'


def test_archive_bill_reverse():
    url = reverse('bills:archived-bills')
    assert url == f'/endpoint/archived/'


def test_archive_bill_resolve():
    url = f'/endpoint/archived/'
    assert resolve(url).view_name == 'bills:archived-bills'


def test_archive_unarchive_bill_reverse():
    url = reverse('bills:archive-unarchieve', kwargs={'pk': bill.id})
    assert url == f'/endpoint/bills/{bill.id}/archive/'


def test_archive_unarchive_bill_resolve():
    url = f'/endpoint/bills/{bill.id}/archive/'
    assert resolve(url).view_name == 'bills:archive-unarchieve'
