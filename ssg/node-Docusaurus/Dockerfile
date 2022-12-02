FROM node:latest
# replace this with your application's default port
WORKDIR /app
COPY packag*.json ./
RUN npm install

COPY . .

CMD ["node", "server.js"]
EXPOSE 3000