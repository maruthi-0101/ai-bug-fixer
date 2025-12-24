from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load model and tokenizer once (this happens when the file is imported)
MODEL_NAME = "google/flan-t5-base"

tokenizer = T5Tokenizer.from_pretrained(MODEL_NAME)
model = T5ForConditionalGeneration.from_pretrained(MODEL_NAME)


def fix_bug(code: str, error: str) -> str:
    """
    Takes buggy Python code and its error message,
    sends them to the LLM, and returns an explanation + corrected code.
    """

    # Handle empty inputs
    if not code.strip():
        return "Please provide some Python code to analyze."
    
    # Handle missing error message
    error_section = f"Error Message:\n{error}" if error.strip() else "Error Message:\nNot provided - please analyze the code for potential bugs."

    # Build the prompt dynamically using user input
    prompt = f"""
You are an expert Python developer.

Explain the following error clearly.
Then provide corrected Python code.

Buggy Code:
{code}

{error_section}

Answer in this format ONLY:

Explanation:
<one or two sentences>

Corrected Code:
```python
# corrected code here
```
"""

    # Convert text prompt into tokens (numbers the model understands)
    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True
    )

    # Generate a response from the model
    outputs = model.generate(
        **inputs,
        max_new_tokens=200,
        do_sample=True,
        temperature=0.7,
        top_p=0.9
    )

    # Convert model output tokens back into readable text
    result = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return result