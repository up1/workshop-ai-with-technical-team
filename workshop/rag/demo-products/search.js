const math = require("mathjs");
const { OpenAI } = require("openai");
const redis = require("redis");

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});
const redisClient = redis.createClient(
  process.env.REDIS_URL || "redis://localhost:6379"
);
async function searchInRedis(query) {
  await redisClient.connect();
  // Get embedding for the query
  const queryEmbeddingResponse = await openai.embeddings.create({
    model: "text-embedding-3-small",
    input: query,
  });

  const queryEmbedding = queryEmbeddingResponse.data[0].embedding;

  // Search for products in Redis
  try {
    console.log("Searching in Redis");
    const keys = await redisClient.keys("*");

    let searchResults = [];

    for (const key of keys) {
      const productData = await redisClient.get(key);
      const { embedding, product } = JSON.parse(productData);

      // Calculate cosine similarity
      const similarity =
        math.dot(queryEmbedding, embedding) /
        (math.norm(queryEmbedding) * math.norm(embedding));

      // You can set a similarity threshold to filter relevant products
      if (similarity > 0.6) {
        searchResults.push({ product, similarity });
        console.log(product, similarity);
      }
    }

    // Sort by similarity and return top results
    searchResults.sort((a, b) => b.similarity - a.similarity);
    return searchResults;
  } catch (err) {
    console.error("Error searching in Redis:", err);
    throw err;
  }
}

redisClient.on("connect", () => {
  console.log("Connected to Redis");
});

// Export
module.exports = searchInRedis;
