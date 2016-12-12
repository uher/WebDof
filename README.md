Setting Gudie.

1. zerorpc 설치. (Python에서 zerorpc를 사용하기 위함)
    1.1 zerorpc에 필요한 library먼저 설치.
      - autoconf, autoconf, libtool 사전 설치 필요 (하기 링크 참조).
       - http://munchpress.com/installing-autoconf-automake-libtool-on-mac-osx-mountain-lion/
     - libev
       - brew install libev (brew가 없으면 http://brew.sh/ 여기 참조하면되요.)
     - libzmq 설치
        - 설치 명령어
          $git clone https://github.com/zeromq/libzmq
          $cd libzq (이건 필요할수도있고 아닐수도있어요.)
          $./autogen.sh && ./configure && make -j 4
          $make check && make install && sudo ldconfig
        - 참조 싸이트: http://zeromq.org/intro:get-the-software

   1.2 사전 설치이후 zerorpc 설치
       - $pip install zerorpc

   1.3 1.1과 1.2가 잘 안될경우 시도해 볼 코드
       - $pip install pyzmq --install-option="--zmq=bundled"

    기타 참조 page:
    http://www.zerorpc.io/
    Nodejs 서버에서 zerorpc 사용 - https://github.com/0rpc/zerorpc-node
   https://ianhinsdale.com/post/communicating-between-nodejs-and-python/
   Python 서버에서 zerorpc 사용 - https://github.com/0rpc/zerorpc-python

실행하기
1. python server 실행하기. terminal 열어서 webdof 폴더이동후 아래 명령어 실행
  - $ python python/server.py
2. nodejs server 실행하기. terminal 새로 열어서 webdof 폴더에서 아래 명령어 실행
  - $ npm start (edited)

