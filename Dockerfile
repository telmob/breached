FROM alpine:edge

RUN apk add --update python3 ca-certificates py-requests && update-ca-certificates
COPY breached.py .
ENTRYPOINT ["python3","breached.py"]
CMD ["example@test.com"]