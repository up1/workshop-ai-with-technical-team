import os
from google import genai
from google.genai import types


def generate():
  client = genai.Client(
      api_key=os.environ.get("GEMINI_API_KEY"),
  )

  files = [
      # Make the file available in local system working directory
      client.files.upload(file="./files/demo.mp3"),
  ]
  model = "gemini-2.0-flash"
  contents = [
      types.Content(
          role="user",
          parts=[
              types.Part.from_uri(
                  file_uri=files[0].uri,
                  mime_type=files[0].mime_type,
              ),
              types.Part.from_text(
                  text="""Extract the audio and convert it to text with thai language""",
              ),
          ],
      ),
  ]
  generate_content_config = types.GenerateContentConfig(
      temperature=1,
      top_p=0.95,
      top_k=40,
      max_output_tokens=8192,
      response_mime_type="text/plain",
  )

  for chunk in client.models.generate_content_stream(
      model=model,
      contents=contents,
      config=generate_content_config,
  ):
    print(chunk.text, end="")


generate()