import intent_engine
import actions
import unittest
from unittest.mock import patch, MagicMock

class TestVoiceAssistant(unittest.TestCase):
    
    def test_intent_parsing_open_chrome(self):
        intent, entity = intent_engine.parse_intent("open chrome")
        self.assertEqual(intent, "OPEN_APP")
        self.assertEqual(entity, "chrome")

    def test_intent_parsing_search_google(self):
        intent, entity = intent_engine.parse_intent("search for python tutorial on google")
        self.assertEqual(intent, "SEARCH_GOOGLE")
        self.assertEqual(entity, "python tutorial")

    def test_intent_parsing_shutdown(self):
        intent, entity = intent_engine.parse_intent("shutdown system")
        self.assertEqual(intent, "SYSTEM_CONTROL")
        self.assertEqual(entity, "shutdown")

    @patch('actions.webbrowser.open')
    def test_action_search_google(self, mock_browser):
        actions.search_google("test query")
        mock_browser.assert_called_with("https://www.google.com/search?q=test query")

    @patch('actions.os.system')
    def test_action_open_notepad(self, mock_os):
        actions.open_notepad()
        mock_os.assert_called_with("start notepad")

if __name__ == '__main__':
    print("Running tests...")
    unittest.main()
