import unittest
import os
from chatbot import RAGChatbot

class TestRAGChatbot(unittest.TestCase):
    def setUp(self):
        self.test_dir = "./test_knowledge_base"
        os.makedirs(self.test_dir, exist_ok=True)
        with open(f"{self.test_dir}/test_doc.txt", "w") as f:
            f.write("This is a test document.")
        self.chatbot = RAGChatbot(self.test_dir)

    def test_basic_query(self):
        response = self.chatbot.chat("What is in the test document?")
        self.assertIsNotNone(response)
        self.assertIsInstance(response, str)

    def test_document_addition(self):
        new_doc_path = f"{self.test_dir}/new_doc.txt"
        with open(new_doc_path, "w") as f:
            f.write("This is a new test document.")
        result = self.chatbot.add_document(new_doc_path)
        self.assertTrue("Successfully" in result)

    def tearDown(self):
        import shutil
        shutil.rmtree(self.test_dir)

if __name__ == '__main__':
    unittest.main()