from django.test import TestCase
from django.forms.models import model_to_dict
from nose.tools import eq_, ok_
from .factories import BillsFactory, BillsItemsFactory
from ..serializers import BillsSerializer, BillsItemsSerializer


class TestCreateUserSerializer(TestCase):

    def setUp(self):
        self.bill = model_to_dict(BillsFactory.build())
        self.billitem = model_to_dict(BillsItemsFactory.build())

    def test_bill_serializer_with_empty_data(self):
        serializer = BillsSerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_bill_serializer_with_valid_data(self):
        serializer = BillsSerializer(data=self.bill)
        ok_(serializer.is_valid())

    def test_bill_item_serializer_with_empty_data(self):
        serializer = BillsItemsSerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_bill_item_serializer_with_valid_data(self):
        serializer = BillsItemsSerializer(data=self.billitem)
        ok_(serializer.is_valid())
