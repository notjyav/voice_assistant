# Python Voice Assistant

<img width="1254" height="1254" alt="PyAssist" src="https://github.com/user-attachments/assets/801b6be4-fa0c-45f4-90b4-19cb0a1b633a" />

#

A simple, extensible voice assistant built in Python. It listens for spoken commands via your microphone, matches them to a set of "skills," and responds using text to speech.

It uses Google Web Speech API for listening, and offline text-to-speech for responses.

Current capabilities include Time telling, Jokes, Wikipedia Search, Music Search, and reminders - all of which are contained in the Skills folder.

New skills can be added as long as they're within the folder.

## How to Setup

**1. Install dependencies:**
```bash
pip3 install -r requirements.txt
```

**2. macOS only — microphone support requires PortAudio:**
```bash
brew install portaudio
pip3 install pyaudio
```

**3. Run it:**
```bash
python3 assistant.py
```

## Current Commands

| Command | What it does |

"What time is it?" = Speaks the current time

"Tell me a joke" = Tells a random joke

"What is ____? / "Who is ____?"	= Reads a short Wikipedia summary of topic

"Play _____"	= Opens a Spotify search for the song

"Remind me to ____ "	= Saves a new reminder

"List my reminders"	= Reads back all saved reminders

"Remove/Delete reminder ___" = Removes a specific reminder

"Clear my reminders"	= Deletes all saved reminders

"Exit" / "quit" / "stop"/ "End the Program" =	Ends the program

## Future of the Project

The project is still currently ongoing and future features are soon to be added.

The goal is to further expand the capabilities rather then have it be a simple voice assistance, I want to further refine the projects capabilites and transform it into a personalized assistant that would be able to assist in everyday tasks.
