FROM node:23-alpine3.20 AS build

WORKDIR /usr/src/app

COPY package*.json package-lock.json ./

# COPY --from=build /usr/src/app/dist /usr/share/nginx/html

RUN npm ci

COPY ./ ./

RUN npm run build
