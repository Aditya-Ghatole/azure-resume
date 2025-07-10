import azure.functions as func
import os
import json
from azure.cosmos import CosmosClient, exceptions

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Read env vars
        url = os.environ["COSMOS_DB_URL"]
        key = os.environ["COSMOS_DB_KEY"]
        db_name = os.environ["COSMOS_DB_NAME"]
        container_name = os.environ["COSMOS_DB_CONTAINER"]

        # Connect to Cosmos DB
        client = CosmosClient(url, credential=key)
        container = client.get_database_client(db_name).get_container_client(container_name)

        # Fetch the view count
        item = container.read_item(item="home", partition_key="home")
        item["views"] += 1

        # Update it
        container.upsert_item(item)

        return func.HttpResponse(
            json.dumps({"views": item["views"]}),
            mimetype="application/json",
            status_code=200
        )

    except exceptions.CosmosHttpResponseError as e:
        return func.HttpResponse(
            f"Cosmos DB error: {str(e)}",
            status_code=500
        )
    except Exception as e:
        return func.HttpResponse(
            f"Unexpected error: {str(e)}",
            status_code=500
        )
