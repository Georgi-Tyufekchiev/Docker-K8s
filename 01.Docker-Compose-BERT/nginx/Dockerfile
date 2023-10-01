FROM nginx:1.25-alpine
COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ../src/templates/index.html /usr/share/nginx/html/
COPY ../src/static/styling.css /usr/share/nginx/html/