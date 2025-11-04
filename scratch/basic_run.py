from dkany.client import DKANClient as DkanyClient


def create_client() -> DkanyClient:
    return DkanyClient(
        base_url="https://edit.data.medicaid.gov", user_name="DEMO", password="your_api_key"
    )


def create_dataset() -> str:
    client = create_client()

    body = {
        "title": "Test Dataset from DKAN Client",
        "type": ["dataset"],
        "license": "http://opendatacommons.org/licenses/odc-by/1.0/",
        "accessLevel": "published",
    }

    response = client.create_dataset(body)

    print(f"Created dataset with ID: {response['identifier']}")
    return response["identifier"]


def dataset_exists(dataset_id: str) -> None:
    client = create_client()

    exists = client.check_dataset_exists(dataset_id)

    print(f"dataset {exists} exits")


def update_dataset(dataset_id: str):
    client = create_client()

    body = {
        "title": "Updated Test Dataset from DKAN Client",
        "type": ["dataset"],
        "license": "http://opendatacommons.org/licenses/odc-by/1.0/",
        "accessLevel": "hidden",
    }

    response = client.update_dataset(dataset_id, body)

    print(f"Updated dataset with ID: {response['identifier']}")


def remove_dataset(dataset_id: str):
    client = create_client()

    client.delete_dataset(dataset_id)

    print(f"Deleted dataset with ID: {dataset_id}")


def main():
    dataset_id = create_dataset()
    dataset_exists(dataset_id)
    update_dataset(dataset_id)
    remove_dataset(dataset_id)


if __name__ == "__main__":
    main()
