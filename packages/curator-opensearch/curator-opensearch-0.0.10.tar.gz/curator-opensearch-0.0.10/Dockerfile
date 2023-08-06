FROM python:3.7-buster as builder

# Add the community repo for access to patchelf binary package
#RUN echo 'https://dl-cdn.alpinelinux.org/alpine/v3.16/community/' >> /etc/apk/repositories
RUN apt update && apt install -y build-essential musl-tools musl-dev tar patchelf
# patchelf-wrapper is necessary now for cx_Freeze, but not for Curator itself.
RUN pip3 install cx-Freeze==6.10 patchelf-wrapper
#RUN pip3 install setuptools
RUN pip3 list

COPY . .
RUN ln -s /lib/libc.musl-x86_64.so.1 ldd
RUN ln -s /lib /lib64
RUN pip3 install -r requirements.txt
RUN python3 -m pip install build
RUN python3 -m build
# RUN python3 setup.py build_exe

#FROM alpine:3.17
#RUN apk --no-cache upgrade && apk --no-cache add openssl-dev expat
#COPY --from=builder build/exe.linux-x86_64-3.11 /curator/
#RUN mkdir /.curator

#USER nobody:nobody
#ENV LD_LIBRARY_PATH /curator/lib:$LD_LIBRARY_PATH
#ENTRYPOINT ["/curator/curator"]

