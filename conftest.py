import pytest

from Services.Entity.entity_request import EntityRequest
from Entity.entity_model import Entity
from Services.Entity.data_generator import Generator

@pytest.fixture
def entity_api() -> EntityRequest:
    return EntityRequest

@pytest.fixture()
def generated_entity() -> Entity:
    return Entity(**Generator.generate_client_data())
