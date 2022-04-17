参考 https://github.com/AifiHenryMa/zeromq_protocolbuffer_demo

运行设备 ubuntu20.04

# libzmq build
```
mkdir cmake-build && cd cmake-build
cmake .. && make -j4
sudo apt  install cmake
cmake .. && make -j4
make test && make install && sudo ldconfig
sudo make test && sudo make install && sudo ldconfig
```

# protobuf build

1. protobuf 编译安装前配置
```
sudo apt-get install autoconf automake libtool curl make g++ unzip
git clone https://github.com/protocolbuffers/protobuf.git
cd protobuf
git submodule update --init --recursive
./autogen.sh

```
2. 为了构建和安装c++protobuf运行时和protobuf编译器(protoc)，执行以下命令:
```
 ./configure
 make -j$(nproc) # $(nproc) ensures it uses all cores for compilation
 make check
 sudo make install
 sudo ldconfig # refresh shared library cache.
```
如果“make check”失败，您仍然可以安装，但是这个库的一些特性很可能在您的系统上不能正常工作。继续进行，风险自负。
有关configure和make的高级用法信息，请参阅autoconf文档:
http://www.gnu.org/software/autoconf/manual/autoconf.html#Running-configure-Scripts
3. 安装位置提示
默认情况下，该包将被安装到/usr/local。然而，在许多平台上，/usr/local/lib不是LD_LIBRARY_PATH的一部分。您可以添加它，但只安装到/usr可能更容易。为此，调用configure，如下所示:
```
./configure --prefix=/usr
```
如果您已经用不同的前缀构建了包，请确保在再次构建之前运行“make clean”。
4. 编译依赖包
要编译使用Protocol Buffers的包，需要将各种标志传递给编译器和链接器。从2.2.0版本开始，Protocol Buffers集成了pkg-config来管理这一功能。如果你已经安装了pkg-config，那么你可以调用它来获得如下的标志列表:
```
pkg-config --cflags protobuf         # print compiler flags
pkg-config --libs protobuf           # print linker flags
pkg-config --cflags --libs protobuf  # print both
```
# build demo
```
cd build
cmake ..
make -j4
```
# run demo 

/Client 
Connect to server success...
Type:client	IP:192.168.1.100	Port:5555
Type:server	IP:192.168.1.100	Port:5555
Type:client	IP:192.168.1.100	Port:5555


./Server 
Type:client	IP:192.168.1.100	Port:5555
Type:server	IP:192.168.1.100	Port:5555
Type:client	IP:192.168.1.100	Port:5555
Type:server	IP:192.168.1.100	Port:5555

