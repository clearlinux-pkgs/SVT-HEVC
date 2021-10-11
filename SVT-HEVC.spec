#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : SVT-HEVC
Version  : 1.5.1
Release  : 8
URL      : https://github.com/OpenVisualCloud/SVT-HEVC/archive/v1.5.1/SVT-HEVC-1.5.1.tar.gz
Source0  : https://github.com/OpenVisualCloud/SVT-HEVC/archive/v1.5.1/SVT-HEVC-1.5.1.tar.gz
Summary  : SVT (Scalable Video Technology) for HEVC encoder library
Group    : Development/Tools
License  : GPL-2.0
Requires: SVT-HEVC-bin = %{version}-%{release}
Requires: SVT-HEVC-filemap = %{version}-%{release}
Requires: SVT-HEVC-lib = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-meson
BuildRequires : pkg-config
BuildRequires : pkgconfig(gstreamer-1.0)
BuildRequires : pkgconfig(gstreamer-base-1.0)
BuildRequires : pkgconfig(gstreamer-pbutils-1.0)
BuildRequires : pkgconfig(gstreamer-video-1.0)
BuildRequires : yasm

%description
# Scalable Video Technology for HEVC Encoder (SVT-HEVC Encoder)
[![AppVeyor Build Status](https://ci.appveyor.com/api/projects/status/github/openvisualcloud/SVT-HEVC?branch=master&svg=true)](https://ci.appveyor.com/project/openvisualcloud/SVT-HEVC)
[![Travis Build Status](https://travis-ci.com/OpenVisualCloud/SVT-HEVC.svg?branch=master)](https://travis-ci.com/OpenVisualCloud/SVT-HEVC)

%package bin
Summary: bin components for the SVT-HEVC package.
Group: Binaries
Requires: SVT-HEVC-filemap = %{version}-%{release}

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


%package filemap
Summary: filemap components for the SVT-HEVC package.
Group: Default

%description filemap
filemap components for the SVT-HEVC package.


%package lib
Summary: lib components for the SVT-HEVC package.
Group: Libraries
Requires: SVT-HEVC-filemap = %{version}-%{release}

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
export SOURCE_DATE_EPOCH=1633811751
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto -march=x86-64-v3 -mtune=skylake "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto -march=x86-64-v3 -mtune=skylake "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto -march=x86-64-v3 -mtune=skylake "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto -march=x86-64-v3 -mtune=skylake "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64"
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx512
pushd clr-build-avx512
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto -march=x86_64-v4 -mtune=skylake "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto -march=x86_64-v4 -mtune=skylake "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto -march=x86_64-v4 -mtune=skylake "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto -march=x86_64-v4 -mtune=skylake "
export CFLAGS="$CFLAGS -march=x86-64-v4 -m64 "
export CXXFLAGS="$CXXFLAGS -march=x86-64-v4 -m64 "
export FFLAGS="$FFLAGS -march=x86-64-v4 -m64 "
export FCFLAGS="$FCFLAGS -march=x86-64-v4 -m64 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1633811751
rm -rf %{buildroot}
pushd clr-build-avx2
%make_install_v3  || :
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}
popd
pushd clr-build-avx512
%make_install_v4  || :
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}
popd
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/SvtHevcEncApp
/usr/share/clear/optimized-elf/bin*

%files dev
%defattr(-,root,root,-)
/usr/include/svt-hevc/EbApi.h
/usr/include/svt-hevc/EbApiVersion.h
/usr/include/svt-hevc/EbErrorCodes.h
/usr/lib64/libSvtHevcEnc.so
/usr/lib64/pkgconfig/SvtHevcEnc.pc

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-SVT-HEVC

%files lib
%defattr(-,root,root,-)
/usr/lib64/libSvtHevcEnc.so.1
/usr/share/clear/optimized-elf/lib*
