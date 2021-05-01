FROM python:3.6


WORKDIR /app

RUN apt-get update -yqq && apt-get install apt-transport-https zip -yqq &&  apt-get upgrade -yqq

# Install Chrome WebDriver
#https://github.com/theserverlessway/pytest-chrome/blob/master/Dockerfile
#https://stackoverflow.com/a/55352993
RUN CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
    mkdir -p /opt/chromedriver-$CHROMEDRIVER_VERSION && \
    curl -sS -o /tmp/chromedriver_linux64.zip http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
    unzip -qq /tmp/chromedriver_linux64.zip -d /opt/chromedriver-$CHROMEDRIVER_VERSION && \
    rm /tmp/chromedriver_linux64.zip && \
    chmod +x /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver && \
    ln -fs /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver /usr/local/bin/chromedriver

# Install Google Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && echo "deb https://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
  && apt-get update -qqy \
  && apt-get -qqy install google-chrome-stable \
  && rm /etc/apt/sources.list.d/google-chrome.list \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

COPY requirements.txt .
# install dependencies
RUN pip install -U pip
RUN pip install -r requirements.txt

# copy all the files to the container
COPY . .

# tell the port number the container should expose
# docker run -p 80:80 --rm {IMAGE}
EXPOSE 80

# run the command
CMD ["bash", "python"]