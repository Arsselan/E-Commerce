# Use the official Node.js image as a base image
FROM node:14

# Set the working directory to /app
WORKDIR /app

# Make sure that the container runs properly
HEALTHCHECK --interval=5m --timeout=3s \
  CMD curl -f https://localhost:8080/ || exit 1

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install project dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Expose the default port for Vue.js applications
EXPOSE 8080

# Start the application as the root user
CMD ["npm", "run", "serve"]
