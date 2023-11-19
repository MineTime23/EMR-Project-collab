from django.db import models
from django.contrib.auth.models import AbstractUser


# Patient 모델 정의
class Patient(models.Model):
    id = models.AutoField(primary_key=True)  # id 필드를 다시 추가
    last_name = models.CharField(max_length=50, null=False)
    first_name = models.CharField(max_length=50, null=False)
    birth_date = models.DateField(null=False)
    address = models.CharField(max_length=255, null=False)
    GENDER_CHOICES = [
        ('M', '남성'),
        ('F', '여성'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=False)
    phone_num = models.CharField(max_length=15, null=False)
    email = models.CharField(max_length=100, null=True)
    image = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.first_name


# User 모델 정의
class User(models.Model):
    id = models.AutoField(primary_key=True)  # id 필드를 다시 추가
    user_id = models.CharField(max_length=15, null=False)
    user_pw = models.CharField(max_length=100, null=False)
    name = models.CharField(max_length=50, null=False)
    birth_date = models.DateField(null=False)
    address = models.CharField(max_length=255, null=False)
    GENDER_CHOICES = [
        ('M', '남성'),
        ('F', '여성'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=False)
    phone_num = models.CharField(max_length=15, null=False)
    email = models.CharField(max_length=100, null=True)
    department = models.CharField(max_length=50, null=True)
    position = models.CharField(max_length=50, null=True)
    ROLE_CHOICES = [
        ('관리자', '관리자'),
        ('의사', '의사'),
        ('물리 치료사', '물리 치료사'),
        ('기타 의료진', '기타 의료진'),
        ('환자', '환자'),
        ('간호사', '간호사'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, null=False)

    def __str__(self):
        return self.user_id

# 진료 데이터 모델 정의
class MedicalRecord(models.Model):
    id = models.AutoField(primary_key=True)  # 진료 기록번호, 자동 생성 필드
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)  # 환자와의 외래키 관계
    staff = models.ForeignKey(User, on_delete=models.CASCADE)  # 진료 담당 직원과의 외래키 관계
    date = models.DateField()  # 진료 일자, 날짜 필드
    symptoms = models.CharField(max_length=255)  # 증상, 문자열 필드
    diagnosis = models.CharField(max_length=255)  # 진단, 문자열 필드
    notes = models.TextField()  # 특이사항, 긴 텍스트 필드
    prescription_code = models.IntegerField()  # 약처방 코드 (향후 약처방 데이터 모델로 변경 가능)

    def __str__(self):
        return f"{self.patient.first_name}의 진료 기록"  # 문자열 표현을 정의한 메서드


# 처방 데이터 모델 정의
class Prescription(models.Model):
    prescription_code = models.AutoField(primary_key=True)  # 처방 코드, 자동 생성 필드
    medical_record = models.ForeignKey('MedicalRecord', on_delete=models.CASCADE)  # 진료 기록과의 외래키 관계
    medication_name = models.CharField(max_length=100)  # 처방 약 명, 문자열 필드
    total_dosage = models.DecimalField(max_digits=10, decimal_places=2)  # 총 투여량, 실수 필드
    frequency = models.IntegerField()  # 투여 횟수, 정수 필드
    duration_days = models.IntegerField()  # 투여 기간(일수), 정수 필드
    unit = models.CharField(max_length=20)  # 단위, 문자열 필드

    def __str__(self):
        return f"{self.medical_record.patient.first_name}의 처방 기록"  # 문자열 표현을 정의한 메서드

# 검사데이터 모델 정의
class ExaminationData(models.Model):
    record_number = models.AutoField(primary_key=True)  # 검사 기록번호, 자동 생성 필드
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)  # 환자 고유번호, 외래키 관계
    bone_mass = models.DecimalField(max_digits=10, decimal_places=2)  # 골결근량, 실수 필드
    body_fat = models.DecimalField(max_digits=5, decimal_places=2)  # 체지방량, 실수 필드
    muscle_strength = models.DecimalField(max_digits=5, decimal_places=2)  # 근지구력, 실수 필드
    cardiovascular_endurance = models.DecimalField(max_digits=5, decimal_places=2)  # 심폐지구력, 실수 필드
    agility = models.DecimalField(max_digits=5, decimal_places=2)  # 민첩성, 실수 필드
    flexibility = models.DecimalField(max_digits=5, decimal_places=2)  # 유연성, 실수 필드
    unique_number = models.CharField(max_length=50)  # 자료고유번호, 문자열 필드
    date = models.DateField()  # 검사 일자, 날짜 필드

    def __str__(self):
        return f"{self.patient.first_name}의 검사 데이터 기록"

# 치료데이터 모델 정의
class TreatmentData(models.Model):
    treatment_code = models.AutoField(primary_key=True)  # 치료코드, 자동 생성 필드
    medical_record = models.ForeignKey('MedicalRecord', on_delete=models.CASCADE)  # 진료코드(진료데이터 외래키)
    date = models.DateField()  # 일자, 날짜 필드
    therapy_type = models.CharField(max_length=50)  # 치료 종류, 문자열 필드
    therapy_days = models.IntegerField()  # 치료 일수, 정수 필드
    therapy_time = models.IntegerField()  # 치료 시간, 정수 필드

    def __str__(self):
        return f"{self.medical_record.patient.first_name}의 치료 기록"

# 운동데이터 모델 정의
class ExerciseData(models.Model):
    exercise_code = models.AutoField(primary_key=True)  # 운동 코드, 자동 생성 필드
    medical_record = models.ForeignKey('MedicalRecord', on_delete=models.CASCADE)  # 진료코드(진료데이터 외래키)
    date = models.DateField()  # 일자, 날짜 필드
    repetitions = models.IntegerField()  # 횟수, 정수 필드
    weight = models.DecimalField(max_digits=10, decimal_places=2)  # 중량, 실수 필드
    time = models.DecimalField(max_digits=5, decimal_places=2)  # 시간, 실수 필드
    speed = models.DecimalField(max_digits=5, decimal_places=2)  # 속도, 실수 필드
    distance = models.DecimalField(max_digits=10, decimal_places=2)  # 거리, 실수 필드
    exercise_type = models.CharField(max_length=50)  # 운동종류, 문자열 필드

    def __str__(self):
        return f"{self.medical_record.patient.first_name}의 운동 기록"