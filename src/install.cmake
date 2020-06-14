# ./src/install.cmake
message(STATUS "INSTALL_PREFIX\t\t= ${CMAKE_INSTALL_PREFIX}")
message(STATUS "CMAKE_BUILD_TYPE\t\t= ${CMAKE_BUILD_TYPE}")
message(STATUS "DESTDIR\t\t\t= ${_DESTDIR}")
message(STATUS "CMAKE_SYSTEM_PROCESSOR\t= ${CMAKE_SYSTEM_PROCESSOR}")
message(STATUS "CMAKE_HOST_SYSTEM_PROCESSOR\t= ${CMAKE_HOST_SYSTEM_PROCESSOR}")

install(
  TARGETS ${TARGET_NAME}
  CONFIGURATIONS ${CMAKE_BUILD_TYPE}
  RUNTIME
    DESTINATION bin
)