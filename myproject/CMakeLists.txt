# set minimum cmake version
cmake_minimum_required(VERSION 3.5 FATAL_ERROR)

# project name and language
project(zeromqProtocolBufferDemo LANGUAGES CXX)

set(INCLUDE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/)
message(${INCLUDE_DIR})
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

SET(SRC_CLIENT_LIST client.cpp)
SET(SRC_SERVER_LIST server.cpp)

SET(BROKER_CLIENT_LIST rrclient.cpp)

SET(BROKER_BROKER_LIST rrbroker.cpp)

SET(BROKER_WORKER_LIST rrworker.cpp)

find_package(PkgConfig REQUIRED QUIET)

pkg_search_module(
  ZeroMQ
  REQUIRED
    libzeromq libzmq lib0mq
  IMPORTED_TARGET
  )

if(TARGET PkgConfig::ZeroMQ)
  message(STATUS "Found ZeroMQ")
else()
  message(FATAL_ERROR "Cannot find Protobuf")
endif ()

find_package(Protobuf REQUIRED)
if (PROTOBUF_FOUND)
    message("protobuf found")
else ()
    message(FATAL_ERROR "Cannot find Protobuf")
endif ()

PROTOBUF_GENERATE_CPP(PROTO_SRCS PROTO_HDRS protocolbufTest.proto)
include_directories(${PROTOBUF_INCLUDE_DIRS})
include_directories(${CMAKE_CURRENT_BINARY_DIR})
#add_executable(Client client.cpp protocolbufTest.pb.cc)
add_executable(Client ${SRC_CLIENT_LIST} ${PROTO_SRCS} ${PROTO_HDRS})
target_link_libraries(Client ${PROTOBUF_LIBRARIES} PkgConfig::ZeroMQ)

add_executable(Server ${SRC_SERVER_LIST} ${PROTO_SRCS} ${PROTO_HDRS})
target_link_libraries(Server ${PROTOBUF_LIBRARIES} PkgConfig::ZeroMQ)


###  req <-> rep 扩展模式
add_executable(broker_client ${BROKER_CLIENT_LIST})
target_link_libraries(broker_client PkgConfig::ZeroMQ)

add_executable(broker_broker ${BROKER_BROKER_LIST})
target_link_libraries(broker_broker PkgConfig::ZeroMQ)

add_executable(broker_worker ${BROKER_WORKER_LIST})
target_link_libraries(broker_worker PkgConfig::ZeroMQ)
###
#target_include_directories(${PROJECT_NAME} PUBLIC $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>/)




# target_link_libraries(hello-world message-static)
