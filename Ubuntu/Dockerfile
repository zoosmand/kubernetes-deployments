FROM ubuntu

ARG IMAGE_NAME=ServerTemplateForAllPurposes
ARG IMAGE_VER=0.0.1

EXPOSE 80 443

LABEL name=${IMAGE_NAME}
LABEL version=${IMAGE_VER}

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Yekaterinburg

RUN apt-get update && apt-get install -y \
    ssh-tools \
    curl \
    apt-utils \
    net-tools \
    wget \
    iputils-ping \
    tcpdump \
    zip \
    htop \
    iotop \
    tzdata \
    iproute2 \
    dnsutils \
    \
    && apt-get clean

COPY ./files/run.sh /opt
RUN chmod +x /opt/run.sh

WORKDIR /opt

ENTRYPOINT [ "./run.sh" ]

# ENTRYPOINT ["tail"]
# CMD ["-f","/dev/null"]
