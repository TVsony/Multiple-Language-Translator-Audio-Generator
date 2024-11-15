# Multiple Language Translator & Audio Generator

## Problem Statement

In today's globalized world, communication across languages is crucial for individuals and businesses. However, language barriers often pose challenges to effective communication. To address this, the **Multiple Language Translator & Audio Generator** project aims to provide an intuitive and versatile solution for real-time translation across various languages and generating audio outputs from text in the target language.

This project is a multi-functional tool that enables users to:
- Translate text from one language to another in real-time.
- Convert the translated text into speech/audio, making it accessible for a wide range of users.

## Goal

The primary goal of this project is to develop a web-based application that:
1. Provides seamless translation between multiple languages.
2. Generates audio output from the translated text, enabling users to hear the translation in real time.
3. Offers an intuitive and easy-to-use interface.

## Approach

The approach to building this project involves several stages:

1. **Text Translation**: 
   - Use the **mtranslate** library to provide real-time translation services across multiple languages.
   - Enable translation between a variety of languages such as English, French, Spanish, German, and more.
   
2. **Text-to-Speech Conversion**:
   - Use the **Google Text-to-Speech (gTTS)** library to convert the translated text into speech in the selected language.
   - Allow users to download the generated audio in MP3 format.

3. **Web Interface**:
   - Build a user-friendly interface using **Streamlit** to allow users to input text, select languages, and interact with the translation and audio generation features.

4. **Real-Time Interaction**:
   - Ensure that the translation and audio generation happen in real time, providing a seamless experience for the user.

## Features

- **Multi-language support**: Translate text across a wide range of languages.
- **Audio Generation**: Convert the translated text into audio (MP3 format).
- **Language Selection**: Select the source and target languages easily from a dropdown menu.
- **Instant Translation**: Get the translation in real time as you type.
- **Text-to-Speech**: Listen to the translation in the desired language using high-quality TTS (Text-to-Speech) technology.
- **Download Audio**: Download the generated audio in MP3 format.
- **User-friendly UI**: Interactive and responsive user interface built with Streamlit.

## Challenges

- **Language Coverage**: Handling translations for a wide variety of languages, including complex ones, can be challenging due to nuances in grammar, syntax, and context.
- **Audio Quality**: Ensuring that the audio generated by the Text-to-Speech (TTS) engine is clear and accurate in all supported languages.
- **Real-time Processing**: Maintaining the performance and responsiveness of the app while processing translation and generating audio in real-time.
- **Error Handling**: Managing network issues, translation errors, and invalid input gracefully.
  
## How It Works

1. **Input Text**: The user enters the text they want to translate into the text box.
2. **Language Selection**: The user selects the source language (the language of the text) and the target language (the language to which the text will be translated).
3. **Text Translation**: The application uses the `mtranslate` library to fetch the translation of the input text into the target language.
4. **Text-to-Speech**: Once the translation is ready, the translated text is passed to the `gTTS` library to generate an audio file.
5. **Audio Output**: The generated audio file is provided to the user, who can listen to it within the app or download it as an MP3 file.

## Technology Used

- **Python**: Programming language used for backend development.
- **Streamlit**: Framework for creating the interactive web application.
- **mtranslate**: Library for translating text between languages.
- **gTTS (Google Text-to-Speech)**: Library for converting text into speech.
- **pandas**: For handling and processing any tabular data if needed.
- **HTML/CSS**: For styling the web application interface.
  
## Installation

### Prerequisites

Ensure that you have the following installed:
- **Python 3.10: This project requires Python 3.10 or higher.
- **pip**: Python's package installer.

### Step-by-Step Installation

1. Clone the repository:
2. lang_translation.py : https://github.com/TVsony/Multiple-Language-Translator-Audio-Generator/blob/main/lang_translation.py

3. Create and activate a virtual environment:

conda create -p venv python==3.10 -y

conda activate venv/

3. Install required dependencies:

pip install -r requirements.txt

4. Run the Streamlit application:

streamlit run lang_translation.py

# WEB API 
<img width="1015" alt="image" src="https://github.com/user-attachments/assets/7c7c7212-ec98-452f-b4ed-e6e9615e4d00">


### Enter the text and press ctrl + Enter 

<img width="946" alt="image-1" src="https://github.com/user-attachments/assets/77c51662-1d89-4f1c-9742-b9d3057ed4a5">


#### Select the language and you will get translation as well as audio too 

<img width="930" alt="image-2" src="https://github.com/user-attachments/assets/291045ac-1d51-4306-b4b8-91cc0f4f9855">

# Project Structure

<img width="503" alt="image-3" src="https://github.com/user-attachments/assets/7d6060fd-386f-4b53-b892-b0a809a53399">



### Explanation:

- **Problem Statement**: Describes the purpose of the project.
- **Goal**: Outlines the objectives of the project.
- **Approach**: Provides a high-level overview of how the project is structured and the steps involved.
- **Features**: Lists the major functionalities of the project.
- **Challenges**: Highlights some of the key issues faced during development.
- **How It Works**: Describes the user flow and how the translation and audio generation process works step-by-step.
- **Technology Used**: Lists the technologies and libraries employed in the project.
- **Installation**: Provides a detailed guide to install and run the project.
- **Project Structure**: Shows the folder structure of the project.
- **Other Details**: Contains information like licensing and contribution guidelines.
  
Let me know if you need further modifications or additions!
