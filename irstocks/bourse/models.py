from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class Indicator(models.Model):
    name = models.CharField(max_length=10)   
    SAR = models.FloatField()
    ADX = models.FloatField()
    CCI = models.FloatField()
    STOCHASTIC_VALUE = models.FloatField(default=0.0)
    STOCHASTIC_SIGNAL = models.FloatField(default=0.0)
    RSI = models.FloatField(default=0.0)
    MFI = models.FloatField(default=0.0)
    MOMENTUM = models.FloatField(default=0.0)
    VOLUME = models.FloatField(default=0.0)
    MACD_VALUE = models.FloatField(default=0.0)  
    MACD_HISTOGRAM = models.FloatField(default=0.0)
    MACD_SIGNAL = models.FloatField(default=0.0)
    BOLLINGER_UPPERBAND = models.FloatField(default=0.0)
    BOLLINGER_MIDDLEBAND = models.FloatField(default=0.0)
    BOLLINGER_LOWERBAND = models.FloatField(default=0.0)

    def __str__(self):
        # return self.name + ' ' + str(self.SAR)
        return self.name

class Shares_Specifications(models.Model):
    NAME = models.CharField(max_length=20, default='', null=True)
    INSTANCE_CODE = models.BigIntegerField(default=0, null=True)
    FULL_NAME = models.CharField(max_length=50, default='', null=True)
    TYPE = models.CharField(max_length=200, default='', null=True)
    FIRST_PRICE = models.FloatField(default=0.0, null=True)
    CLOSE_PRICE = models.FloatField(default=0.0, null=True)
    CLOSE_PRICE_CHANGE = models.FloatField(default=0.0, null=True)
    CLOSE_PRICE_CHANGE_PERCENT = models.CharField(max_length=20, default='', null=True)
    FINAL_PRICE = models.FloatField(default=0.0, null=True)
    FINAL_PRICE_CHANGE = models.FloatField(default=0.0, null=True)
    FINAL_PRICE_CHANGE_PERCENT = models.CharField(max_length=20, default='', null=True)
    HIGHEST_PRICE = models.FloatField(default=0.0, null=True)
    LOWEST_PRICE = models.FloatField(default=0.0, null=True)
    EPS = models.FloatField(default=0.0, null=True)
    PE = models.FloatField(default=0.0, null=True)
    SELL_COUNT_1 = models.FloatField(default=0.0, null=True)
    SELL_COUNT_2 = models.FloatField(default=0.0, null=True)
    SELL_COUNT_3 = models.FloatField(default=0.0, null=True)
    SELL_VOLUME_1 = models.FloatField(default=0.0, null=True)
    SELL_VOLUME_2 = models.FloatField(default=0.0, null=True)
    SELL_VOLUME_3 = models.FloatField(default=0.0, null=True)
    SELL_PRICE_1 = models.FloatField(default=0.0, null=True)
    SELL_PRICE_2 = models.FloatField(default=0.0, null=True)
    SELL_PRICE_3 = models.FloatField(default=0.0, null=True)
    BUY_COUNT_1  = models.FloatField(default=0.0, null=True)
    BUY_COUNT_2 = models.FloatField(default=0.0, null=True)
    BUY_COUNT_3 = models.FloatField(default=0.0, null=True)
    BUY_VOLUME_1 = models.FloatField(default=0.0, null=True)
    BUY_VOLUME_2 = models.FloatField(default=0.0, null=True)
    BUY_VOLUME_3 = models.FloatField(default=0.0, null=True)
    BUY_PRICE_1 = models.FloatField(default=0.0, null=True)
    BUY_PRICE_2 = models.FloatField(default=0.0, null=True)
    BUY_PRICE_3 = models.FloatField(default=0.0, null=True)
    CO_BUY_COUNT = models.FloatField(default=0.0, null=True)
    REAL_BUY_COUNT = models.FloatField(default=0.0, null=True)
    REAL_SELL_COUNT = models.FloatField(default=0.0, null=True)
    CO_SELL_COUNT = models.FloatField(default=0.0, null=True)
    REAL_BUY_VOLUME = models.FloatField(default=0.0, null=True)
    CO_BUY_VOLUME = models.FloatField(default=0.0, null=True)
    REAL_SELL_VOLUME = models.FloatField(default=0.0, null=True)
    CO_SELL_VOLUME = models.FloatField(default=0.0, null=True)
    REAL_BUY_VALUE = models.FloatField(default=0.0, null=True)
    CO_BUY_VALUE = models.FloatField(default=0.0, null=True)
    REAL_SELL_VALUE = models.FloatField(default=0.0, null=True)
    CO_SELL_VALUE = models.FloatField(default=0.0, null=True)
    TRADE_NUMBER = models.FloatField(default=0.0, null=True)
    TRADE_VOLUME = models.FloatField(default=0.0, null=True)
    TRADE_VALUE = models.FloatField(default=0.0, null=True)
    ALL_STOCKS = models.FloatField(default=0.0, null=True)
    BASIS_VOLUME = models.FloatField(default=0.0, null=True)
    # ######################## Stats
    N_DAY_3M = models.SmallIntegerField(default=0, null=True)
    N_DAY_12M = models.SmallIntegerField(default=0, null=True)
    N_PERCENT_12M = models.SmallIntegerField(default=0, null=True)
    N_RANK_3M = models.SmallIntegerField(default=0, null=True)
    N_RANK_12M = models.SmallIntegerField(default=0, null=True)
    P_DAY_3M = models.SmallIntegerField(default=0, null=True)
    P_DAY_12M = models.SmallIntegerField(default=0, null=True)
    P_PERCENT_12M = models.SmallIntegerField(default=0, null=True)
    P_RANK_3M = models.SmallIntegerField(default=0, null=True)
    P_RANK_12M = models.SmallIntegerField(default=0, null=True)
    TRADE_NDAY_3M = models.SmallIntegerField(default=0, null=True)
    TRADE_NDAY_12M = models.SmallIntegerField(default=0, null=True)
    TRADE_DAY_3M = models.SmallIntegerField(default=0, null=True)
    TRADE_DAY_12M = models.SmallIntegerField(default=0, null=True)
    TRADE_RANK_3M = models.SmallIntegerField(default=0, null=True)
    TRADE_RANK_12M = models.SmallIntegerField(default=0, null=True)
    TN_AVERAGE_3M = models.BigIntegerField(default=0, null=True)
    TN_AVERAGE_12M = models.BigIntegerField(default=0, null=True)
    TN_RANK_3M = models.SmallIntegerField(default=0, null=True)
    TN_RANK_12M = models.SmallIntegerField(default=0, null=True)
    TN_LAST_DAY = models.SmallIntegerField(default=0, null=True)
    TVAL_AVERAGE_3M = models.BigIntegerField(default=0, null=True)
    TVAL_AVERAGE_12M = models.BigIntegerField(default=0, null=True)
    TVAL_RANK_3M = models.SmallIntegerField(default=0, null=True)
    TVAL_RANK_12M = models.SmallIntegerField(default=0, null=True)
    TVAL_LAST_DAY = models.BigIntegerField(default=0, null=True)

    # ######################## Indicator
    ADX = models.FloatField(default=0.0, null=True)
    CCI = models.FloatField(default=0.0, null=True)
    STOCHASTIC_VALUE = models.FloatField(default=0.0, null=True)
    STOCHASTIC_SIGNAL = models.FloatField(default=0.0, null=True)
    STOCHASTIC_RSI = models.FloatField(default=0.0, null=True)
    RSI = models.FloatField(default=0.0, null=True)
    MFI = models.FloatField(default=0.0, null=True)
    MOMENTUM = models.FloatField(default=0.0, null=True)
    VOLUME = models.FloatField(default=0.0, null=True)
    MACD_VALUE = models.FloatField(default=0.0, null=True)  
    MACD_HISTOGRAM = models.FloatField(default=0.0, null=True)
    MACD_SIGNAL = models.FloatField(default=0.0, null=True)
    BOLLINGER_UPPERBAND = models.FloatField(default=0.0, null=True)
    BOLLINGER_MIDDLEBAND = models.FloatField(default=0.0, null=True)
    BOLLINGER_LOWERBAND = models.FloatField(default=0.0, null=True)
    ICHIMOKU_TENKEN_SEN = models.FloatField(default=0.0, null=True)
    ICHIMOKU_KIJUN_SEN = models.FloatField(default=0.0, null=True)
    EMA_5 = models.FloatField(default=0.0, null=True)
    EMA_10 = models.FloatField(default=0.0, null=True)
    EMA_20 = models.FloatField(default=0.0, null=True)
    EMA_30 = models.FloatField(default=0.0, null=True)
    EMA_50 = models.FloatField(default=0.0, null=True)
    SMA_5 = models.FloatField(default=0.0, null=True)
    SMA_10 = models.FloatField(default=0.0, null=True)
    SMA_20 = models.FloatField(default=0.0, null=True)
    SMA_30 = models.FloatField(default=0.0, null=True)
    SMA_50 = models.FloatField(default=0.0, null=True)
    WILLIAMS_PERCENT_RANGE = models.FloatField(default=0.0, null=True)


    def __str__(self):
        # return self.name + ' ' + str(self.SAR)
        return self.NAME