// 1. Read products_with_embeddings.json
const fs = require('fs');
const path = require('path');
const productsFilePath = path.join(__dirname, 'products_with_embeddings.json');
const productsWithEmbeddings = JSON.parse(fs.readFileSync(productsFilePath, 'utf-8'));

// 2. Create sqlite-vector database and table
const { DatabaseSync } = require("node:sqlite");
const sqliteVec = require("sqlite-vec");

const db = new DatabaseSync("products.db", { allowExtension: true });
sqliteVec.load(db);

db.exec(`
  CREATE TABLE IF NOT EXISTS products (
    id TEXT PRIMARY KEY,
    name TEXT,
    embedding VECTOR
  )
`);

// 3. Insert data into the products table
const insertStmt = db.prepare("INSERT INTO products (id, name, embedding) VALUES (?, ?, vec_f32(?))");
for (const product of productsWithEmbeddings) {
  // convert string to vector
  const embedding = product.embedding; // Ensure embedding is an array of numbers
  // Insert product data into the table
  insertStmt.run(product.id, product.name, new Float32Array(embedding));
}

// 4. Create vector index on the embedding column
db.exec(`
  CREATE INDEX IF NOT EXISTS idx_embedding ON products(embedding)
`);

db.close();


console.log('Database setup complete. You can now query the products table.');