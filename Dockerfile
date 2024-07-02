FROM kathara/base:latest

RUN curl -sS https://deb.troglobit.com/pubkey.gpg | apt-key add -
RUN echo "deb [arch=amd64] https://deb.troglobit.com/debian stable main" | tee /etc/apt/sources.list.d/troglobit.list
RUN apt-get update && apt-get install nemesis
