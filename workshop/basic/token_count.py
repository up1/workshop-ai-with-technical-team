import tiktoken
def num_tokens_from_string(string: str, encoding_name: str) -> int:
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

print(num_tokens_from_string("I love you!", "cl100k_base"))
# "cl100k_base" encoding model used from OpenAI's GPT-3 model, GPT-3.5-turbo and GPT-4