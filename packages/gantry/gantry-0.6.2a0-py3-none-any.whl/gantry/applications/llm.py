import logging
import re
import uuid
from dataclasses import dataclass
from typing import List, Optional

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal  # type: ignore

from pydantic import BaseModel

from gantry.api_client import APIClient
from gantry.applications.core import Application

logger = logging.getLogger(__name__)


OPENAI_COMPLETION_MODELS = [
    "text-davinci-001",
    "text-davinci-002",
    "text-davinci-003",
    "text-curie-001",
    "text-babbage-001",
    "text-ada-001",
]


def _get_prompt_inputs(prompt: str) -> List[str]:
    return list(set(re.findall(r"\{\{([^\}\{]+)\}\}", prompt)))  # unique list


@dataclass(frozen=True)
class VersionDetails:
    config: dict
    description: str
    app_name: str
    version_id: uuid.UUID


class OpenAIParams(BaseModel):
    temperature: float = 1.0
    max_tokens: int = 16
    top_p: float = 1.0
    frequency_penalty: float = 0.0
    presence_penalty: float = 0.0


class CompletionApplication(Application):
    """
    A class representing a completion application.
    """

    def __init__(
        self,
        name: str,
        api_client: APIClient,
        id: Optional[uuid.UUID] = None,
        organization_id: Optional[uuid.UUID] = None,
    ):
        super().__init__(name, api_client, id, organization_id)
        self._configuration_name = f"default_{name}_configuration"
        # TODO: validate name

    def create_version(
        self,
        prompt_template: str,
        description: str,
        model: str,
        model_params: Optional[dict] = None,
    ) -> VersionDetails:
        if model not in OPENAI_COMPLETION_MODELS:
            raise ValueError(f"Invalid model '{model}'. Must be one of {OPENAI_COMPLETION_MODELS}")

        model_params = model_params or {}
        params = OpenAIParams(**model_params).dict()

        configuration_data = {
            "prompt": prompt_template,
            "prompt_inputs": _get_prompt_inputs(prompt_template),
            "model": model,
            "params": params,
        }

        res = self._api_client.request(
            "POST",
            f"/api/v1/cms/{self._name}/configurations/{self._configuration_name}/versions",
            json={
                "configuration_data": configuration_data,
                "description": description,
            },
            raise_for_status=True,
        )

        return VersionDetails(
            config=configuration_data,
            description=description,
            app_name=self._name,
            version_id=uuid.UUID(res["data"]["id"]),
        )

    def get_version(self, version: Literal["prod", "test", "latest"]) -> Optional[VersionDetails]:
        version_data: dict

        try:
            if version == "latest":
                # for latest version, we get a list of all versions and pick the most recent
                res = self._api_client.request(
                    "GET",
                    f"/api/v1/cms/{self._name}/configurations/{self._configuration_name}/versions",
                    raise_for_status=True,
                )
                version_data = res["data"][0]
            else:
                # for releases, we can get the latest release by environment
                res = self._api_client.request(
                    "GET",
                    f"/api/v1/cms/{self._name}/configurations/{self._configuration_name}/releases",
                    params={"latest": True, "env": version},
                    raise_for_status=True,
                )
                version_data = res["data"][0]["version"]
        except IndexError:
            logger.warn("No version found for '%s'", version)
            return None

        # now that we have the version, we can get the config data
        res = self._api_client.request(
            "GET",
            (
                f"/api/v1/cms/{self._name}/configurations/{self._configuration_name}"
                f"/versions/{version_data['id']}/data"
            ),
            raise_for_status=True,
        )
        config_data = res["data"][0]

        return VersionDetails(
            config=config_data,
            description=version_data["notes"],
            app_name=self._name,
            version_id=uuid.UUID(version_data["id"]),
        )
