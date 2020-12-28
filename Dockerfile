FROM python

WORKDIR /usr/src/app

COPY . .

RUN python ./test.py

CMD [ "python3", "./tested_progr.py" ]
