import gradio as gr
from backend import RAGBackend
import config
import theme

# Inizializza backend
backend = RAGBackend()

def respond(file, query, history):
    if not query.strip():
        return history, ""

    # history è una lista di dict: {"role": "...", "content": "..."}
    history = history or []
    history.append({"role": "user", "content": query})
    # placeholder assistente per streaming
    history.append({"role": "assistant", "content": "…"})

    yield history, ""

    response_generator = backend.query(file, query)
    full_response = ""
    for chunk in response_generator:
        full_response = chunk
        history[-1] = {"role": "assistant", "content": full_response}
        yield history, ""

with gr.Blocks(theme=gr.themes.Base(), css=theme.WCAG_CSS, title=config.APP_TITLE) as demo:
    
    # HEADER
    gr.HTML(f"""
        <div class="header-container">
            <h1>{config.APP_TITLE}</h1>
            <p>{config.APP_SUBTITLE}</p>
        </div>
    """)
    
    with gr.Row():
        # COLONNA SINISTRA (Input)
        with gr.Column(scale=1, elem_classes="input-panel"):
            gr.Markdown("### 📂 Documento Sorgente", elem_id="src_title")
            file_input = gr.File(
                label="Carica PDF",
                file_types=[".pdf"],
                type="filepath"
            )
            gr.Markdown("""
            **Guida Rapida:**
            1. Carica un PDF (max 20MB)
            2. Attendi l'elaborazione
            3. Chiedi qualsiasi cosa in chat
            """, elem_id="quick_guide")
            
        # COLONNA DESTRA (Chat)
        with gr.Column(scale=2, elem_classes="chat-panel"):
            chatbot = gr.Chatbot(
                label="Conversazione",
                height=550,
                show_copy_button=True,
                avatar_images=(None, "🤖"),
                type="messages",
                elem_id="chatbot"
            )

            msg = gr.Textbox(
                show_label=False,
                placeholder="Scrivi la tua domanda qui...",
                scale=4,
                container=False,
                elem_id="msgbox"
            )

            submit = gr.Button("Invia ➢", variant="primary", scale=1, elem_id="btn-submit")
            clear  = gr.Button("🗑️ Cancella Chat", variant="secondary", elem_id="btn-clear")

    # LOGICA EVENTI
    # Submit con tasto o Enter
    gr.on(
        triggers=[submit.click, msg.submit],
        fn=respond,
        inputs=[file_input, msg, chatbot],
        outputs=[chatbot, msg]
    )
    
    # Clear
    clear.click(lambda: None, None, chatbot, queue=False)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
