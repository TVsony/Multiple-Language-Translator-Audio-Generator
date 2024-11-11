import streamlit as st
from mtranslate import translate  # Importing the translation library
import pandas as pd
import os
from gtts import gTTS  # Importing gTTS for text-to-speech
import base64  # For file encoding

# Step 1: Load the language dataset (language.csv)
df = pd.read_csv(r"language.csv")
df.dropna(inplace=True)  # Drop rows with missing values
lang = df['name'].to_list()  # List of languages
langlist = tuple(lang)  # Convert the language list to a tuple for easier access
langcode = df['iso'].to_list()  # List of corresponding ISO language codes

# Step 2: Create a dictionary to map language names to their respective language codes
lang_array = {lang[i]: langcode[i] for i in range(len(langcode))}

# Step 3: Streamlit Layout
st.title("Language Translation App")  # Display the title of the app
inputtext = st.text_area("Enter text to translate", height=100)  # Text area for user input

# Step 4: Sidebar to choose the language to translate to
choice = st.sidebar.radio('Select Language', langlist)

# Step 5: Dictionary for speech language mapping (ISO code to language name)
speech_langs = {
    "af": "Afrikaans", "ar": "Arabic", "bg": "Bulgarian", "bn": "Bengali",
    "bs": "Bosnian", "ca": "Catalan", "cs": "Czech", "cy": "Welsh",
    "da": "Danish", "de": "German", "el": "Greek", "en": "English",
    "eo": "Esperanto", "es": "Spanish", "et": "Estonian", "fi": "Finnish",
    "fr": "French", "gu": "Gujarati", "hi": "Hindi", "hr": "Croatian",
    "hu": "Hungarian", "hy": "Armenian", "id": "Indonesian", "it": "Italian",
    "ja": "Japanese", "jw": "Javanese", "km": "Khmer", "kn": "Kannada",
    "ko": "Korean", "la": "Latin", "lv": "Latvian", "mk": "Macedonian",
    "ml": "Malayalam", "mr": "Marathi", "my": "Burmese", "ne": "Nepali",
    "nl": "Dutch", "no": "Norwegian", "pl": "Polish", "pt": "Portuguese",
    "ro": "Romanian", "ru": "Russian", "si": "Sinhala", "sk": "Slovak",
    "sq": "Albanian", "sr": "Serbian", "su": "Sundanese", "sv": "Swedish",
    "sw": "Swahili", "ta": "Tamil", "te": "Telugu", "th": "Thai",
    "tl": "Filipino", "tr": "Turkish", "uk": "Ukrainian", "ur": "Urdu",
    "vi": "Vietnamese", "zh-CN": "Chinese"
}

# Function to generate a download link for audio file (MP3)
def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()  # Read the file
    bin_str = base64.b64encode(data).decode()  # Encode the file to base64
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href  # Return the HTML for file download link

# Layout columns for input and output display
c1, c2 = st.columns([4, 3])  # Create two columns for the input-output layout

# Step 6: Input handling and translation
if len(inputtext) > 0:
    try:
        # Translate the input text into the chosen language
        output = translate(inputtext, lang_array[choice])
        
        # Display the translated text in the left column
        with c1:
            st.text_area("Translated Text", output, height=200)
        
        # Step 7: Check if speech generation is supported for the chosen language
        if choice in speech_langs.values():
            with c2:
                # Generate speech from the translated text using gTTS
                aud_file = gTTS(text=output, lang=lang_array[choice], slow=False)
                aud_file.save("lang.mp3")  # Save the audio as 'lang.mp3'
                
                # Read the generated audio file
                audio_file_read = open('lang.mp3', 'rb')
                audio_bytes = audio_file_read.read()
                
                # Play the audio in the Streamlit app
                st.audio(audio_bytes, format='audio/mp3')
                
                # Provide a download link for the generated audio file
                st.markdown(get_binary_file_downloader_html("lang.mp3", 'Audio File'), unsafe_allow_html=True)
    
    except Exception as e:
        st.error(f"Error: {e}")  # Display error if anything goes wrong
