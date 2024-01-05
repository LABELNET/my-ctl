#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@Create  :   2024/01/05 13:47:10
@Author  :   Yuan Mingzhuo
"""

from os import getcwd, makedirs
from os.path import join, exists
import json
import os

"""
# 目录结构
$ .SIMPLE-DEPS      
│   CMakeLists.txt                 # 项目根 CMakeLists.txt , 用于项目配置
│   README.md                      # 说明文档，无关
├───.vscode                        # 头文件路径配置
│       c_cpp_properties.json
├───cmake                          # 第三方依赖文件夹
├───build                          # CMake 编译输出
└───demo                           # 主模块
    │   CMakeLists.txt             # 主模块 CMakeLists.txt                    
    ├───include                    # 源码：头文件文件夹
    │       demo_utils.h
    └───src                        # 源码: 代码文件夹
            demo_utils.cc
            main.cc
```
"""


def new_file(file_name, data):
    """
    create new file
    """
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(data)


def new_project_dir(project_name):
    """
    project_name
    """
    project_dir = join(getcwd(), project_name)
    if not exists(project_dir):
        makedirs(project_dir)


def new_root_CMakeLists(project_name):
    """
    root/CMakeLists.txt
    """
    content = [
        "cmake_minimum_required(VERSION 3.18)",
        "\n",
        "# 项目名称",
        f"set(PROJECT_NAME {project_name})",
        "project(${PROJECT_NAME} VERSION 0.1.0)",
        "\n",
        "if (NOT CMAKE_BUILD_TYPE)",
        "    set(CMAKE_BUILD_TYPE Release)",
        "endif()",
        "\n",
        "# 2. C++ 标准库",
        "set(CMAKE_CXX_STANDARD 20)",
        "set(CMAKE_CXX_STANDARD_REQUIRED ON)",
        "set(CMAKE_CXX_EXTENSIONS OFF)",
        "\n",
        "# 3. 第三方库",
        'set(CMAKE_MODULE_PATH "${CMAKE_CURRENT_LIST_DIR}/cmake;${CMAKE_MODULE_PATH}")',
        "#set (ZLIB_ROOT D:/Software/vcpkg/packages/zlib_x64-windows)" "\n",
        "# 4.工程名称",
        "project(${PROJECT_NAME} LANGUAGES CXX)",
        "\n",
        "# 5.主模块 main",
        "add_subdirectory(demo)",
        "\n",
        "# 6.打包器",
        "set(CPACK_PROJECT_NAME ${PROJECT_NAME})",
        "set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})",
        "include(CPack)",
        "\n",
        "# 8. Windows 异常",
        "if (WIN32)",
        "    add_definitions (-DNOMINMAX -D_USE_MATH_DEFINES)",
        "endif ()",
        "\n",
        "# 9.使用编译缓存，提升编译速度",
        "if (NOT MSVC)",
        "    find_program (CCACHE_PROGRAM ccache)",
        "    if (CCACHE_PROGRAM)",
        '        message (STATUS "Found CCache: ${CCACHE_PROGRAM}")',
        "        set_property (GLOBAL PROPERTY RULE_LAUNCH_COMPILE ${CCACHE_PROGRAM})",
        "        set_property (GLOBAL PROPERTY RULE_LAUNCH_LINK ${CCACHE_PROGRAM})",
        "    endif ()",
        "endif ()",
    ]
    file = join(getcwd(), project_name, "CMakeLists.txt")
    data = "\n".join(content)
    new_file(file, data)


def new_root_readme(project_name):
    """
    root/README.md
    """
    mulu = """
        $ SIMPLE-MOD-DEPS      
        │   CMakeLists.txt                 # 项目根 CMakeLists.txt,多模块
        │   README.md                      # 说明文档，无关
        ├───.vscode                        # 头文件路径配置
        │       c_cpp_properties.json
        ├───build                          # CMake 编译输出
        ├───cmake                          # 第三方依赖存放路径 FindXXX.cmake
        ├───demo                           # 主模块 main
        │   │   CMakeLists.txt             # 主模块 CMakeLists.txt ，配置子模块链接
        │   │
        │   ├───include                    # 源码: 主模块头文件
        │   │       demo_utils.h   
        │   │  
        │   └───src                        # 源码: 主模块源码实现
        │           demo_utils.cc
        │           main.cc                
        │
        └───store                          # 子模块
            │   CMakeLists.txt             # 子模块 CMakeLists.txt ，本地依赖包
            │
            ├───include                    # 源码: 子模块头文件
            │       store_utils.h
            │
            └───src                        # 源码: 子模块源码实现
                    store_utils.cc
        """
    content = [f"#{project_name}", "补充内容", "\n", "#目录结构", "\n", f"{mulu}"]
    file = join(getcwd(), project_name, "README.md")
    data = "\n".join(content)
    new_file(file, data)


def new_vscode_cpp(project_name):
    """
    root/.vscode/c_cpp_properties.json
    """
    vscode_dir = join(getcwd(), project_name, ".vscode")
    if not exists(vscode_dir):
        makedirs(vscode_dir)
    cpp_properties = {
        "configurations": [
            {
                "name": "Win32",
                "includePath": [
                    "${default}",
                    "${workspaceFolder}/demo/include",
                    "${workspaceFolder}/store/include",
                ],
                "defines": ["_DEBUG", "UNICODE", "_UNICODE"],
                "windowsSdkVersion": "10.0.22621.0",
                "intelliSenseMode": "windows-msvc-x64",
            }
        ],
        "version": 4,
    }
    data = json.dumps(cpp_properties, indent=4)
    file = join(vscode_dir, "c_cpp_properties.json")
    new_file(file, data)


def new_cmake_dir(project_name):
    """
    root/cmake
    """
    cmake_dir = join(getcwd(), project_name, "cmake")
    if not exists(cmake_dir):
        makedirs(cmake_dir)


def new_main_module(project_name):
    """
    root/module
    """
    module_name = str(project_name).replace("-", "_")
    module_dir = join(getcwd(), project_name, module_name)
    if not exists(module_dir):
        makedirs(module_dir)
    # root/module/include
    module_include_dir = join(module_dir, "include")
    if not exists(module_include_dir):
        makedirs(module_include_dir)
    # root/module/src
    module_src_dir = join(module_dir, "src")
    if not exists(module_src_dir):
        makedirs(module_src_dir)
    # root/module/src/main.cc
    data = "/// 主模块代码实现"
    file = join(module_src_dir, "main.cc")
    new_file(file, data)
    # root/module/CMakeLists.txt
    cmake_content = [
        "cmake_minimum_required (VERSION 3.18)",
        "\n",
        "# 1.可执行文件",
        f"add_executable ({module_name})",
        "\n",
        "# 2.源码，注意: 源文件代码格式，这里用的为 .cc 文件",
        "file (GLOB_RECURSE srcs CONFIGURE_DEPENDS src/*.cc include/*.h)",
        "\n",
        "# 3.目标",
        "target_sources (demo PUBLIC ${srcs})" "\n",
        "# 4.头文件",
        f"target_include_directories ({module_name} PUBLIC include)" "\n",
        "# 5.非主模块, 链接库",
        "# add_library(store STATIC ${srcs})",
        "# add_library(store SHARED ${srcs})",
        "# add_library(store OBJECT ${srcs})",
        "\n",
        "# 6.第三方依赖 GRPC",
        "# find_package (gRPC CONFIG REQUIRED)",
        "\n",
        "# 7.第三方依赖 Link ",
        "# target_link_libraries (demo PUBLIC subModeul)",
    ]
    file = join(module_dir, "CMakeLists.txt")
    data = "\n".join(cmake_content)
    new_file(file, data)


def create_cpp(project_name):
    """
    创建C++模板工程
    """
    new_project_dir(project_name)
    new_root_CMakeLists(project_name)
    new_root_readme(project_name)
    new_vscode_cpp(project_name)
    new_cmake_dir(project_name)
    new_main_module(project_name)
