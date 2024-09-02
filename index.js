const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());

// Basic GET route
app.get('/api/items', (req, res) => {
  res.json({ message: 'GET all items' });
});

// Basic POST route
app.post('/api/items', (req, res) => {
  const newItem = req.body;
  res.json({ message: 'POST new item', item: newItem });
});

// Basic PUT route
app.put('/api/items/:id', (req, res) => {
  const { id } = req.params;
  const updatedItem = req.body;
  res.json({ message: `PUT update item with id ${id}`, item: updatedItem });
});

// Basic DELETE route
app.delete('/api/items/:id', (req, res) => {
  const { id } = req.params;
  res.json({ message: `DELETE item with id ${id}` });
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
