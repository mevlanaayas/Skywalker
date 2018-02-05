# -*- coding: utf-8 -*-
from url_filter import filtersets
from base.models import CustomUser


class UserFilter(filtersets.ModelFilterSet):
    """

    """

    class Meta:
        """

        """
        model = CustomUser
