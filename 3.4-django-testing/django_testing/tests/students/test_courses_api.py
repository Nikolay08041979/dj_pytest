from model_bakery import baker
import pytest
from rest_framework.test import APIClient

from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.fixture
def course_factory(student_factory):
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_get_first_course(client, course_factory):
    # Arrange
    courses = course_factory(_quantity=1, _name="Math")
    # Act
    response = client.get("/api/v1/courses/")
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)
    assert data[0]["name"] == "Math"


@pytest.mark.django_db
def test_get_courses(client, course_factory):
    # Arrange
    courses = course_factory(_quantity=10)
    # Act
    response = client.get("/api/v1/courses/")
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)
    for i, course in enumerate(courses):
        assert data[i]["name"] == course.name


@pytest.mark.django_db
def test_filter_courses_by_id(client, course_factory):
    # Arrange
    courses = course_factory(_quantity=10)
    # Act
    response = client.get("/api/v1/courses/?id=1")
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)
    assert data[0]["name"] == "Math"


@pytest.mark.django_db
def test_filter_courses_by_name(client, course_factory):
    courses = course_factory(_quantity=10)
    response = client.get("/api/v1/courses/?name=math")
    assert response.status_code == 200
    data = response.json()
    for i, name in enumerate(data):
        if name["name"] == getattr(courses[i], "name"):
            assert name["name"] == "Math"

    assert len(data) == len(courses)
    assert data[0]["name"] == "Math"


@pytest.mark.django_db
def test_create_course(client, course):
    count = Course.objects.count()
    response = client.post("/api/v1/courses/", {"name": course.id})
    assert response.status_code == 201
    data = response.json()
    assert Course.objects.count() == count + 1


@pytest.mark.django_db
def test_update_course(client):
    # Arrange
    course = Course.objects.create(name="Chemistry")
    # Act
    response = client.patch(f"/api/v1/courses/{course.id}/", {"name": "Physics"})
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Physics"


@pytest.mark.django_db
def test_delete_course(client):
    # Arrange
    course = Course.objects.create(name="Chemistry")
    # Act
    response = client.delete(f"/api/v1/courses/{course.id}/")
    # Assert
    assert response.status_code == 204
