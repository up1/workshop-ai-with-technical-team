const { re } = require("mathjs");
const { OpenAI } = require("openai");

// Initialize OpenAI and Redis clients
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

async function sendPromptToOpenAI(products) {
  console.log(products);
    const prompt = `Here are some product suggestions for : ${products.map(p => `${p.name} for $${p.price}`).join(', ')}.`;
    
    const response = await openai.chat.completions.create({
      model: "gpt-4",
      messages: [
        {
          "role": "assistant",
          "content": [
            {
              "type": "text",
              "text": `
                You are a helpful assistant that recommends products to users. You should respond 3 products with short product name and price
              `
            }
          ]
        },
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": prompt
            }
          ]
        }
      ],
      max_tokens: 100,
    });
  
    return response;
  }

// Export
module.exports = sendPromptToOpenAI;
  