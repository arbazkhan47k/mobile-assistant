import gradio as gr
import google.generativeai as genai

# 🔐 Gemini API Key
genai.configure(api_key="AIzaSyB2d9IkC5uUUC3-BJ0_9hx_HXRIngE5QLk")

# 📱 Mobile Assistant Function
def mobile_assistant(query):
    model = genai.GenerativeModel("gemini-pro")
    try:
        response = model.generate_content(query)
        return response.text.strip()
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
