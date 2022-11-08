# FROM python:3.9
FROM public.ecr.aws/docker/library/python:3.9

RUN apt-get -y update && apt-get install -y --no-install-recommends wget nginx ca-certificates && rm -rf /var/lib/apt/lists/*


RUN python3 -m pip install --upgrade pip 

RUN pip3 install numpy scipy pandas tensorflow pydot scikit-learn matplotlib seaborn Pillow flask gevent gunicorn

ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/opt/program:${PATH}"

# Set up the program in the image
COPY ethnicity_prediction /opt/program
WORKDIR /opt/program
