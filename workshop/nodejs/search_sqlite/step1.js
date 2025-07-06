// 1. Load data from products.json
const fs = require('fs');
const path = require('path');

const productsFilePath = path.join(__dirname, 'products.json');
const products = JSON.parse(fs.readFileSync(productsFilePath, 'utf-8'));

// 2. Embedding data using OpenAI API
const { OpenAI } = require('openai');
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});
async function embedProducts(products) {
  const embeddings = await Promise.all(
    products.map(async (product) => {
      const response = await openai.embeddings.create({
        model: 'text-embedding-ada-002',
        input: product.name,
      });
      return {
        ...product,
        embedding: response.data[0].embedding,
      };
    })
  );
  return embeddings;
}

// 3. Save embeddings to products_with_embeddings.json
async function saveEmbeddings(embeddings) {
  const outputFilePath = path.join(__dirname, 'products_with_embeddings.json');
  fs.writeFileSync(outputFilePath, JSON.stringify(embeddings, null, 2));
}
async function main() {
  try {
    const embeddings = await embedProducts(products);
    await saveEmbeddings(embeddings);
    console.log('Embeddings saved to products_with_embeddings.json');
  } catch (error) {
    console.error('Error embedding products:', error);
  }
}
main();