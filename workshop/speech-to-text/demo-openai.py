from openai import OpenAI
client = OpenAI()

audio_file = open("./files/demo.mp3", "rb")
try:
    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file
    )
    print("Transcription: ")
    print(transcription.text)
    print("Transcription completed successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    audio_file.close()