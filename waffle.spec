#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : waffle
Version  : 1.5.2
Release  : 2
URL      : https://github.com/waffle-gl/waffle/archive/v1.5.2.tar.gz
Source0  : https://github.com/waffle-gl/waffle/archive/v1.5.2.tar.gz
Summary  : a library for selecting an OpenGL API and window system at runtime
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: waffle-bin
Requires: waffle-lib
Requires: waffle-data
Requires: waffle-doc
BuildRequires : cmake
BuildRequires : pkgconfig(egl)
BuildRequires : pkgconfig(gbm)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(wayland-egl)
BuildRequires : pkgconfig(x11-xcb)

%description
CMOCKA
=======
cmocka is a fork for Google's cmockery unit testing framework to fix bugs and
support it in future.
See https://code.google.com/p/cmockery/

%package bin
Summary: bin components for the waffle package.
Group: Binaries
Requires: waffle-data

%description bin
bin components for the waffle package.


%package data
Summary: data components for the waffle package.
Group: Data

%description data
data components for the waffle package.


%package dev
Summary: dev components for the waffle package.
Group: Development
Requires: waffle-lib
Requires: waffle-bin
Requires: waffle-data
Provides: waffle-devel

%description dev
dev components for the waffle package.


%package doc
Summary: doc components for the waffle package.
Group: Documentation

%description doc
doc components for the waffle package.


%package lib
Summary: lib components for the waffle package.
Group: Libraries
Requires: waffle-data

%description lib
lib components for the waffle package.


%prep
%setup -q -n waffle-1.5.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1519154937
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=/usr/lib64 -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=64 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_RANLIB=/usr/bin/gcc-ranlib
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1519154937
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/wflinfo

%files data
%defattr(-,root,root,-)
/usr/share/cmake/*

%files dev
%defattr(-,root,root,-)
/usr/include/waffle-1/waffle.h
/usr/include/waffle-1/waffle_gbm.h
/usr/include/waffle-1/waffle_glx.h
/usr/include/waffle-1/waffle_version.h
/usr/include/waffle-1/waffle_wayland.h
/usr/include/waffle-1/waffle_x11_egl.h
/usr/lib64/cmake/Waffle/WaffleConfig.cmake
/usr/lib64/cmake/Waffle/WaffleConfigVersion.cmake
/usr/lib64/libwaffle-1.so
/usr/lib64/pkgconfig/waffle-1.pc

%files doc
%defattr(-,root,root,-)
/usr/share/doc/waffle1/HACKING.txt
/usr/share/doc/waffle1/LICENSE-threads.txt
/usr/share/doc/waffle1/LICENSE.txt
/usr/share/doc/waffle1/README.txt
/usr/share/doc/waffle1/examples/Makefile.example
/usr/share/doc/waffle1/examples/gl_basic.c
/usr/share/doc/waffle1/examples/simple-x11-egl.c
/usr/share/doc/waffle1/release-notes/waffle-0.1.txt
/usr/share/doc/waffle1/release-notes/waffle-0.2.txt
/usr/share/doc/waffle1/release-notes/waffle-0.3.0.txt
/usr/share/doc/waffle1/release-notes/waffle-0.3.1.txt
/usr/share/doc/waffle1/release-notes/waffle-1.0.0.txt
/usr/share/doc/waffle1/release-notes/waffle-1.0.1.txt
/usr/share/doc/waffle1/release-notes/waffle-1.1.0.txt
/usr/share/doc/waffle1/release-notes/waffle-1.1.1.txt
/usr/share/doc/waffle1/release-notes/waffle-1.1.2.txt
/usr/share/doc/waffle1/release-notes/waffle-1.2.0.txt
/usr/share/doc/waffle1/release-notes/waffle-1.2.1.txt
/usr/share/doc/waffle1/release-notes/waffle-1.2.2.txt
/usr/share/doc/waffle1/release-notes/waffle-1.3.0.txt
/usr/share/doc/waffle1/release-notes/waffle-1.4.0.txt
/usr/share/doc/waffle1/release-notes/waffle-1.4.1.txt
/usr/share/doc/waffle1/release-notes/waffle-1.4.2.txt
/usr/share/doc/waffle1/release-notes/waffle-1.4.3.txt
/usr/share/doc/waffle1/release-notes/waffle-1.4.4.txt
/usr/share/doc/waffle1/release-notes/waffle-1.5.0.txt
/usr/share/doc/waffle1/release-notes/waffle-1.5.1.txt
/usr/share/doc/waffle1/release-notes/waffle-1.5.2.txt

%files lib
%defattr(-,root,root,-)
/usr/lib64/libwaffle-1.so.0
/usr/lib64/libwaffle-1.so.0.5.2
