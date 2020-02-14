from django.test import TestCase

# Create your tests here.
import pytest
from django.db import models
import products as prd
import datetime


@pytest.fixture
def product_title():
    prd.title = 'test'
    return prd


@pytest.fixture
def product_pub_date():
    prd.pub_date = datetime.datetime.now()
    return prd


@pytest.fixture
def product_body():
    prd.body = 'This is body'
    return prd


@pytest.fixture
def product_url():
    prd.url = 'http://www.google.com'
    return prd


def test_title(product_title):
    # print(type(input_value))
    assert type(product_title.title) == str


def test_date(product_pub_date):
    assert type(product_pub_date.pub_date) == datetime.datetime


def test_body(product_body):
    assert type(product_body.body) == str


def test_url(product_url):
    assert type(product_url.url) == str
