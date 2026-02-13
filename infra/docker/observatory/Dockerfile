FROM node:20-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

RUN npm install -g vite @vitejs/plugin-react

COPY observatory_app.js .
COPY package.json .

RUN npm install

EXPOSE 5173

CMD ["node", "observatory_app.js"]
