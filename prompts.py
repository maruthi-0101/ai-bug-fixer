# prompts.py
"""
Prompt Templates.

Purpose:
- Store reusable prompt templates for the LLM
- Can be imported into bug_fixer.py for cleaner code

Note: Currently, prompts are defined inline in bug_fixer.py.
This file is reserved for future refactoring when adding more features.
"""

# Example template (for future use):
SYSTEM_PROMPT = "You are an expert Python developer who helps fix bugs."

BUG_FIX_TEMPLATE = """
Explain the following error clearly.
Then provide corrected Python code.

Buggy Code:
{code}

Error Message:
{error}
"""
