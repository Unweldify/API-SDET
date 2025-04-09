import pytest

from Api.Entity_service.entity_request import EntityService
from Entity.entity_model import Entity
from Data.data_generator import Generator

@pytest.fixture
def entity_api() -> EntityService:
    return EntityService

@pytest.fixture()
def generated_entity() -> Entity:
    return Entity(**Generator.generate_client_data())
