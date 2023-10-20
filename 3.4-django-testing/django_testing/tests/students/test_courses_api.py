import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def courses_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_get_first_course(client, courses_factory):
    # Arrange
    first_course = courses_factory(_quantity=10)

    # Act
    for course in first_course:
        response = client.get(f'/courses/{course.id}/')
        data = response.json()

    # Assert
    assert response.status_code == 200
    assert data['name'] == course.name


@pytest.mark.django_db
def test_get_course_list(client, courses_factory):
    # Arrange
    courses = courses_factory(_quantity=5)

    # Act
    response = client.get('/courses/')
    data = response.json()

    # Assert
    assert response.status_code == 200
    assert len(data) == len(courses)
    for i, m in enumerate(data):
           assert m['id'] == courses[i].id


@pytest.mark.django_db
def test_filter_courses_id(client, courses_factory):
    # Arrange
    courses = courses_factory(_quantity=15)

    # Act
    for course in courses:
        response = client.get(f'/courses/?id={course.id}')
        data = response.json()[0]

    # Assert
    assert response.status_code == 200
    assert data['id'] == course.id


@pytest.mark.django_db
def test_filter_courses_name(client, courses_factory):
    # Arrange
    courses = courses_factory(_quantity=15)

    # Act
    for course in courses:
        response = client.get(f'/courses/?name={course.name}')
        data = response.json()[0]

    # Assert
    assert response.status_code == 200
    assert data['name'] == course.name


@pytest.mark.django_db
def test_create_course(client):

    User.objects.create_user('admin')
    count = Course.objects.count()

    response = client.post('/courses/', data={'name': 'math', 'students': []})

    assert response.status_code == 201
    assert Course.objects.count() == count + 1


@pytest.mark.django_db
def test_update_course(client, courses_factory):
    courses = courses_factory(_quantity=15)

    for course in courses:
        response = client.patch(f'/courses/{course.id}/', data={'name': 'math', 'students': []})
        data_response = response.json()
        updated_course = client.get(f'/courses/{course.id}/')
        data_update = updated_course.json()

    assert response.status_code == 200
    assert data_update == data_response


@pytest.mark.django_db
def test_delete_course(client, courses_factory):

    courses = courses_factory(_quantity=15)

    for course in courses:
        response = client.delete(f'/courses/{course.id}/')
        deleted_course = client.get(f'/courses/{course.id}/')

    assert response.status_code == 204
    assert deleted_course.status_code == 404




