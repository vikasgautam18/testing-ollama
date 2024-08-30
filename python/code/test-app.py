import ollama, pydantic
import gradio as gr

# Function to invoke the LLM  
def invoke_llm(question, model):
    response = ollama.chat(model=model, messages=[
    {
        'role': 'user',
        'content': question,
    },
    ])

    #debug
    # print(response['message']['content'])
    
    return response['message']['content']

# Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown(
      """
      # Hallucination Detection Demo
      Upload a pdf document and ask any questions based on the document. 
      Use the buttons to answer the question and check if the answer is hallucinated or not.
      """)
    with gr.Row():
        with gr.Column():
            input_qn = gr.Textbox(label="Input Question")
            model = gr.Dropdown(
            ["llama3", "phi"], label="Model", info="Select a model to use")
            llm_res = gr.Textbox(label="LLM Response")
            with gr.Row():
                  h_button = gr.Button("Ask LLM")

    h_button.click(
      fn= invoke_llm,      
      inputs=[input_qn, model],  
      outputs=[llm_res]
    )

# Launch the demo application
demo.launch(share=True, 
            server_name="0.0.0.0",
            timeout=120
            )


