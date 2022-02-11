FROM public.ecr.aws/dataminded/spark-k8s-glue:v3.1.2-hadoop-3.3.1 

USER root
WORKDIR /repo
COPY requirements.txt /repo/

RUN pip install -r requirements.txt

USER 185

COPY cleaner.py upload.py /repo/

ENTRYPOINT [ "python3" ] 
CMD [ "upload.py" ]