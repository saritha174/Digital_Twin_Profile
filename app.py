from groq import Groq
from context import TWIN_SYSTEM_PROMPT
from tools import tools, handle_tool_calls
from styles import CSS, JS, EXAMPLES
from dotenv import load_dotenv
import gradio as gr

# Load environment variables
load_dotenv(override=True)


# -------------------------------
# Groq Client
# -------------------------------

groq = Groq()


# -------------------------------
# Model
# -------------------------------

MODEL_NAME = "llama-3.3-70b-versatile"


# -------------------------------
# System Prompt
# -------------------------------

system = [
    {
        "role": "system",
        "content": TWIN_SYSTEM_PROMPT
    }
]


# -------------------------------
# Chat Function
# -------------------------------

def chat(message, history):

    messages = system + history + [
        {
            "role": "user",
            "content": message
        }
    ]

    response = groq.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    # -------------------------------
    # Handle Tool Calls
    # -------------------------------

    while response.choices[0].finish_reason == "tool_calls":

        assistant_message = response.choices[0].message

        tool_calls = assistant_message.tool_calls

        results = handle_tool_calls(tool_calls)

        messages.append(assistant_message)

        messages.extend(results)

        response = groq.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            tools=tools,
            tool_choice="auto"
        )

    # -------------------------------
    # Return Final Response
    # -------------------------------

    return response.choices[0].message.content


# -------------------------------
# Launch Gradio
# -------------------------------

if __name__ == "__main__":

    gr.ChatInterface(
        chat,
        examples=EXAMPLES,
        title="Digital Twin",
        description="Talk to my AI twin about my career",
        chatbot=gr.Chatbot(show_label=False),
    ).launch(
        css=CSS,
        js=JS,
        theme=gr.themes.Base()
    )
