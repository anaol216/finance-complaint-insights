import unittest
from src.rag_pipeline import rag_answer

class TestRAGPipeline(unittest.TestCase):
    def test_basic_query(self):
        query = "Why are customers unhappy with personal loans?"
        result = rag_answer(query)
        self.assertIn("answer", result)
        self.assertIn("sources", result)
        self.assertTrue(len(result["sources"]) > 0)

if __name__ == '__main__':
    unittest.main()
