import json
import unittest

from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase, APIRequestFactory

from api.views import MultiplyView

factory = APIRequestFactory()


class FailTestException(Exception):
    def __init__(self, args):
        super().__init__(*args)


class TestResolver:

    @staticmethod
    def sync_resolve_named_args(method=None, args_dict=None):
        try:
            return method(**args_dict)
        except Exception as e:
            return False

    @staticmethod
    def sync_resolve_args(method=None, args_list=None):
        try:
            return method(*args_list)
        except Exception as e:
            return False


class MultiplyTestCase(APITestCase):

    def test_multiply(self):
        request = factory.get(reverse("multiply-view"))
        response = MultiplyView().as_view()(request)
        result = response.data
        self.assertEquals(float(result["result"]), float("4")*float("6"), msg="Test multiply view")
