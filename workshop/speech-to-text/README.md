# Demo with Speech to text
* OpenAI
* Gemini

## Step 0 :: Record your voice
* https://whisper-openai.vercel.app/
  * Save into file in `./files/demo.mp3`

## 1. [OpenAI with Whisper model](https://platform.openai.com/docs/guides/speech-to-text)

```
$export OPENAI_API_KEY=<your api key>
$python demo-openai.py
```

## 2. [Gemini 2.0 Flash](https://deepmind.google/technologies/gemini/flash/)
* Get key from [Google AI Studio](https://aistudio.google.com/)
* [Cookbook](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Audio.ipynb)

```
$export GEMINI_API_KEY=<your api key>
$demo-gemini.py
```

## 3. HuggingFace model
* https://huggingface.co/learn/audio-course/en/chapter5/demo

```
$pip install git+https://github.com/huggingface/speechbox
$python demo-huggingface.py
```
