FROM docker.io/node:16.15.0-alpine
ENV DEBIAN_FRONTEND noninteractive

LABEL org.opencontainers.image.title "Aleph document converters"
LABEL org.opencontainers.image.licenses MIT
LABEL org.opencontainers.image.source https://github.com/alephdata/convert-document

RUN apk --no-cache add bash libreoffice util-linux libreoffice-writer psmisc curl \
    ttf-droid-nonlatin ttf-droid ttf-dejavu ttf-freefont ttf-liberation \
    msttcorefonts-installer fontconfig \
    && update-ms-fonts \
    && fc-cache -f \
    && rm -rf /var/cache/apk/* /tmp/* /var/tmp/* \
    #&& apt-get -q -y dist-upgrade \
    #&& apt-get -q -y install locales libreoffice libreoffice-writer psmisc curl \
    #libreoffice-impress libreoffice-common  \
    #fonts-opensymbol hyphen-fr hyphen-de hyphen-en-us hyphen-it hyphen-ru \
    #fonts-droid-fallback fonts-dustin fonts-f500 fonts-fanwood fonts-freefont-ttf \
    #fonts-liberation fonts-lmodern fonts-lyx fonts-sil-gentium fonts-texgyre \
    #fonts-tlwg-purisa #
    #python3-pip python3-uno python3-lxml python3-icu unoconv \
    #&& apt-get -qq -y autoremove \
    #&& apk clean \
    && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8

ENV LANG='en_US.UTF-8'

RUN groupadd -g 1000 -r app \
    && useradd -m -u 1000 -d /tmp -s /bin/false -g app app

RUN mkdir -p /convert
WORKDIR /convert
COPY requirements.txt /convert
RUN pip3 install --no-cache-dir -q -r /convert/requirements.txt
COPY setup.py /convert/
COPY convert /convert/convert/
RUN pip3 install -q -e .

USER app

HEALTHCHECK --interval=10s --timeout=10s --retries=100 \
    CMD curl -f http://localhost:3000/health/live || exit 1

CMD ["gunicorn", \
    "-w", "4", \
    "--bind", "0.0.0.0:3000", \
    "--access-logfile", "-", \
    "--error-logfile", "-", \
    "--timeout", "84600", \
    "convert.app:app"]
