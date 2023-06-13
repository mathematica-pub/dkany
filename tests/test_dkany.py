from dkany.client import DKANClient as DkanyClient
import unittest

class TestDkanyClient(unittest.TestCase):
    def setUp(self):
        self.client = DkanyClient(
            base_url = "https://edit.data.medicaid.gov"
        )

    def test_check_dataset_exists(self):
        test_dataset_id = "9e407144-9ed9-5cee-937a-17d65b07a9a7"
        exists = self.client.check_dataset_exists(test_dataset_id)
        print(f"dataset {exists} exists")
        assert exists == True
        
    def test_search(self):
        title_success = "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-02-06-to-2023-02-12"
        search_success = self.client.search(title=title_success)
        assert len(search_success) == 1
        print("Search success:", len(search_success))
        
        title_fail = "Product Data for asdfasdf"
        search_fail = self.client.search(title=title_fail)
        assert len(search_fail) == 0
        print("Search fail:", len(search_fail))
        
    def test_get_dataset_metadata(self):
        test_dataset_id = "9e407144-9ed9-5cee-937a-17d65b07a9a7"
        metadata = self.client.get_dataset_metadata(test_dataset_id)
        assert metadata["identifier"] == test_dataset_id
    
    def test_get_data_by_dataset_identifier(self):
        test_dataset_id = "9e407144-9ed9-5cee-937a-17d65b07a9a7"
        results = self.client.get_data_by_dataset_identifier(test_dataset_id)
        assert len(results) > 0