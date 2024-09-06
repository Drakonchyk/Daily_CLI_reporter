import unittest
from unittest.mock import patch
from collections import defaultdict
from datetime import datetime, timedelta
from main import get_time_entries, generate_report, format_time, print_report, ensure_timezone_aware
import pytz

class TestClockifyReport(unittest.TestCase):
    """Unit tests for Clockify Report functionalities."""

    def setUp(self):
        """Set up common test data."""
        self.utc = pytz.utc
        self.sample_time_entries = [
            {
                "description": "Task 1",
                "timeInterval": {
                    "start": "2023-09-05T08:00:00Z",
                    "end": "2023-09-05T10:00:00Z"
                }
            },
            {
                "description": "Task 2",
                "timeInterval": {
                    "start": "2023-09-05T11:00:00Z",
                    "end": "2023-09-05T12:30:00Z"
                }
            }
        ]

    @patch('requests.get')
    def test_get_time_entries_success(self, mock_get):
        """
        Test that get_time_entries successfully retrieves data from the API.
        """
        mock_response_data = [
            {
                "description": "Task 1",
                "timeInterval": {
                    "start": "2023-09-05T08:00:00Z",
                    "end": "2023-09-05T10:00:00Z"
                }
            }
        ]
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response_data

        result = get_time_entries()
        self.assertEqual(result, mock_response_data)

    @patch('requests.get')
    def test_get_time_entries_failure(self, mock_get):
        """
        Test that get_time_entries returns None when the API request fails.
        """
        mock_get.return_value.status_code = 400

        result = get_time_entries()
        self.assertIsNone(result)

    def test_generate_report(self):
        """
        Test that generate_report correctly processes time entries into a report structure.
        """
        report = generate_report(self.sample_time_entries)

        expected_report = defaultdict(lambda: defaultdict(list))
        expected_report[datetime(2023, 9, 5).date()]['Task 1'].append((
            datetime(2023, 9, 5, 10, 0, 0, tzinfo=self.utc),
            2 * 60 * 60
        ))
        expected_report[datetime(2023, 9, 5).date()]['Task 2'].append((
            datetime(2023, 9, 5, 12, 30, 0, tzinfo=self.utc),
            1.5 * 60 * 60
        ))

        self.assertEqual(report, expected_report)

    def test_format_time(self):
        """
        Test that format_time correctly formats seconds into HH:MM:SS string.
        """
        self.assertEqual(format_time(3600), "1:00:00")
        self.assertEqual(format_time(3661), "1:01:01")

    def test_ensure_timezone_aware(self):
        """
        Test ensure_timezone_aware correctly converts naive datetime to aware datetime.
        """
        naive_dt = datetime(2023, 9, 5, 10, 0, 0)
        aware_dt = datetime(2023, 9, 5, 10, 0, 0, tzinfo=self.utc)

        self.assertEqual(ensure_timezone_aware(naive_dt), aware_dt)
        self.assertEqual(ensure_timezone_aware(None), datetime.min.replace(tzinfo=self.utc))

    @patch('builtins.print')
    def test_print_report(self, mock_print):
        """
        Test that print_report outputs the correct formatted report.
        """
        report = defaultdict(lambda: defaultdict(list))
        report[datetime(2023, 9, 5).date()]['Task 1'].append((
            datetime(2023, 9, 5, 10, 0, 0, tzinfo=self.utc),
            2 * 60 * 60
        ))
        report[datetime(2023, 9, 5).date()]['Task 2'].append((
            None,
            None
        ))

        print_report(report)

        mock_print.assert_any_call("Summary Report:")
        mock_print.assert_any_call(f"\nDate: {datetime(2023, 9, 5).date()}")
        mock_print.assert_any_call("\tTask: Task 1 \n\t- Completed at: 10:00:00 \n\t- Time spent: 2:00:00")
        mock_print.assert_any_call("\tTask: Task 2 \n\t- Ongoing \n\t- Time spent: Unknown")

if __name__ == '__main__':
    unittest.main()
