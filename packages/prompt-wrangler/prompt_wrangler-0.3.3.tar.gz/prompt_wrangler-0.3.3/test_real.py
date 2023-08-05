from dotenv import load_dotenv

load_dotenv()

from prompt_wrangler import PromptWrangler, Prediction


def test_private_prompt():  # Use the fixtures in the function arguments
    pw = PromptWrangler()
    prompt = pw.prompt("ms-test/test-prompt")

    result = prompt.run(args={"input": "some input"})

    assert isinstance(result, Prediction)

    # Assert prediction exists
    assert result.prediction
