from dotenv import load_dotenv
from SubjectTable import SubjectTable
import os


load_dotenv()


db_connection_string = os.getenv("DATABASE_URL")
db = SubjectTable(db_connection_string)


def test_get_subjects():
    db_result = db.get_subjects()
    assert len(db_result) > 0


def test_insert():
    db.create(name='Technologija', subject_id=17)
    result = db.get_subject_by_id(17)
    assert len(result) > 0
    db.delete(17)


def test_update():
    db.create(name='Technologija', subject_id=17)
    db.update(name='SuperTechnologija', subject_id=17)
    result = db.get_subject_by_id(17)
    assert result[0][1] == 'SuperTechnologija'
    db.delete(17)


def test_delete():
    db.create(name='Technologija', subject_id=17)
    result = db.get_subject_by_id(17)
    assert len(result) > 0
    db.delete(17)
    result_after = db.get_subject_by_id(17)
    assert len(result) > len(result_after)
