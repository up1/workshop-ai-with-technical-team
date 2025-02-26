# DEmo with Speech to text
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

## 2. [HuggingFace model]
* https://huggingface.co/learn/audio-course/en/chapter5/demo

```
$pip install git+https://github.com/huggingface/speechbox
$python demo-huggingface.py
```

## 3. Gemini
* Get key from [Google AI Studio](https://aistudio.google.com/)

```
$export GEMINI_API_KEY=<your api key>
$demo-vertex.py
```