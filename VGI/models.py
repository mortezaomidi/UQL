from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.gis.db import models as geomodel

class MyUser(AbstractUser):
    is_citizen = geomodel.BooleanField(default=False)
    is_expert = geomodel.BooleanField(default=False)
    is_admin = geomodel.BooleanField(default=False)


@python_2_unicode_compatible  # only if you need to support Python 2
class Criteria(geomodel.Model):
    user = geomodel.OneToOneField(MyUser, on_delete=geomodel.CASCADE)

    Q1 = (
        (1, "Negligible"),
        (2, "Very low"),
        (3, "Low"),
        (4, "Moderate"),
        (5, "High"),
        (7, "Very High"),
        (8, "Extreme"),
        )
    Q2 = (
        (1, "Very Bad"),
        (2, "Bad"),
        (3, "Somewhat Bad"),
        (4, "Neither Good nor Bad"),
        (5, "Somewhat Good"),
        (6, "Good"),
        (7, "Very Good"),
        )
    Q3 = (
        (1, "Strongly Disagree"),
        (2, "Disagree"),
        (3, "Somewhat Disagree"),
        (4, "Neither Agree Nor Disagree"),
        (5, "Somewhat Agree"),
        (6, "Agree"),
        (7, "Strongly Agree"),
        )

    # Enviromental Critera
    q11 = geomodel.PositiveSmallIntegerField(choices=Q1, verbose_name=None)
    q12 = geomodel.PositiveSmallIntegerField(choices=Q1, verbose_name=None)
    q13 = geomodel.PositiveSmallIntegerField(choices=Q1, verbose_name=None)
    q14 = geomodel.PositiveSmallIntegerField(choices=Q2, verbose_name=None)
    q15 = geomodel.PositiveSmallIntegerField(choices=Q2, verbose_name=None)

    @property
    def sum_q1(self):
        return self.q11 + self.q12 + self.q13 + self.q14 + self.q15

    # Socio-economic Criteria
    q21 = geomodel.PositiveSmallIntegerField(choices=Q1, verbose_name=None)
    q22 = geomodel.PositiveSmallIntegerField(choices=Q1, verbose_name=None)
    q23 = geomodel.PositiveSmallIntegerField(choices=Q1, verbose_name=None)
    q24 = geomodel.PositiveSmallIntegerField(choices=Q1, verbose_name=None)
    q25 = geomodel.PositiveSmallIntegerField(choices=Q1, verbose_name=None)
    q26 = geomodel.PositiveSmallIntegerField(choices=Q1, verbose_name=None)
    q27 = geomodel.PositiveSmallIntegerField(choices=Q1, verbose_name=None)
    q28 = geomodel.PositiveSmallIntegerField(choices=Q1, verbose_name=None)
    q29 = geomodel.PositiveSmallIntegerField(choices=Q3, verbose_name=None)
    q210 = geomodel.PositiveSmallIntegerField(choices=Q3, verbose_name=None)

    @property
    def sum_q2(self):
        return self.q21 + self.q22 + self.q23 + self.q24 + self.q25 \
         + self.q26 + self.q27 + self.q28 + self.q29 + self.q210

    # Phisical Criteria
    q31 = geomodel.PositiveSmallIntegerField(choices=Q1, verbose_name=None)
    q32 = geomodel.PositiveSmallIntegerField(choices=Q1, verbose_name=None)
    q32 = geomodel.PositiveSmallIntegerField(choices=Q1, verbose_name=None)
    q33 = geomodel.PositiveSmallIntegerField(choices=Q2, verbose_name=None)
    q34 = geomodel.PositiveSmallIntegerField(choices=Q2, verbose_name=None)
    q35 = geomodel.PositiveSmallIntegerField(choices=Q2, verbose_name=None)
    q36 = geomodel.PositiveSmallIntegerField(choices=Q2, verbose_name=None)
    q37 = geomodel.PositiveSmallIntegerField(choices=Q2, verbose_name=None)
    q38 = geomodel.PositiveSmallIntegerField(choices=Q2, verbose_name=None)
    q39 = geomodel.PositiveSmallIntegerField(choices=Q2, verbose_name=None)
    q310 = geomodel.PositiveSmallIntegerField(choices=Q2, verbose_name=None)
    q311 = geomodel.PositiveSmallIntegerField(choices=Q3, verbose_name=None)
    q312 = geomodel.PositiveSmallIntegerField(choices=Q3, verbose_name=None)
    q313 = geomodel.PositiveSmallIntegerField(choices=Q3, verbose_name=None)
    q314 = geomodel.PositiveSmallIntegerField(choices=Q3, verbose_name=None)
    q315 = geomodel.PositiveSmallIntegerField(choices=Q3, verbose_name=None)
    q316 = geomodel.PositiveSmallIntegerField(choices=Q3, verbose_name=None)
    q317 = geomodel.PositiveSmallIntegerField(choices=Q3, verbose_name=None)

    @property
    def sum_q3(self):
        return self.q31 + self.q32 + self.q33 + self.q34 + self.q35 + self.q36 \
            + self.q37 + self.q38 + self.q39 + self.q310 + self.q311 + self.q312 \
            + self.q313 + self.q314 + self.q315 + self.q316 + self.q317

    def __str__(self):
        return "Sum of Enviromental: " + str(self.sum_q1) + \
        " Sum of Socio-economical: " + \
        str(self.sum_q2) + " Sum of Phisical: " + str(self.sum_q3)
