# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import TestCase
from django.utils import timezone

from core.models import Child
from babybuddy.templatetags import babybuddy_tags


class TemplateTagsTestCase(TestCase):
    def test_child_count(self):
        self.assertEqual(babybuddy_tags.get_child_count(), 0)
        Child.objects.create(
            first_name="Test", last_name="Child", birth_date=timezone.localdate()
        )
        self.assertEqual(babybuddy_tags.get_child_count(), 1)
        Child.objects.create(
            first_name="Test", last_name="Child 2", birth_date=timezone.localdate()
        )
        self.assertEqual(babybuddy_tags.get_child_count(), 2)

    def user_is_read_only(self):
        user = get_user_model().objects.create_user(
            username="readonly", password="readonly", is_superuser=False, is_staf=False
        )
        self.assertFalse(babybuddy_tags.user_is_read_only(user))

        group = Group.objects.get(name="read_only")
        user.groups.add(group)
        self.assertTrue(babybuddy_tags.user_is_read_only(user))
