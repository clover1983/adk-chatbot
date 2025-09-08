from google.adk.models.lite_llm import LiteLlm
import litellm
from google.genai import types

from . import env_import

# litellm.aiohttp_trust_env = True
litellm.disable_aiohttp_transport = True
# litellm.return_response_headers = True
litellm._turn_on_debug()
# litellm.json_logs = True


base_model=LiteLlm(
        # https://models.litellm.ai/
        # model="openai/claude-sonnet-4",
        model="openai/claude-sonnet-4",
        api_base="https://xxx",
        # Pass authentication headers if needed
        # extra_headers=auth_headers
        # Alternatively, if endpoint uses an API key:
        api_key=env_import.API_KEY,
        # input_cost_per_token="0.000003",
        # output_cost_per_token="0.000015",
        # # Rate Limit
        # rpm: xx,
        # mock_testing_fallbacks=True,
        # stream=True,
        # stream_options={"include_usage": True},
    )

base_generate_content_config=types.GenerateContentConfig(
        temperature=0.5,
        max_output_tokens=4096
    )