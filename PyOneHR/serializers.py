from datetime import date

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.signing import TimestampSigner
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from rest_framework.reverse import reverse

