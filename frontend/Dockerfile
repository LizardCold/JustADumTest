FROM node:20.11.0-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY src/ ./src/
COPY public/ ./public/

EXPOSE 3000

CMD ["npm", "start"]
