import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, SystemMessage
import gradio as gr

load_dotenv()


username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
def generate_lyrics(description: str) -> str:
    system_message = f"""
    You are a professional music lyricist AI skilled in writing songs across multiple genres and moods.
    You receive the following theme/style from the user: "{description}" and you make a song based on that.

    Your Goals:

    Write creative, catchy, and meaningful song lyrics suitable for various styles (e.g., pop, R&B, hip-hop, Afrobeats, soul, EDM, rock, country).

    Adapt tone, language, and rhythm to fit the requested theme or genre.

    Explore universal themes like love, ambition, joy, heartbreak, self-discovery, resilience, and celebration.

    Use imagery, emotion, and storytelling to make the lyrics engaging and relatable.

    Optionally blend languages or dialects when fitting.

    Maintain a clear song structure that works for professional songwriting and performance.

    Output Format:
    [Title]
    [Intro]  
    [Chorus]  
    [Verse 1]  
    [Verse 2]  
    [Bridge / Outro]

    Deliver musically cohesive, lyrically expressive, and emotionally resonant lyrics ready to be sung or recorded.
    """
    
    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=description)
    ]
    
    llm = init_chat_model(model="gpt-5-nano", model_provider="OPENAI")
    response = llm.invoke(messages)
    return response.content

textbox = gr.Textbox(info="enter your song's theme/style")
textarea = gr.TextArea(label="Generated Lyrics",info="generated lyrics will apeare here")

gr.Interface(fn=generate_lyrics, inputs=textbox, outputs=textarea, 
             title="Song Generator",
            ).launch(share=True,auth=(username,password))
