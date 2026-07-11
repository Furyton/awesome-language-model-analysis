import os
import tempfile
import unittest

import generate_readme


class GenerateReadmeParsingTests(unittest.TestCase):
    def test_get_section_list_skips_malformed_rows(self):
        original_root = generate_readme.ROOT
        try:
            with tempfile.TemporaryDirectory() as tmp_dir:
                generate_readme.ROOT = tmp_dir
                topic = "test-topic"
                topic_dir = os.path.join(tmp_dir, topic)
                os.makedirs(topic_dir, exist_ok=True)

                csv_path = os.path.join(topic_dir, generate_readme.FILE_NAME)
                with open(csv_path, "w", encoding="utf-8") as f:
                    f.write("Title,Date,Url,Author\n")
                    f.write("Good Paper,2024-02-01,http://example.com/good,Good Author\n")
                    f.write("Bad Paper,2024-01-01,http://example.com/bad,Bad Author,EXTRA\n")

                paper_list, rows = generate_readme.get_section_list(topic)
                self.assertEqual(len(paper_list), 1)
                self.assertEqual(len(rows), 1)
                self.assertIn("Good Paper", paper_list[0])
        finally:
            generate_readme.ROOT = original_root


if __name__ == "__main__":
    unittest.main()
