import random
from .models import *

from faker import Faker # type: ignore
fake = Faker()

def seed_db(n=10)->None:
    try:
        for i in range(0,n):
            
            departments_obj = Department.objects.all()
            random_index = random.randint(0,len(departments_obj)-1)
            department = departments_obj[random_index]
            
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(18,30)
            student_addr = fake.address()
            
            student_id = f'STU-0{random.randint(100,999)}'
            student_id_obj = StudentID.objects.create(student_id = student_id)
            
            student_obj = Student.objects.create(
                department = department,
                student_id = student_id_obj,
                student_name = student_name,
                student_email = student_email,
                student_age = student_age,
                student_addr = student_addr,
            )
    except Exception as e:
        print(e)


def create_subject_marks():
    try:
        student_obj = Student.objects.all()
        for student in student_obj:
            subject_obj = Subjects.objects.all()
            for subject in subject_obj:
                SubjectMarks.objects.create(
                    student = student,
                    subject = subject,
                    marks = random.randint(0,100)
                )
    except Exception as e:
        print(e)

from django.db.models import Sum

def generate_report_card():
    
    current_rank = -1
    ranks = Student.objects.annotate(marks = Sum('studentmarks__marks')).order_by('-marks' , '-student_age')

    i = 1
    for rank in ranks:
        ReportCard.objects.create(
            student = rank ,
            student_rank = i
        )
        i = i + 1