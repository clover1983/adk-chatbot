from . import log_controller

from google.adk.agents import LlmAgent
from .litellm_config import base_model, base_generate_content_config
from google.adk.tools import load_memory

from .prompt import agent_instruction
from .tools.tools import get_current_date, mcp

from . import env_import


root_agent = LlmAgent(
    model=base_model,
    generate_content_config=base_generate_content_config,
    name="root_agent",
    instruction=agent_instruction,
    tools=[load_memory, get_current_date, mcp],
    # sub_agents=[xxx],
    # before_agent_callback=check_if_agent_should_run,
    # before_model_callback=simple_before_model_modifier,
    # before_tool_callback=simple_before_tool_modifier
)