import pytest

import source.school as school


def test_add_students(student_factory, course_factory):
    student = student_factory(1, "Jean")
    maths = course_factory(101, "maths")
    maths.add_student(student)
    assert student in maths.students

def test_add_course(course_factory, student_factory):
    course = course_factory(101, "maths")
    student = student_factory(1, "Jean")
    course.add_student(student)
    assert course.student_count() == 1