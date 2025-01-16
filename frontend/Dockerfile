FROM node:23-alpine3.21 

WORKDIR /usr/src/app

COPY package*.json package-lock.json ./

RUN npm ci

COPY ./ ./

# Default command for development
CMD ["npm", "run", "dev"]
