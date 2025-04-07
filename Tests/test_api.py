import allure
from random import choice


@allure.title('Проверить функциональность добавления сущности.')
def test_create_entity(entity_api, generated_entity):
    id = int(entity_api.create_entity(generated_entity))

    in_list = entity_api.get_entity(id)

    with allure.step('Смотрим если сущность есть в списке.'):
        assert in_list, (
            'Сущность не была создана.'
        )


@allure.title('Проверить функциональность удаления сущности.')
def test_delete_entity(entity_api, generated_entity):
    id = int(entity_api.create_entity(generated_entity))

    entity_api.delete_entity(id)

    in_list = entity_api.get_entity(id)
    with allure.step('Смотрим если сущность удалилась.'):
        assert not in_list, (
            'Сущность не удалилась.'
        )


@allure.title('Проверить функциональность получения сущности.')
def test_get_entity(entity_api, generated_entity):

    id = entity_api.create_entity(generated_entity)

    in_list = entity_api.get_entity(id)

    with allure.step('Посмотрим если существо было получено'):
        assert in_list, (
            'Сущность не была получена.'
        )


@allure.title('Проверить функциональность получения списка сущностей.')
def test_get_entities(entity_api):
    entities = entity_api.get_all_entities()

    with allure.step('Посмотрим если был получен список сущностей.'):
        assert entities != [], (
            'Список сущностей не был получен.'
        )


@allure.title('Проверить функциональность изменения сущности.')
def test_patch_entity(entity_api, generated_entity):
    id = choice(entity_api.get_all_entities()).id
    old_entity = entity_api.get_entity(id)

    entity_api.patch_entity(id, generated_entity)

    new_entity = entity_api.get_entity(id)

    with allure.step('Смотрим если существо изменилось.'):
        assert new_entity.model_dump_json() != old_entity.model_dump_json(), (
            'Существо не изменено.'
        )
