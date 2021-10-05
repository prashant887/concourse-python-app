FROM python:3-alpine
RUN mkdir /src /test
COPY /src /src
COPY /test /test

CMD ["tail", "-f" ,"/dev/null"]