import requests
from typing import Any, Dict, Optional
import os


class APIException(Exception):
    def __init__(self, response):
        self.status_code = response.status_code
        self.reason = response.reason
        self.text = response.text
        super().__init__(
            f"Status code: {self.status_code}, Reason: {self.reason}, Response body: {self.text}"
        )


def make_request(url, method="GET", headers=None, params=None, data=None):
    if method.upper() == "GET":
        response = requests.get(url, headers=headers, params=params)
    elif method.upper() == "POST":
        response = requests.post(url, headers=headers, params=params, json=data)
    else:
        raise ValueError(f"Unsupported method: {method}")

    if response.status_code == 200:
        result = response.json()
        return Prediction(result["prediction"])
    else:
        # Print response details
        print(
            f"Status code: {response.status_code}, Reason: {response.reason}, Response body: {response.text}"
        )

        # Raise custom exception with response details
        raise APIException(response)


class PromptWrangler:
    """Prompt Wrangler client."""

    def __init__(self, base_url: str = "https://prompt-wrangler.com/api") -> None:
        """
        Initialize the PromptWrangler client.

        :param workspace: The workspace identifier.
        """

        self.base_url = base_url

        # Confirm that either PROMPT_WRANGLER_API_KEY exists or OPENAI_API_KEY exists
        self.prompt_wrangler_api_key = os.getenv("PROMPT_WRANGLER_API_KEY")
        self.openai_api_key = os.getenv("OPENAI_API_KEY")

        # Print env
        if self.prompt_wrangler_api_key is None and self.openai_api_key is None:
            raise Exception(
                "Prompt Wrangler API key not found. Please set environemnt variable PROMPT_WRANGLER_API_KEY or OPENAI_API_KEY."
            )

    def prompt(self, prompt_path: str) -> "PromptWranglerPrompt":
        """
        Add a prompt to the PromptWrangler client.

        :param prompt_path: The page to the prompt - workspace/prompt-slug.
        :return: A PromptWranglerPrompt instance.
        """
        return PromptWranglerPrompt(self, prompt_path)


class PromptWranglerPrompt:
    def __init__(self, prompt_wrangler: PromptWrangler, prompt_path: str) -> None:
        """
        Initialize a PromptWranglerPrompt.

        :param prompt_wrangler: The PromptWrangler client.
        :param prompt_slug: The prompt slug.
        """
        self.prompt_wrangler = prompt_wrangler
        self.prompt_path = prompt_path

    def run(self, args: Optional[Dict[str, Any]] = None) -> "Prediction":
        """
        Run the prompt and return a Prediction object.

        :param args: Optional dictionary of arguments to be passed to the API.
        :return: A Prediction instance.
        """
        headers = {
            "Content-Type": "application/json",
        }

        if self.prompt_wrangler.prompt_wrangler_api_key:
            headers["x-api-key"] = self.prompt_wrangler.prompt_wrangler_api_key

        if self.prompt_wrangler.openai_api_key:
            headers["x-openai-api-key"] = self.prompt_wrangler.openai_api_key

        url = f"{self.prompt_wrangler.base_url}/predict/{self.prompt_path}"
        payload = {"args": args} if args else {}
        response = make_request(url, method="POST", headers=headers, data=payload)
        return response


class Prediction:
    def __init__(self, prediction: Any) -> None:
        """
        Initialize a Prediction object.

        :param prediction: The prediction value.
        """
        self.prediction = prediction

    def __repr__(self) -> str:
        return f"Prediction(prediction={self.prediction})"
