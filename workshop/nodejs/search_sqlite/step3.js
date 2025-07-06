// Connect DB
const { DatabaseSync } = require("node:sqlite");
const sqliteVec = require("sqlite-vec");

const db = new DatabaseSync("products.db", { allowExtension: true });
sqliteVec.load(db);

const { sqlite_version, vec_version } = db
  .prepare(
    "select sqlite_version() as sqlite_version, vec_version() as vec_version;",
  )
  .get();
console.log(`SQLite version: ${sqlite_version}, SQLite-Vec version: ${vec_version}`);

// Embedding search function
function searchProducts(query, limit = 5) {
  const searchStmt = db.prepare(`
    SELECT id, name, vec_distance_cosine(embedding, vec_f32(?)) AS score
    FROM products
    ORDER BY score ASC
    LIMIT ${limit}
  `);

  // Convert query to vector using OpenAI API
  const { OpenAI } = require('openai');
  const openai = new OpenAI({
    apiKey: process.env.OPENAI_API_KEY,
  });

  return openai.embeddings.create({
    model: 'text-embedding-ada-002',
    input: query,
  }).then(response => {
    const queryEmbedding = new Float32Array(response.data[0].embedding);
    
    // Execute the search statement with the query embedding
    return searchStmt.all(queryEmbedding);
  });
}

searchProducts("android", 5)
  .then(results => {
    console.log("Search Results:");
    results.forEach(result => {
      console.log(`ID: ${result.id}, Name: ${result.name}`, `Score: ${result.score}`);
    });
  })
  .catch(error => {
    console.error("Error during search:", error);
  }
  )
  .finally(() => {
    db.close();
  }
  );