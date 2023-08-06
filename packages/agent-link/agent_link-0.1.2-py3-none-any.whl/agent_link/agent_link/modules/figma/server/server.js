const express = require('express');
const cheerio = require('cheerio');
const axios = require('axios');
const cors = require('cors');
const app = express();
const port = 3000;

app.use(cors());

app.get('/parse', async (req, res) => {
    const url = req.query.url;
  
    try {
      const response = await axios.get(url);
      const html = response.data;
      const $ = cheerio.load(html);
  
      const elements = [];
  
      $('p, h1, h2, h3, h4, h5, h6, img').each((i, el) => {
        const tagName = el.tagName;
        const textContent = $(el).text();
        const src = $(el).attr('src');
        elements.push({ tagName, textContent, src });
      });
  
      res.json(elements);
    } catch (error) {
      console.error('Error fetching and parsing the URL:', error); // Log the error on the server
      res.status(500).json({ error: 'Failed to parse the URL' });
    }
  });
  

app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});
