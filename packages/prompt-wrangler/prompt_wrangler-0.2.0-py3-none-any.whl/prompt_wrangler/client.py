import requests
from typing import Any, Dict, Optional


class PromptWrangler:
    """Prompt Wrangler client."""

    def __init__(self, api_key: str, workspace: str) -> None:
        """
        Initialize the PromptWrangler client.

        :param api_key: The API key for authentication.
        :param workspace: The workspace identifier.
        """
        self.api_key = api_key
        self.workspace = workspace
        self.base_url = "https://prompt-wrangler.com/api"

    def prompt(self, prompt_slug: str) -> "PromptWranglerPrompt":
        """
        Add a prompt to the PromptWrangler client.

        :param prompt_slug: The prompt slug.
        :return: A PromptWranglerPrompt instance.
        """
        return PromptWranglerPrompt(self, prompt_slug)


class PromptWranglerPrompt:
    def __init__(self, prompt_wrangler: PromptWrangler, prompt_slug: str) -> None:
        """
        Initialize a PromptWranglerPrompt.

        :param prompt_wrangler: The PromptWrangler client.
        :param prompt_slug: The prompt slug.
        """
        self.prompt_wrangler = prompt_wrangler
        self.prompt_slug = prompt_slug

    def run(self, args: Optional[Dict[str, Any]] = None) -> "Prediction":
        """
        Run the prompt and return a Prediction object.

        :param args: Optional dictionary of arguments to be passed to the API.
        :return: A Prediction instance.
        """
        headers = {
            "x-api-key": self.prompt_wrangler.api_key,
            "Content-Type": "application/json",
        }
        url = f"{self.prompt_wrangler.base_url}/{self.prompt_wrangler.workspace}/prompts/{self.prompt_slug}/predict"
        payload = {"args": args} if args else {}
        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            result = response.json()
            print(f"HELLO____ {result}")  # Add this line for debugging purposes

            return Prediction(result["prediction"])
        else:
            response.raise_for_status()


class Prediction:
    def __init__(self, prediction: Any) -> None:
        """
        Initialize a Prediction object.

        :param prediction: The prediction value.
        """
        self.prediction = prediction

    def __repr__(self) -> str:
        return f"Prediction(prediction={self.prediction})"
