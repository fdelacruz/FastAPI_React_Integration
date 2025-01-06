FROM node:20-alpine3.20 AS build

WORKDIR /usr/src/app

COPY package*.json package-lock.json ./

RUN npm ci

COPY ./ ./

RUN npm run build
