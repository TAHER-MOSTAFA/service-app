from unicodedata import category
from service.machines.models import Company, Machine, Category
from factory import Faker
from factory.django import DjangoModelFactory
import factory
import factory.fuzzy

class CompanyFactory(DjangoModelFactory):
    name = Faker("company")
    address = Faker("address")
    website = Faker("url")
    image = factory.django.ImageField(color='blue')
    description = Faker("paragraph", nb_sentences=5)
    
    class Meta:
        model = Company
        django_get_or_create = ["name"]
CAT_LIST = ["راوتر" , "ليزر", "قواطع"]

class CategoryFactory(DjangoModelFactory):
    name = factory.fuzzy.FuzzyChoice(CAT_LIST)
    
    class Meta:
        model = Category
        django_get_or_create = ["name"]
        
class MachineFactory(DjangoModelFactory):
    name = Faker("sentence", nb_words=1)
    company = factory.SubFactory(CompanyFactory)
    category = factory.SubFactory(CategoryFactory)
    image = factory.django.ImageField(color='blue')
    description = Faker("paragraph", nb_sentences=5)
    
    class Meta:
        model = Machine
        django_get_or_create = ["name"]