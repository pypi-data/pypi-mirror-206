import logging
import uuid
from typing import Optional

from typeguard import typechecked

from gantry.api_client import APIClient
from gantry.applications.core import Application
from gantry.applications.llm import CompletionApplication

logger = logging.getLogger(__name__)


class ApplicationClient:
    def __init__(self, api_client: APIClient) -> None:
        self._api_client = api_client

    @typechecked
    def create_application(
        self, application_name: str, application_type: Optional[str] = None
    ) -> Application:
        """
        Create an empty application.
        """
        data = {
            "model_name": application_name,
        }
        if application_type:
            data["model_type"] = application_type

        res = self._api_client.request(
            "POST",
            "/api/v1/applications",
            json=data,
            raise_for_status=True,
        )

        return self._get_application(
            name=application_name,
            id=uuid.UUID(res["data"]["id"]),
            type=application_type,
        )

    @typechecked
    def get_application(self, application_name: str) -> Application:
        res1 = self._api_client.request(
            "GET",
            "/api/v1/applications/{}".format(application_name),
            raise_for_status=True,
        )
        res2 = self._api_client.request(
            "GET",
            "/api/v1/applications/{}/schemas".format(application_name),
            raise_for_status=True,
        )

        return self._get_application(
            name=res1["data"]["func_name"],
            id=uuid.UUID(res1["data"]["versions"][0]["application_id"]),
            type=res2["data"]["model_type"],
        )

    @typechecked
    def archive_application(self, application_name: str) -> None:
        model_id = self.get_application(application_name)._id
        self._api_client.request(
            "DELETE",
            "/api/v1/applications/{}".format(model_id),
            raise_for_status=True,
        )

    @typechecked
    def delete_application(self, application_name: str) -> None:
        model_id = self.get_application(application_name)._id
        self._api_client.request(
            "POST",
            "/api/v1/applications/{}/hard_delete".format(model_id),
            raise_for_status=True,
        )

    def _get_application(self, name: str, id: uuid.UUID, type: Optional[str]) -> Application:
        if type == "Completion":
            return CompletionApplication(
                name=name,
                api_client=self._api_client,
                id=id,
            )
        elif type == "Custom":
            return Application(
                name=name,
                api_client=self._api_client,
                id=id,
            )
        else:
            return Application(
                name=name,
                api_client=self._api_client,
                id=id,
            )
