#!/usr/bin/python
# -*- coding: utf-8 -*-

student2score = {
    "Darius": 100,
    "Dr. Mundo": 80,
    "Morgana": 60,
    "Sivir": 75,
    "Yummi": 20,
    "Viktor": 97
}


def get_special_students(student2score):
    """
    특별반 학생의 리스트를 리턴하는 함수
    특별반은 점수가 80점 이상이어야 들어갈 수 있다.

    :param student2score:
    :return special_students:
    """
    special_students = []
    for student in student2score:
        if student2score[student] >= 80:
            special_students.append(student)
    return special_students


print(get_special_students(student2score))
