FROM nginx:alpine
COPY . /usr/share/nginx/html
RUN rm -f /usr/share/nginx/html/Dockerfile /usr/share/nginx/html/nginx.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
