from python:3.7

WORKDIR /home/coleman

COPY . /home/coleman

ENTRYPOINT ["python", "say_hey.py"]
CMD ["my friend"]
