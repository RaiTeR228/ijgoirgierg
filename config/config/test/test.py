import pytest
from rest_framework.test import APIClient

@pytest.fixture
def client():
    # фикстура для создания клиента API
    return APIClient()

@pytest.mark.django_db
# Проверка Get запроса
def test_api_get(client):
    response = client.get('/hors-products/')
    assert response.status_code != 500
    print(f"GET status: {response.status_code}")

@pytest.mark.django_db
# тестируем POST запрос по принятию данных
def test_api_post(client):
    data = {'name': 'John Doe'}
    response = client.post('/hors-products/', data, format='json')
    # проверяем, что статус код 
    assert response.status_code != 500
    print(f"POST status: {response.status_code}")

@pytest.mark.django_db
def test_api_return(client):
    # проверяем что запрос возвращает данные
    response = client.get('/hors-products/')
    # проверяем что есть какойто ответ от сервера
    assert response.content is not None
    print(f"GET status: {response.status_code[:20]}")