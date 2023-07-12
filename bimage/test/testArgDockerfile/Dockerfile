FROM continuumio/miniconda3:latest

ARG CAT

ENV env_name $CAT

COPY greetings.sh .

RUN chmod +x /greetings.sh

CMD ["/greetings.sh"]
