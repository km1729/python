FROM node:16-alpine3.11
COPY hellojs.js /
CMD ["node", "/hellojs.js"]

# # bash install
# RUN apk add bash

# # Set the timezone in docker
# RUN apk --no-cache add tzdata && \
#         cp /usr/share/zoneinfo/Australia/Melbourne /etc/localtime && \
#         echo "Australia/Melbourne" > /etc/timezone

# # Create Directory for the Container
# WORKDIR /app

# # Only copy the package.json file to work directory
# #COPY package.json .
# RUN npm install

# # Docker Demon Port Mapping
# EXPOSE 3000

# # Node ENV
# ENV NODE_ENV=production