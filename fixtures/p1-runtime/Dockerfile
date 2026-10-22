FROM python:3.12-alpine
COPY server.py /server.py
COPY release.txt /release.txt
USER 65534
EXPOSE 8080
CMD ["python", "-B", "/server.py"]
