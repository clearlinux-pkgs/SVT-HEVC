#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: f4bef72
#
Name     : SVT-HEVC
Version  : 1.5.1
Release  : 22
URL      : https://github.com/OpenVisualCloud/SVT-HEVC/archive/v1.5.1/SVT-HEVC-1.5.1.tar.gz
Source0  : https://github.com/OpenVisualCloud/SVT-HEVC/archive/v1.5.1/SVT-HEVC-1.5.1.tar.gz
Summary  : SVT (Scalable Video Technology) for HEVC encoder library
Group    : Development/Tools
License  : GPL-2.0
Requires: SVT-HEVC-bin = %{version}-%{release}
Requires: SVT-HEVC-lib = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : pkg-config
BuildRequires : pkgconfig(gstreamer-1.0)
BuildRequires : pkgconfig(gstreamer-base-1.0)
BuildRequires : pkgconfig(gstreamer-pbutils-1.0)
BuildRequires : pkgconfig(gstreamer-video-1.0)
BuildRequires : yasm
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Scalable Video Technology for HEVC Encoder (SVT-HEVC Encoder)
[![AppVeyor Build Status](https://ci.appveyor.com/api/projects/status/github/openvisualcloud/SVT-HEVC?branch=master&svg=true)](https://ci.appveyor.com/project/openvisualcloud/SVT-HEVC)
[![Travis Build Status](https://travis-ci.com/OpenVisualCloud/SVT-HEVC.svg?branch=master)](https://travis-ci.com/OpenVisualCloud/SVT-HEVC)

%package bin
Summary: bin components for the SVT-HEVC package.
Group: Binaries

%description bin
bin components for the SVT-HEVC package.


%package dev
Summary: dev components for the SVT-HEVC package.
Group: Development
Requires: SVT-HEVC-lib = %{version}-%{release}
Requires: SVT-HEVC-bin = %{version}-%{release}
Provides: SVT-HEVC-devel = %{version}-%{release}
Requires: SVT-HEVC = %{version}-%{release}

%description dev
dev components for the SVT-HEVC package.


%package lib
Summary: lib components for the SVT-HEVC package.
Group: Libraries

%description lib
lib components for the SVT-HEVC package.


%prep
%setup -q -n SVT-HEVC-1.5.1
cd %{_builddir}/SVT-HEVC-1.5.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1710771884
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1710771884
rm -rf %{buildroot}
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/SvtHevcEncApp

%files dev
%defattr(-,root,root,-)
/usr/include/svt-hevc/EbApi.h
/usr/include/svt-hevc/EbApiVersion.h
/usr/include/svt-hevc/EbErrorCodes.h
/usr/lib64/libSvtHevcEnc.so
/usr/lib64/pkgconfig/SvtHevcEnc.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libSvtHevcEnc.so.1
