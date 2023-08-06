import os

import pytest

DATA_DIR_NAME = "data"
SMALL_SKY_DIR_NAME = "small_sky"
SMALL_SKY_ORDER1_DIR_NAME = "small_sky_order1"
SMALL_SKY_TO_SMALL_SKY_ORDER1_DIR_NAME = "small_sky_to_small_sky_order1"
TEST_DIR = os.path.dirname(__file__)

# pylint: disable=missing-function-docstring, redefined-outer-name


@pytest.fixture
def test_data_dir():
    return os.path.join(TEST_DIR, DATA_DIR_NAME)


@pytest.fixture
def small_sky_dir(test_data_dir):
    return os.path.join(test_data_dir, SMALL_SKY_DIR_NAME)


@pytest.fixture
def small_sky_order1_dir(test_data_dir):
    return os.path.join(test_data_dir, SMALL_SKY_ORDER1_DIR_NAME)


@pytest.fixture
def small_sky_to_small_sky_order1_dir(test_data_dir):
    return os.path.join(test_data_dir, SMALL_SKY_TO_SMALL_SKY_ORDER1_DIR_NAME)
