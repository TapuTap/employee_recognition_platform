from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.timezone import now
from tinymce.models import HTMLField
from django.contrib.auth import get_user_model


User = get_user_model()
    

class Manager(models.Model):
    first_name = models.CharField(_("first name"), max_length=50)
    last_name = models.CharField(_("last name"), max_length=50)
    email = models.EmailField(_("email"), max_length=254)
    hire_date = models.DateField(_("hire date"), auto_now=False, auto_now_add=False, default=now)
    term_date = models.DateField(_("termination date"), auto_now=False, null=True, blank=True)
    department = models.CharField(_("department"), max_length=50)
    user = models.OneToOneField(
        User,
        verbose_name=("user_profile"),
        on_delete=models.CASCADE,
        related_name='manager',
        null=True,
        blank=True
    )    
    STATUS_ACTIVITY = (
        (0, _('Active')),
        (1, _('Terminated'))
    )
    status = models.PositiveSmallIntegerField(
        _("status"), 
        choices=STATUS_ACTIVITY, 
        default=0,
        db_index=True
    )

    class Meta:
        verbose_name = _("manager")
        verbose_name_plural = _("managers")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("manager_detail", kwargs={"pk": self.pk})
    

class Employee(models.Model):
    first_name = models.CharField(_("first name"), max_length=50)
    last_name = models.CharField(_("last name"), max_length=50)
    email = models.EmailField(_("email"), max_length=254)
    hire_date = models.DateField(_("hire date"), auto_now=False, auto_now_add=False, default=now)
    term_date = models.DateField(_("termination date"), auto_now=False, null=True, blank=True)
    position = models.CharField(_("position"), max_length=50)
    manager = models.ForeignKey(
        Manager,
        verbose_name=_("manager"),
        on_delete=models.CASCADE, 
        related_name="employees",
        null=True, blank=True,
    )
    user = models.OneToOneField(
        User,
        verbose_name=_("user"),
        on_delete=models.CASCADE,
        related_name='employee',
        null=True,
        blank=True
    )

    STATUS_ACTIVITY = (
        (0, _('Active')),
        (1, _('Terminated')),
    )

    status = models.PositiveSmallIntegerField(
        _("status"), 
        choices=STATUS_ACTIVITY, 
        default=0,
        db_index=True
    )

    class Meta:
        verbose_name = _("employee")
        verbose_name_plural = _("employees")

    def __str__(self):
        return f"{self.first_name} {self.last_name} "

    def get_absolute_url(self):
        return reverse("employee_detail", kwargs={"pk": self.pk})
    
class Goal(models.Model):
    title = models.CharField(_("title"), max_length=150, db_index=True, blank=True, null=True)
    description = HTMLField(_("description"), max_length=2000, db_index=True, blank=True, null=True)
    start_date = models.DateField(_("start date"), auto_now=False, auto_now_add=False, default= now)
    end_date = models.DateField(_("end date"), auto_now=False, null=True, blank=True)
    owner = models.ForeignKey(
        User,
        verbose_name=_("owner"),
        on_delete=models.CASCADE,
        related_name="goal_owner",
        null=True, blank=True,
        )

    PRIORITY_CHOICES = (
        (0, _('High')),
        (1, _('Medium')),
        (2, _('Low')),
    )
    priority = models.PositiveSmallIntegerField(
        _("priority"), 
        choices=PRIORITY_CHOICES, 
        default=0,
        db_index=True
    )
    GOAL_STATUS = (
        (0, _('Planned')),
        (1, _('In progress')),
        (2, _('Complete')),
        (3, _('On hold')),
        (4, _('Cancelled')),
    )
    status = models.PositiveSmallIntegerField(
        _("status"), 
        choices=GOAL_STATUS, 
        default=0,
        db_index=True
    )
    PROGRESS_CHOICES = (
        (0, _('0 %')),
        (1, _('10 %')),
        (2, _('20 %')),
        (3, _('30 %')),
        (4, _('40 %')),
        (5, _('50 %')),
        (6, _('60 %')),
        (7, _('70 %')),
        (8, _('80 %')),
        (9, _('90 %')),
        (10, _('100 %')),
    )
    progress = models.PositiveSmallIntegerField(
        _("progress"), 
        choices=PROGRESS_CHOICES, 
        default=0,
        db_index=True
    )

    class Meta:
        verbose_name = _("goal")
        verbose_name_plural = _("goals")

    def __str__(self):
        status = dict(Goal.GOAL_STATUS)[self.status]
        return f'{self.title}, {status}'

    def get_absolute_url(self):
        return reverse("goal_detail", kwargs={"pk": self.pk})


class Review(models.Model):
    SCORE_CHOICES = (
        (0, _('Nearly Meets Expectations')),
        (8, _('Meets Expectations')),
        (15, _('Exceeds Expectations')),
    )
    goals_achievment = HTMLField(_("goals achievment"), max_length=2000, db_index=True, blank=True, null=True)
    goals_review = models.PositiveSmallIntegerField(
        _("goals review"), 
        choices=SCORE_CHOICES, 
        default=0,
        db_index=True
    )
    teamwork = HTMLField(_("teamwork"), max_length=2000, db_index=True, blank=True, null=True)
    teamwork_review = models.PositiveSmallIntegerField(
        _("teamwork review"), 
        choices=SCORE_CHOICES, 
        default=0,
        db_index=True
    )
    innovation = HTMLField(_("innovation"), max_length=2000, db_index=True, blank=True, null=True)
    innovation_review = models.PositiveSmallIntegerField(
        _("innovation review"), 
        choices=SCORE_CHOICES, 
        default=0,
        db_index=True
    )
    work_ethics = HTMLField(_("work ethics"), max_length=2000, db_index=True, blank=True, null=True)
    work_ethics_review = models.PositiveSmallIntegerField(
        _("work ethics review"), 
        choices=SCORE_CHOICES, 
        default=0,
        db_index=True
    )
    total_review =models.PositiveSmallIntegerField(
        _("total review"), 
        choices=SCORE_CHOICES, 
        default=0,
        db_index=True
    )
    manager = models.ForeignKey(
        User,
        verbose_name=_("manager"),
        on_delete=models.CASCADE,
        related_name="reviews_manager",
        null=True, blank=True,
    )
    employee = models.ForeignKey(
        Employee,
        verbose_name=_("employee"),
        on_delete=models.CASCADE, 
        related_name="rewiews",
        null=True, blank=True,
    )

    class Meta:
        verbose_name = _("review")
        verbose_name_plural = _("reviews")

    def __str__(self):
        return f'{self.employee.first_name} {self.employee.last_name},{self.total_review}'

    def get_absolute_url(self):
        return reverse("review_detail", kwargs={"pk": self.pk})
