from django.test import SimpleTestCase
from rest_framework.test import APIRequestFactory

from apps.core.api import healthcheck


class HealthcheckTests(SimpleTestCase):
    def test_returns_ok_status(self):
        request = APIRequestFactory().get("/api/v1/health/")
        response = healthcheck(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"status": "ok"})
