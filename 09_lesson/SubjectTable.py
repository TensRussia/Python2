from sqlalchemy import create_engine, text


class SubjectTable:
    __scripts = {
        "select by subject_id": text(
            "SELECT * FROM subject WHERE subject_id = :select_id"
            ),
        "select": text("SELECT * FROM subject"),
        "delete_by_subject_id": text(
            "DELETE FROM subject WHERE subject_id = :id_to_delete"
            ),
        "insert_new": text(
            "INSERT INTO subject (subject_id, subject_title)"
            "VALUES (:id, :name)"
            ),
        "update": text(
            "UPDATE subject SET subject_title = :name WHERE subject_id = :id"
            ),
        "get_m_id": text("SELECT MAX(subject_id) FROM subject"),
    }

    def __init__(self, db_connection_string):
        self.__db = create_engine(db_connection_string)

    def get_subject_by_id(self, s_id):
        connection = self.__db.connect()
        rows = connection.execute(self.__scripts["select by subject_id"],
                                  {"select_id": s_id}).fetchall()
        connection.close()
        return rows

    def get_subjects(self):
        connection = self.__db.connect()
        rows = connection.execute(self.__scripts["select"]).fetchall()
        connection.close()
        return rows

    def delete(self, subject_id):
        connection = self.__db.connect()
        connection.execute(self.__scripts["delete_by_subject_id"],
                           {"id_to_delete": subject_id})
        connection.commit()
        connection.close()

    def create(self, name, subject_id):
        connection = self.__db.connect()
        connection.execute(self.__scripts["insert_new"],
                           {"id": subject_id, "name": name})
        connection.commit()
        connection.close()

    def update(self, name, subject_id):
        connection = self.__db.connect()
        connection.execute(self.__scripts["update"],
                           {"id": subject_id, "name": name})
        connection.commit()
        connection.close()

    def get_max_id(self):
        connection = self.__db.connect()
        m_id = connection.execute(self.__scripts["get_m_id"]).fetchall()[0][0]
        connection.close()
        return m_id
