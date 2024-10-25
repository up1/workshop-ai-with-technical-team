const readCSVFile = require("./read-file");
const createEmbeddingsAndStoreInRedis = require("./store-data");
const searchInRedis = require("./search");
const sendPromptToOpenAI = require("./prompt");
const { re } = require("mathjs");

const startProcess = async () => {
  // Step 1: Read the CSV file
//   const products = await readCSVFile("products.csv");

  // Step 2: Store embeddings in Redis
//   await createEmbeddingsAndStoreInRedis(products);

  // Step 3: Search for products in Redis
  const searchResults = await searchInRedis("Laptop");
  console.log(searchResults);

  // Step 4: Send product suggestions to OpenAI
  const response = await sendPromptToOpenAI(
    searchResults.map((result) => result.product)
  );
  console.log(response.choices[0].message.content);
  process.exit(0); 
};

startProcess();
