from transformers import pipeline

model_id = "sanchit-gandhi/whisper-small-dv"  # update with your model id
pipe = pipeline("automatic-speech-recognition", model=model_id)
audio_file = "./files/demo.mp3"
transcription = pipe(audio_file)
print("Transcription: ")
print(transcription["text"])
print("Transcription completed successfully.")

def transcribe_speech(filepath):
    output = pipe(
        filepath,
        max_new_tokens=256,
        generate_kwargs={
            "task": "transcribe",
            "language": "thai",
        },  # update with the language you've fine-tuned on
        chunk_length_s=30,
        batch_size=8,
    )
    return output["text"]

transcription = transcribe_speech(audio_file)
print("Transcription with thai language: ")
print(transcription)
print("Transcription completed successfully.")