from openai import OpenAI

model = "gpt-4o"
client = OpenAI()
prompt = """
Generate object describing 10 users item using the following JSON structure:

{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "integer"
    },
    "name": {
      "type": "string"
    },
    "username": {
      "type": "string"
    },
    "email": {
      "type": "string"
    },
    "address": {
      "type": "object",
      "properties": {
        "street": {
          "type": "string"
        },
        "suite": {
          "type": "string"
        },
        "city": {
          "type": "string"
        },
        "zipcode": {
          "type": "string"
        },
        "geo": {
          "type": "object",
          "properties": {
            "lat": {
              "type": "string"
            },
            "lng": {
              "type": "string"
            }
          },
          "required": [
            "lat",
            "lng"
          ]
        }
      },
      "required": [
        "street",
        "suite",
        "city",
        "zipcode",
        "geo"
      ]
    },
    "phone": {
      "type": "string"
    },
    "website": {
      "type": "string"
    },
    "company": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "catchPhrase": {
          "type": "string"
        },
        "bs": {
          "type": "string"
        }
      },
      "required": [
        "name",
        "catchPhrase",
        "bs"
      ]
    }
  },
  "required": [
    "id",
    "name",
    "username",
    "email",
    "address",
    "phone",
    "website",
    "company"
  ]
}
"""

messages=[
    {
        "role": "user",
        "content": "Response must show only JSON data without additional text."
    },
    {
        "role": "user",
        "content": prompt,
    }
];

response = client.chat.completions.create(
    model=model,
    messages=messages
)

print(response.choices[0].message.content)