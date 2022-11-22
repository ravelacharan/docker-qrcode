FROM python:3.12.0a1-buster
RUN apt-get update &&\
    /usr/local/bin/python3 -m pip install --upgrade pip &&\
    /usr/local/bin/python3 -m pip install --upgrade setuptools &&\
    adduser script
ENV PATH="/home/script/.local/bin:${PATH}"
ENV QR_CODE_FILE_NAME="generated_qrcode.png"
ENV QR_CODE_FILE_PATH="generated_images"
ENV QR_CODE_DATA="https://hub.docker.com/repository/docker/charanravela54/qrcode"
WORKDIR /home/script
COPY --chown=script:script . .
RUN pip3 install -r requirements.txt
ENTRYPOINT ["runuser", "-u", "script", "--", "python3"]
CMD ["main.py"]
