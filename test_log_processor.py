import unittest
from unittest.mock import mock_open, patch
from log_processor import extract_instance_ids, process_log_file  # Import your functions

class TestLogProcessing(unittest.TestCase):
    
    def test_extract_instance_ids(self):
        log_data = [
            'Instance Id = 123\n',
            'Some other line\n',
            'Instance Id = 456\n',
            'Instance Id = 123\n'
        ]
        expected_ids = ['123', '456']
        result = extract_instance_ids(log_data, "Instance Id = ")
        self.assertEqual(result, expected_ids)

    @patch('builtins.open', new_callable=mock_open, read_data='Instance Id = 123\n{"entityId": "456", "entityName": "Test Entity"}\n')
    def test_process_log_file(self, mock_file):
        process_log_file('2024-08-08.log')
        mock_file.assert_called_once_with('2024-08-08.log', 'r')
        # You can further check the contents of the output file if needed

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            process_log_file('non_existent_file.log')

if __name__ == '__main__':
    unittest.main()
