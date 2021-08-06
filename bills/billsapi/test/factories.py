import datetime
import factory
import factory.fuzzy
from bills.users.test.factories import UserFactory

from ..models import Bills, BillsItems


class BillsFactory(factory.django.DjangoModelFactory):
    id = factory.Faker('uuid4')
    name = factory.fuzzy.FuzzyText()
    created_at = factory.LazyFunction(datetime.datetime.now)
    active = True
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Bills


class BillsItemsFactory(factory.django.DjangoModelFactory):
    id = factory.Faker('uuid4')
    item = factory.fuzzy.FuzzyText()
    price = factory.fuzzy.FuzzyInteger(0, 42)
    created_at = factory.LazyFunction(datetime.datetime.now)
    negative = False
    bill = factory.SubFactory(BillsFactory)
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = BillsItems
