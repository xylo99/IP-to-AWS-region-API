from unittest.mock import patch
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase


class CommandsTestCase(TestCase):

    def test_wait_for_db_ready(self):
        """Test waiting for PostgresDB after the instance is available"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as item:
            item.return_value = True
            call_command('wait_for_db')
            self.assertEqual(item.call_count, 1)

    # Patch decorator to mock time.sleep to speed up testing.
    # Hence it doesn't take 5 seconds to run test.
    @patch('time.sleep', return_value=None)
    def test_wait_for_db(self, ts):
        """Test waiting for db"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as item:
            # raise opeprational error 5 times, if possible, and complete on the
            # 6th time.
            item.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(item.call_count, 6)
