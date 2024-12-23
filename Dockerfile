FROM node:18-alpine as build
WORKDIR /usr/src/app
ADD *.json ./
RUN npm install

ADD client/public ./public
ADD client/src ./src