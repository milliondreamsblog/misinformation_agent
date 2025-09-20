"""
Lead Validator Agent

This agent is responsible for validating if a lead has all the necessary information
for qualification.
"""

from google.adk.agents import LlmAgent

# --- Constants ---
GEMINI_MODEL = "gemini-2.0-flash"

# Create the validator agent
lead_validator_agent = LlmAgent(
    name="LeadValidatorAgent",
    model=GEMINI_MODEL,
    instruction="""
    You are an AI specialized in detecting and evaluating potential misinformation.

    Your task is to carefully analyze the content provided by the user and determine:
    1. Whether the content is potentially misleading, false, or unverified.
    2. The reason behind your evaluation, citing clues, inconsistencies, or context.
    3. Provide a serious, actionable assessment that could guide the user to understand the credibility of the content.

    Output format (strictly):
    - 'valid' if content appears credible
    - 'invalid: [reason]' if content appears misleading or unverified

    Example valid output: 'valid'
    Example invalid output: 'invalid: lacks credible sources, contains exaggerated claims'

    Remember, your responses should be **precise, analytical, and useful for educating users** about misinformation.
    """,
    description="Validates information for credibility and misinformation potential.",
    output_key="validation_status",
)