import azure.functions as func
import os
import json
from azure.cosmos import CosmosClient
from azure.cosmos.exceptions import CosmosResourceNotFoundError

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="TrackViews", methods=["GET"])
def track_views(req: func.HttpRequest) -> func.HttpResponse:
    try:
        url = os.environ["COSMOS_DB_URL"]
        key = os.environ["COSMOS_DB_KEY"]
        db_name = os.environ["COSMOS_DB_NAME"]
        container_name = os.environ["COSMOS_DB_CONTAINER"]

        client = CosmosClient(url, credential=key)
        container = client.get_database_client(db_name).get_container_client(container_name)

        try:
            item = container.read_item(item="home", partition_key="home")
            item["views"] += 1
            container.upsert_item(item)
        except CosmosResourceNotFoundError:
            item = {"id": "home", "views": 1}
            container.create_item(item)

        # Read item and increment views
        item = container.read_item(item="home", partition_key="home")
        item["views"] += 1
        container.upsert_item(item)

        return func.HttpResponse(
            json.dumps({"views": item["views"]}),
            mimetype="application/json",
            status_code=200
        )

    except Exception as e:
        return func.HttpResponse(
            f"Error: {str(e)}",
            status_code=500
        )
