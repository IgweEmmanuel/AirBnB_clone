#!/usr/bin/python3
from unittest import TestCase
from models import BaseModel
from uuid import UUID

class TestBaseModel(TestCase):
    def test_uuid(self):
        bm1 = BaseModel()
        bm2 = BaseModel()

        self.assertTrue(hasattr(bm1, "id")
        self.assertNotEquals(bm1, bm2)
        self.assertIsInstance(UUID(bm1.id), UUID)
        self.assertIsInstance(bm1.id, str)
