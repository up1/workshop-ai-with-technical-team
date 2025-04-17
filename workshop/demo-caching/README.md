# Demo of prompt caching
* [OpenAI](https://platform.openai.com/docs/guides/prompt-caching)

## 1. OpenAI Prompt Caching
* OpenAI's Prompt Caching automatically applies to prompts longer than 1,024 tokens
* Caching mechanism reduces costs and latency for repeated prompts
* Auto caching in api => [chat completion](https://platform.openai.com/docs/api-reference/chat/object)

```
$export OPENAI_API_KEY=<your key>
$python demo-openai.py

CompletionUsage(
    completion_tokens=428, 
    prompt_tokens=1154, 
    total_tokens=1582, 
    completion_tokens_details=CompletionTokensDetails(
        audio_tokens=0, reasoning_tokens=0, accepted_prediction_tokens=0, rejected_prediction_tokens=0), 
        prompt_tokens_details=PromptTokensDetails(
            audio_tokens=0, cached_tokens=1024))
```

## 2. Anthropic caching
* [Prompt caching (beta)](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)

```
$python demo-anthropic.py

usage=PromptCachingBetaUsage(
    cache_creation_input_tokens=0, 
    cache_read_input_tokens=2424, 
    input_tokens=15, 
    output_tokens=45)
```