# Why this file exists:
# Runs the Vite dev server in a container for local development, matching
# the backend's approach so `docker compose up` starts the whole stack with
# one command. A production multi-stage build (Vite build + Nginx) is
# intentionally left out for now - it belongs in the deployment/CI-CD
# feature work, not this skeleton.
FROM node:20-slim

WORKDIR /app

COPY package.json ./
RUN npm install

COPY . .

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
