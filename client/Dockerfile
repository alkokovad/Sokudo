FROM node:latest as build
WORKDIR /usr/src/app
ADD *.json ./
RUN npm install -g npm@11.0.0
RUN yarn

ADD public ./public
ADD src ./src