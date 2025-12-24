import gradio as gr
from bug_fixer import fix_bug


def run_bug_fixer(code, error):
    """
    This function connects the UI to the bug fixing logic.
    For now, it just calls fix_bug().
    """
    return fix_bug(code, error)


interface = gr.Interface(
    fn=run_bug_fixer,
    inputs=[
        gr.Textbox(label="Buggy Python Code", lines=10),
        gr.Textbox(label="Error Message")
    ],
    outputs=gr.Textbox(label="AI Explanation & Fix"),
    title="AI Bug Fixer"
)

interface.launch()