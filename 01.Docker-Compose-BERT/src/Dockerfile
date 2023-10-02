FROM python:3.10-slim

WORKDIR /src
COPY requirements.txt /src
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install pymongo flask transformers torch==1.12.0+cpu -f https://download.pytorch.org/whl/torch_stable.html

COPY . .

ENV FLASK_APP app.py
ENV FLASK_RUN_PORT 8000
ENV FLASK_RUN_HOST 0.0.0.0

EXPOSE 8000

CMD ["flask","run"]