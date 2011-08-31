#!/usr/bin/python
import sqlite3

class AttendDB():

    def __init__(self):
        """Interaction with the sqlite database."""
        self.db_name = 'Attendance.db'
        self.class_table = 'academy'

    def open_connection(self):
        """Create a connection and a cursor to the given database."""
        self.conn = sqlite3.connect(self.db_name)
        self.c = self.conn.cursor()

    def add_student(self, apelido="", fn="", ln=""):
        """Add new student to table."""
        self.open_connection()
        self.c.execute("INSERT INTO students (apelido, fn, ln) " + \
                       "VALUES ('" + str(apelido) + "', '" + str(fn) + \
                       "', '" + str(ln) +"')")
        self.conn.commit()
        self.close_connection()

    def remove_student(self, apelido="", fn="", ln=""):
        """Remove student from table."""
        self.open_connection()
        self.c.execute(\
            "DELETE FROM students WHERE apelido=? AND fn=? AND ln=?",\
            (apelido, fn, ln))
        self.conn.commit()
        self.close_connection()

    def get_attendance_for_date(self, curr_date):
        """Get the students that attended class on a given date from today."""
        self.open_connection()
        students = []
        self.c.execute("SELECT students.* FROM academy JOIN students " +\
                "ON academy.Sid=students.Sid " + \
                "WHERE academy.classDate='"+str(curr_date)+"'")
        for row in self.c:
            students.append(row)

        self.close_connection()
        return students

    def get_students(self):
        """Get all of the students."""
        self.open_connection()
        students = []
        self.c.execute("SELECT * FROM students")
        for row in self.c:
            students.append(row)

        self.close_connection()
        return students

    def student_attend(self, sid, curr_date):
        """Add students attendance to table."""
        self.open_connection()
        self.c.execute("INSERT INTO academy (Sid, classDate) VALUES (" + \
                        str(sid)+", '"+str(curr_date)+"')")
        self.conn.commit()
        self.close_connection()

    def student_deattend(self, sid, curr_date):
        """Rmove student attendance from table."""
        self.open_connection()
        self.c.execute("DELETE FROM academy WHERE Sid='" + str(sid) + "' " + \
                       "AND classDate='" + str(curr_date) + "'")
        self.conn.commit()
        self.close_connection()

    def close_connection(self):
        """Close the connection."""
        self.c.close()
        self.conn.close()

if __name__ == '__main__':
    # TODO - Testing
    pass
