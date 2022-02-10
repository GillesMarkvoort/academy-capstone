FROM ... 
RUN useradd -ms /bin/bash pyspark-user
COPY /jars /repo
RUN pyspark --jars file1.jar,file2.jar