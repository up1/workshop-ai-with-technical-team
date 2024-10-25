const fs = require('fs').promises;
const csv = require('csv-parser');
const { Readable } = require('stream');

async function readCSVFile(filePath) {
  const products = [];

  try {
    const fileContent = await fs.readFile(filePath, 'utf8');
    const stream = Readable.from(fileContent);

    await new Promise((resolve, reject) => {
      stream
        .pipe(csv())
        .on('data', (row) => {
          products.push(row);
        })
        .on('end', () => {
          console.log('CSV file successfully processed');
          resolve();
        })
        .on('error', reject);
    });

    // proceed with processing the data, like creating embeddings
  } catch (error) {
    console.error('Error reading the CSV file:', error);
  }

  return products;
}

// readCSVFile('products.csv');

// Exporrt
module.exports = readCSVFile;