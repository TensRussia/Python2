import pytest
from SubjectTable import SubjectTable
import os
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="module")
def db():
    return SubjectTable(os.getenv("DATABASE_URL"))


@pytest.fixture
def seeded_subject(db):
    db.create(name='TestSubject', subject_id=99)
    yield
    db.delete(99)
