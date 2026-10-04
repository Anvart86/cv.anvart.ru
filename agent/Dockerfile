FROM python:3.12-alpine
WORKDIR /app
COPY server.py .
RUN adduser -D -H agent && mkdir /data && chown agent /data
USER agent
ENV DB_PATH=/data/agent.db PORT=8080
EXPOSE 8080
CMD ["python3", "-u", "server.py"]
