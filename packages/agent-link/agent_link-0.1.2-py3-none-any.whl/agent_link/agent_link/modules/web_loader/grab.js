const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

async function screenshotWebsite(url, outputFolder) {
  try {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto(url, { waitUntil: 'networkidle2' });
    await page.setViewport({ width: 1280, height: 800 });

    const body = await page.$('body');
    const bounding_box = await body.boundingBox();
    const screenshotOptions = {
      path: path.join(outputFolder, 'image.png'),
      clip: {
        x: bounding_box.x,
        y: bounding_box.y,
        width: Math.min(bounding_box.width, page.viewport().width),
        height: bounding_box.height,
      },
    };

    await page.screenshot(screenshotOptions);
    await browser.close();
    console.log(`Long screenshot saved as ${screenshotOptions.path}`);
  } catch (error) {
    console.error(`Error taking screenshot: ${error}`);
  }
}

if (process.argv.length < 3) {
  console.log('Usage: node screenshot.js <website_url>');
  process.exit(1);
}

const websiteUrl = process.argv[2];
const parsedUrl = new URL(websiteUrl);
const outputFolder = path.join('gen', 'image', parsedUrl.hostname);
fs.mkdirSync(outputFolder, { recursive: true });

screenshotWebsite(websiteUrl, outputFolder);
