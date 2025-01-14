FROM node:23-alpine3.20 

WORKDIR /usr/src/app

COPY package*.json package-lock.json ./

RUN npm ci

COPY ./ ./

# Default command for development
CMD ["npm", "run", "dev"]
