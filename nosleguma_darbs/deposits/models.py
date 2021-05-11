import decimal

from django.db import models


class Deposit(models.Model):
    deposit = models.IntegerField()
    term = models.IntegerField()
    rate = models.DecimalField(decimal_places=2, max_digits=10)

    def interest(self):
        s = 0
        for t in range(self.term):
            s = self.deposit * ((1+self.rate) ** (t+1))
        result = s - self.deposit

        return result
