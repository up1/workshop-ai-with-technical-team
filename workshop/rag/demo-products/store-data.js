const { OpenAI } = require("openai");
const redis = require("redis");

// Initialize OpenAI and Redis clients
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});
const redisClient = redis.createClient(
  process.env.REDIS_URL || "redis://localhost:6379"
);

async function createEmbeddingsAndStoreInRedis(products) {
  await redisClient.connect();
  for (const product of products) {
    const textToEmbed = `${product.name} ${product.price}`;
    const embeddingResponse = await openai.embeddings.create({
      model: "text-embedding-3-small",
      input: textToEmbed
    });

    const embedding = embeddingResponse.data[0].embedding;

    // Store the embedding in Redis with product ID as key
    console.log(`Storing embedding for product ID: ${product.id}`);
    await redisClient.set(product.id, JSON.stringify({ embedding, product }));
  }
}

redisClient.on("connect", () => {
  console.log("Connected to Redis");
});

// Export createEmbeddingsAndStoreInRedis
module.exports = createEmbeddingsAndStoreInRedis;
