import streamlit as st
from dotenv import load_dotenv
from gtts import gTTS
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
import tempfile
import io

load_dotenv()  # Load all the environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = """You are a YouTube video summarizer. You will be taking the transcript text
and summarizing the entire video and providing the important summary in points
within 250 words. Please provide the summary of the text given here:  """

## Getting the transcript data from YouTube videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]

        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except Exception as e:
        raise e


## Getting the summary based on the prompt from Google Gemini Pro
def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text


## Generate the answer based on the user's question and summary
def generate_answer_from_summary(question, summary):
    question_prompt = f"""You are an AI assistant. Based on the following video summary, answer the user's question clearly and concisely:

    Summary:
    {summary}

    User's Question: {question}

    Answer:"""

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(question_prompt)
    return response.text


## Convert the summary text to speech using gTTS
def convert_text_to_speech(text):
    tts = gTTS(text, lang='en')
    # Saving the audio file in a temporary file
    temp_audio_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_audio_file.name)
    
    # Open the file in binary mode
    with open(temp_audio_file.name, "rb") as f:
        audio_data = f.read()

    # Return audio data so it can be used in Streamlit
    return audio_data


st.title("YouTube Transcript to Detailed Notes Converter")
youtube_link = st.text_input("Enter YouTube Video Link:")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_container_width=True)

# Ensure the summary and answer persist
if "summary" not in st.session_state:
    st.session_state.summary = ""

if "answer" not in st.session_state:
    st.session_state.answer = ""

if st.button("Get Detailed Notes"):
    transcript_text = extract_transcript_details(youtube_link)

    if transcript_text:
        summary = generate_gemini_content(transcript_text, prompt)
        st.session_state.summary = summary  # Store the summary in session state
        st.markdown("## Detailed Notes:")
        st.write(summary)

# Display question box and answer button if the summary exists
if st.session_state.summary:
    user_question = st.text_input("Ask a question based on the generated summary:")

    if user_question:
        if st.button("Get Answer"):
            answer = generate_answer_from_summary(user_question, st.session_state.summary)
            st.session_state.answer = answer  # Store the answer in session state
            st.markdown("## Answer to Your Question:")
            st.write(answer)

    # Add button to convert summary to speech
    if st.button("Convert Summary to Speech"):
        if st.session_state.summary:
            audio_data = convert_text_to_speech(st.session_state.summary)
            st.markdown("## Listen to the Summary:")
            st.audio(audio_data, format="audio/mp3")
