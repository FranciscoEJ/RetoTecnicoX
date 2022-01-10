# This image does not particularly care what OS runs underneath
FROM node:14-slim
# Create the directory and instruct Docker to operate
WORKDIR /user/src/app
# Copy the requirements file
COPY ./package.json ./
# Copy the lock file in order to install dependencies
COPY ./yarn.lock ./
# Install Node dependencies
RUN npm install
# Copy the rest of the codebase into the image
COPY . .
# Expose port
EXPOSE 3000
# Set up the entry point
ENTRYPOINT [ "npm" ]
# Finally start the server
CMD ["start"]