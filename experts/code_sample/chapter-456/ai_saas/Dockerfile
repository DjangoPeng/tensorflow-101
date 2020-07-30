FROM tensorflow/tensorflow:2.2.0-gpu

ENV LC_ALL="C.UTF-8" LANG="C.UTF-8"
ENV PYTHONIOENCODING=utf-8

RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

RUN sed -i s/archive.ubuntu.com/mirrors.aliyun.com/g /etc/apt/sources.list && \
    sed -i s/security.ubuntu.com/mirrors.aliyun.com/g /etc/apt/sources.list && \
    apt-get update && apt-get install -y libsm6 libxext6 libxrender-dev wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install -i https://mirrors.aliyun.com/pypi/simple --upgrade pip

COPY ai_saas /opt/app/ai_saas

RUN pip install -i https://mirrors.aliyun.com/pypi/simple -r /opt/app/ai_saas/requirements.txt

COPY models /opt/app/models
COPY data/baijiu/class.csv /opt/app/data/baijiu/class.csv
COPY keras-retinanet /opt/app/keras-retinanet
COPY test opt/app/test

ENV PYTHONPATH=/opt/app/:${PYTHONPATH}

WORKDIR /opt/app/

RUN cd keras-retinanet && pip install . --user

EXPOSE 9000

CMD ["python3", "ai_saas/manage.py"]

# docker build -t tf2-ai-saas -f ai_saas/Dockerfile .
# docker run --runtime nvidia -it --rm --name tf2_ai_saas -p 9000:9000 tf2-ai-saas bash