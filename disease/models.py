from django.contrib.auth.models import User
from django.db import models


class Disease(models.Model):

    class Meta:
        verbose_name = "Disease"
        verbose_name_plural = "Diseases"

    def __str__(self):
        return self.title

    title = models.CharField(max_length=50, default="")
    content = models.TextField()


class Question(models.Model):

    class Meta:
        verbose_name = "True/false question"
        verbose_name_plural = "True/false questions"

    def __str__(self):
        return self.statement

    def next(self):
        """The next question in the quiz, or None if this is the last"""
        # Note: this is expensive (linked list would be better), but quizzes are short
        questions = list(self.question.question_set.all())
        if not (self == questions[-1]):
            current_pos = questions.index(self)
            return questions[current_pos + 1]

    question = models.ForeignKey(Disease)
    statement = models.CharField(max_length=200)
    description=models.CharField(max_length=400,default='')
    answer = models.BooleanField("True?")


class UserAnswer(models.Model):

    class Meta:
        verbose_name = "User answer"
        verbose_name_plural = "User answers"

    def __str__(self):
        return "{}: {}: {}".format(self.user, self.question, self.answer)

    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    answer = models.BooleanField()
