from openai import OpenAI
import gradio as gr
from dotenv import load_dotenv
import os

# ✅ Load .env file and get API key securely
load_dotenv()
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

# 🔧 Gemini model setup using OpenAI-compatible wrapper
gemini_model = OpenAI(
    api_key=GEMINI_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# 📱 Mobile Assistant Function
def mobile_assistant(query):
    prompt = [
        {
            "role": "system",
            "content": (
                "You are a mobile assistant for Indian users. "
                "When a user types a mobile phone name, return the following details:\n\n"
                "- 📱 Mobile Name\n"
                "- 💰 Price in India (₹)\n"
                "- ⚙️ Processor Name\n"
                "- 🌟 Key Features\n"
                "- 📸 Camera Lens Details (Rear & Front)\n"
                "- 🔄 Year or Month of Latest Update (if known)\n\n"
                "Reply clearly and simply."
            )
        },
        {
            "role": "user",
            "content": query
        }
    ]

    try:
        response = gemini_model.chat.completions.create(
            model="gemini-2.5-flash",
            messages=prompt
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error: {str(e)}"

# 🌐 Gradio UI
ui = gr.Interface(
    fn=mobile_assistant,
    inputs=gr.Textbox(placeholder="e.g. iPhone 15 Pro Max, Realme Narzo 70x"),
    outputs=gr.Textbox(label="📱 Mobile Details", lines=12),
    title="📱 Mobile Guru – Assistant for Indian Users",
    description="Enter any mobile name to get full details like price in India, processor, features, camera, and launch info.",
    theme="soft"
)

# 🚀 Launch App
if __name__ == "__main__":
    ui.launch()
