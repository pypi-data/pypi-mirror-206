figma.showUI(__html__, { width: 400, height: 150 });

figma.ui.onmessage = async (msg) => {
  if (msg.type === "convert-website") {
    const url = msg.url;
    const encodedUrl = encodeURIComponent(url);

    try {
      // Replace "localhost:3000" with your actual server URL if it's not running locally
      const response = await fetch(`http://localhost:3000/parse?url=${encodedUrl}`);
      const elements = await response.json();

      for (const element of elements) {
        let node;

        if (element.tagName === 'img') {
          const imageData = await fetch(element.src);
          const imageBuffer = await imageData.arrayBuffer();
          const imageUint8Array = new Uint8Array(imageBuffer);
          const imageHash = figma.createImage(imageUint8Array).hash;
          node = figma.createRectangle();
          node.resize(200, 200);
          node.fills = [{ type: "IMAGE", scaleMode: "FILL", imageHash }];
        } else {
          node = figma.createText();
          node.characters = element.textContent;
        }

        figma.currentPage.appendChild(node);
      }

      figma.closePlugin();
    } catch (error) {
      console.error(error);
      figma.closePlugin("Failed to convert website. Please check the URL and try again.");
    }
  }
};
