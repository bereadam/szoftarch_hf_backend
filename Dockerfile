FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y libmysqlclient-dev
COPY requirements.pip requirements.pip
RUN pip install -r requirements.pip
EXPOSE 8000
ADD ./poi_project/ /poi_project
ADD ./entry.sh /poi_project/entry.sh
WORKDIR /poi_project
ENTRYPOINT ["/poi_project/entry.sh"]
