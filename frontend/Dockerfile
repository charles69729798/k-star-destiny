# Build stage
FROM node:22-slim AS build-stage

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
# API URL은 빌드 시점에 주입하거나 Nginx 프록시를 통해 상대 경로로 처리 가능
ENV VITE_API_URL=/api
RUN npm run build

# Production stage
FROM nginx:stable-alpine

COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
