class DKANClient(object):
    base_url: str | None
    cookie_dict: dict | None
    user_name: str | None
    password: str | None
    
    def search(self, title: str=None, tags: dict[str:str]=None, 
               categories: str=None, page: str="ALL") -> dict:
        ...

    def filter_search_results(self, search_results: dict, 
                              filter_params: dict[str:str]) -> dict:
        ...

    def create_dataset(self, body: any) -> dict:
        ...

    def delete_dataset(self, dataset_identifier: str) -> dict:
        ...

    def update_dataset(self, dataset_identifier: str, body: any)-> dict:
        ...

    def mark_dataset_hidden(self, dataset_identifier: str, message: str="") -> any:
        """
        Sets dataset accesslevel to "hidden"
        Hides dataset from searches made on data.medicare.gov user interface
        """
        ...

    def mark_dataset_public(self, dataset_identifier: str, message: str="") -> any:
        """
        Sets dataset accesslevel to "published"
        Makes a dataset searchable through data.medicare.gov user interface
        """
        ...

    def get_dataset_metadata(self, dataset_identifier: str) -> dict:
        ...
    
    def check_dataset_exists(self, dataset_identifier: str) -> bool:
        ...
    
    def trigger_dataset_reimport(self, dataset_identifier: str) -> any:
        ...
    
    def get_full_query_url(self, dataset_identifier: str, datastore_idx: int=0) -> str:
        ...
    
    def get_data_by_dataset_identifier(self, dataset_identifier: str, datastore_idx: int=0)-> dict:
         ...