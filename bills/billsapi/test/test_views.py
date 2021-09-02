import json

from django.urls import reverse

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from bills.users.test.factories import UserFactory
from .factories import BillsFactory, BillsItemsFactory

from ..serializers import BillsSerializer, BillsItemsSerializer
from ..models import Bills, BillsItems


class RegistrationTest(APITestCase):
    def test_registration(self):
        data = {'username': 'newidea',
                'email': 'sadsa@gmail.com',
                'password': 'G@dfssd3',
                'password_confirm': 'G@dfssd3'}
        response = self.client.post('/accounts/register/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class BillsViewTest(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.token = self.user.auth_token
        self.api_autherization()

    def api_autherization(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_bills_list_authenticated(self):
        response = self.client.get(reverse('bills:bills-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_bills_list_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(reverse('bills:bills-list'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_bills_list_with_current_user(self):
        bill = BillsFactory(user=self.user)
        response = self.client.get(reverse('bills:bills-list'))
        self.assertEqual(response.data['results'][0]['name'], bill.name)

    def test_bills_list_with_another_user(self):
        bill = BillsFactory(user=self.user)
        user2 = UserFactory()
        self.client.force_authenticate(user=user2)
        response = self.client.get(reverse('bills:bills-list'))
        self.assertEqual(response.data['results'], [])

    def test_create_bills(self):
        data = {'name': 'new bill test'}
        response = self.client.post(reverse('bills:bills-list'), data)
        self.assertEqual(response.data['name'], 'new bill test')

    def test_update_bill(self):
        bill = BillsFactory(user=self.user)
        response = self.client.put(reverse('bills:bills-detail', kwargs={'pk': bill.id}),
                                   {'name': 'modified'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'modified')

    def test_delete_bill(self):
        bill = BillsFactory(user=self.user)
        response = self.client.delete(
            reverse('bills:bills-detail', kwargs={'pk': bill.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_bills_detail_with_another_user(self):
        bill = BillsFactory(user=self.user)
        user2 = UserFactory()
        self.client.force_authenticate(user=user2)
        response = self.client.get(
            reverse('bills:bills-detail', kwargs={'pk': bill.id}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_bills_items_list_current_user(self):
        bill = BillsFactory(user=self.user)
        billitem = BillsItemsFactory(bill=bill)
        response = self.client.get(
            reverse('bills:items-list', kwargs={'pk': bill.id}))
        self.assertEqual(response.data['results'][0]['item'], billitem.item)

    def test_bills_items_list_another_user(self):
        bill = BillsFactory(user=self.user)
        billitem = BillsItemsFactory(bill=bill)
        user2 = UserFactory()
        self.client.force_authenticate(user=user2)
        response = self.client.get(
            reverse('bills:items-list', kwargs={'pk': bill.id}))
        self.assertEqual(response.data['results'], [])

    def test_create_billitem_positive(self):
        bill = BillsFactory(user=self.user)
        data = {'item': 'new bill item test', 'price': 2}
        response = self.client.post(
            reverse('bills:items-list', kwargs={'pk': bill.id}), data)
        self.assertEqual(response.data['item'], 'new bill item test')
        self.assertEqual(response.data['negative'],  False)

    def test_create_billitem_negative(self):
        bill = BillsFactory(user=self.user)
        data = {'item': 'new bill item test', 'price': -2}
        response = self.client.post(
            reverse('bills:items-list', kwargs={'pk': bill.id}), data)
        self.assertEqual(response.data['item'], 'new bill item test')
        self.assertEqual(response.data['negative'],  True)

    def test_create_billitem_with_another_user(self):
        bill = BillsFactory(user=self.user)
        data = {'item': 'new bill item test', 'price': 2}
        user2 = UserFactory()
        self.client.force_authenticate(user=user2)
        response = self.client.post(
            reverse('bills:items-list', kwargs={'pk': bill.id}), data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_bills_items_detail_current_user(self):
        billitem = BillsItemsFactory(user=self.user)
        response = self.client.get(
            reverse('bills:items-update', kwargs={'pk': billitem.id}))
        self.assertEqual(response.data['item'], billitem.item)

    def test_bills_items_detail_with_another_user(self):
        billitem = BillsItemsFactory(user=self.user)
        user2 = UserFactory()
        self.client.force_authenticate(user=user2)
        response = self.client.get(
            reverse('bills:items-update', kwargs={'pk': billitem.id}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_bill_item_with_positive(self):
        billitem = BillsItemsFactory(user=self.user)
        response = self.client.put(reverse('bills:items-update', kwargs={'pk': billitem.id}),
                                   {'item': 'modified', 'price': 2})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['item'], 'modified')
        self.assertEqual(response.data['price'], 2)
        self.assertEqual(response.data['negative'], False)

    def test_update_bill_item_with_negative(self):
        billitem = BillsItemsFactory(user=self.user)
        response = self.client.put(reverse('bills:items-update', kwargs={'pk': billitem.id}),
                                   {'item': 'modified', 'price': -2})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['item'], 'modified')
        self.assertEqual(response.data['price'], -2)
        self.assertEqual(response.data['negative'], True)

    def test_delete_bill_item(self):
        billitem = BillsItemsFactory(user=self.user)
        response = self.client.delete(
            reverse('bills:items-update', kwargs={'pk': billitem.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_export_bill_with_another_user(self):
        bill = BillsFactory(user=self.user)
        data = {'item': 'new bill item test', 'price': 2}
        user2 = UserFactory()
        self.client.force_authenticate(user=user2)
        response = self.client.get(
            reverse('bills:items-csv', kwargs={'pk': bill.id}), data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_export_bill_with_same_user(self):
        bill = BillsFactory(user=self.user)
        data = {'item': 'new bill item test', 'price': 2}
        response = self.client.get(
            reverse('bills:items-csv', kwargs={'pk': bill.id}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_archieved_list_with_current_user(self):
        bill = BillsFactory(user=self.user, active=False)
        response = self.client.get(reverse('bills:archived-bills'))
        self.assertEqual(response.data['results'][0]['name'], bill.name)

    def test_archieved_list_with_another_user(self):
        bill = BillsFactory(user=self.user, active=False)
        user2 = UserFactory()
        self.client.force_authenticate(user=user2)
        response = self.client.get(reverse('bills:archived-bills'))
        self.assertEqual(response.data['results'], [])

    def test_archive_bill_with_current_user(self):
        bill = BillsFactory(user=self.user)
        response = self.client.post(
            reverse('bills:archive-unarchieve', kwargs={'pk': bill.id}))
        self.assertEqual(response.data['active'],  False)

    def test_unarchive_bill_with_current_user(self):
        bill = BillsFactory(user=self.user)
        response = self.client.put(
            reverse('bills:archive-unarchieve', kwargs={'pk': bill.id}))
        self.assertEqual(response.data['active'],  True)

    def test_archive_bill_with_another_user(self):
        bill = BillsFactory(user=self.user)
        user2 = UserFactory()
        self.client.force_authenticate(user=user2)
        response = self.client.post(
            reverse('bills:archive-unarchieve', kwargs={'pk': bill.id}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_unarchive_bill_with_another_user(self):
        bill = BillsFactory(user=self.user)
        user2 = UserFactory()
        self.client.force_authenticate(user=user2)
        response = self.client.put(
            reverse('bills:archive-unarchieve', kwargs={'pk': bill.id}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
