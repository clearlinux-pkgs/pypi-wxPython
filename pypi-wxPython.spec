#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v13
# autospec commit: dc0ff31b4314
#
Name     : pypi-wxPython
Version  : 4.2.1
Release  : 17
URL      : https://files.pythonhosted.org/packages/aa/64/d749e767a8ce7bdc3d533334e03bb1106fc4e4803d16f931fada9007ee13/wxPython-4.2.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/aa/64/d749e767a8ce7bdc3d533334e03bb1106fc4e4803d16f931fada9007ee13/wxPython-4.2.1.tar.gz
Summary  : Cross platform GUI toolkit for Python, "Phoenix" version
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause BSL-1.0 GPL-2.0 GPL-3.0 HPND LGPL-2.0 Libpng MIT OFL-1.1 TCL Zlib libtiff wxWindows
Requires: pypi-wxPython-license = %{version}-%{release}
Requires: pypi-wxPython-python = %{version}-%{release}
Requires: pypi-wxPython-python3 = %{version}-%{release}
Requires: pypi(numpy)
Requires: pypi(pillow)
Requires: pypi(six)
BuildRequires : doxygen-bin
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pypi(attrdict)
BuildRequires : python3-dev
BuildRequires : sip
BuildRequires : wxWidgets-bin
BuildRequires : wxWidgets-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: backport-0006-Bump-version-number.patch
Patch2: backport-0018-Fix-compatibility-with-Cython-3.0.0.patch
Patch3: backport-0019-Update-sip-to-v6.7.11.patch
Patch4: backport-0038-Fix-additional-SyntaxWarnings-with-Python-3.12.patch
Patch5: backport-0039-integer-division-for-randint.patch
Patch6: backport-0043-Update-sip-to-v6.8.2.patch
Patch7: backport-0044-Add-Python-3.12-to-classifiers.patch
Patch8: backport-0045-Update-sip-to-v6.8.3-and-fix-deprecations.patch
Patch9: Fix-sip-build-failure-on-bool.cpp.patch

%description
sip Extension Module
====================
The sip extension module provides support for the wx package.

%package dev
Summary: dev components for the pypi-wxPython package.
Group: Development
Provides: pypi-wxPython-devel = %{version}-%{release}
Requires: pypi-wxPython = %{version}-%{release}

%description dev
dev components for the pypi-wxPython package.


%package license
Summary: license components for the pypi-wxPython package.
Group: Default

%description license
license components for the pypi-wxPython package.


%package python
Summary: python components for the pypi-wxPython package.
Group: Default
Requires: pypi-wxPython-python3 = %{version}-%{release}
Provides: pypi-wxpython-python

%description python
python components for the pypi-wxPython package.


%package python3
Summary: python3 components for the pypi-wxPython package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pypi-wxPython package.


%prep
%setup -q -n wxPython-4.2.1
cd %{_builddir}/wxPython-4.2.1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p1
%patch -P 7 -p1
%patch -P 8 -p1
%patch -P 9 -p1
pushd ..
cp -a wxPython-4.2.1 buildapx
popd

%build
## build_prepend content
# Convert files to UTF-8
for file in demo/TestTable.txt docs/sphinx/_downloads/i18nwxapp/locale/I18Nwxapp.pot docs/sphinx/class_summary.pkl docs/sphinx/wx.1moduleindex.pkl; do
iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
touch -r $file $file.new && \
mv $file.new $file
done
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1719957065
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
DOXYGEN=/usr/bin/doxygen python3 -u build.py sip build_py --use_syswx --gtk3  %{?_smp_mflags}

pushd ../buildapx
## build_prepend content
# Convert files to UTF-8
for file in demo/TestTable.txt docs/sphinx/_downloads/i18nwxapp/locale/I18Nwxapp.pot docs/sphinx/class_summary.pkl docs/sphinx/wx.1moduleindex.pkl; do
iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
touch -r $file $file.new && \
mv $file.new $file
done
## build_prepend end
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -mapxf -mavx10.1 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
DOXYGEN=/usr/bin/doxygen python3 -u build.py sip build_py --use_syswx --gtk3  %{?_smp_mflags}
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
export SOURCE_DATE_EPOCH=1719957065
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-wxPython
cp %{_builddir}/wxPython-%{version}/demo/data/SIL_OPEN_FONT_LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-wxPython/fa2b5c52bc6b71cbf75cf48e541569d83b22c0a3 || :
cp %{_builddir}/wxPython-%{version}/ext/nanosvg/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-wxPython/f4f94babc436555d2f5992e29aacc47433fbadb4 || :
cp %{_builddir}/wxPython-%{version}/ext/wxWidgets/3rdparty/catch/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-wxPython/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90 || :
cp %{_builddir}/wxPython-%{version}/ext/wxWidgets/3rdparty/nanosvg/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-wxPython/f4f94babc436555d2f5992e29aacc47433fbadb4 || :
cp %{_builddir}/wxPython-%{version}/ext/wxWidgets/3rdparty/pcre/LICENCE %{buildroot}/usr/share/package-licenses/pypi-wxPython/3005b2c68faac406829c8ea56376ddcb1ed0eabb || :
cp %{_builddir}/wxPython-%{version}/ext/wxWidgets/3rdparty/pcre/cmake/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/pypi-wxPython/ff3ed70db4739b3c6747c7f624fe2bad70802987 || :
cp %{_builddir}/wxPython-%{version}/ext/wxWidgets/build/cmake/modules/cotire_test/license %{buildroot}/usr/share/package-licenses/pypi-wxPython/ece76272e705e27f0c76531aac6dd0b10820bc10 || :
cp %{_builddir}/wxPython-%{version}/ext/wxWidgets/docs/gpl.txt %{buildroot}/usr/share/package-licenses/pypi-wxPython/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/wxPython-%{version}/ext/wxWidgets/docs/wine/COPYING.LIB %{buildroot}/usr/share/package-licenses/pypi-wxPython/ec2350cf4fe9c4f97c3ee5c9046d0396672c365a || :
cp %{_builddir}/wxPython-%{version}/ext/wxWidgets/src/expat/expat/COPYING %{buildroot}/usr/share/package-licenses/pypi-wxPython/8623dd26727a708a49dbe6a52edb1d931d70816d || :
cp %{_builddir}/wxPython-%{version}/ext/wxWidgets/src/motif/mdi/COPYRIGHT %{buildroot}/usr/share/package-licenses/pypi-wxPython/3f65d8e23a75d7c0a9a7b7092c9249e4f8cd2db4 || :
cp %{_builddir}/wxPython-%{version}/ext/wxWidgets/src/motif/xmcombo/copying.txt %{buildroot}/usr/share/package-licenses/pypi-wxPython/17e3b0eea99abffe6ac71e65627413236e0b117a || :
cp %{_builddir}/wxPython-%{version}/ext/wxWidgets/src/png/LICENSE %{buildroot}/usr/share/package-licenses/pypi-wxPython/fc3951ba26fe1914759f605696a1d23e3b41766f || :
cp %{_builddir}/wxPython-%{version}/ext/wxWidgets/src/regex/COPYRIGHT %{buildroot}/usr/share/package-licenses/pypi-wxPython/9a5a0d7c8ffa82a9489acbb7f0d6947a2b1bc27f || :
cp %{_builddir}/wxPython-%{version}/ext/wxWidgets/src/stc/scintilla/License.txt %{buildroot}/usr/share/package-licenses/pypi-wxPython/9da27f7b263edb706105ccd68880474013b11bca || :
cp %{_builddir}/wxPython-%{version}/ext/wxWidgets/src/tiff/COPYRIGHT %{buildroot}/usr/share/package-licenses/pypi-wxPython/a2f64f2a85f5fd34bda8eb713c3aad008adbb589 || :
cp %{_builddir}/wxPython-%{version}/ext/wxWidgets/src/zlib/LICENSE %{buildroot}/usr/share/package-licenses/pypi-wxPython/233f44af3fb55dcc7fddfef8e77ac627b0008756 || :
cp %{_builddir}/wxPython-%{version}/license/gpl.txt %{buildroot}/usr/share/package-licenses/pypi-wxPython/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/wxPython-%{version}/license/gpl.txt %{buildroot}/usr/share/package-licenses/pypi-wxPython/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/wxPython-%{version}/license/lgpl.txt %{buildroot}/usr/share/package-licenses/pypi-wxPython/ba8966e2473a9969bdcab3dc82274c817cfd98a1 || :
cp %{_builddir}/wxPython-%{version}/sip/siplib/LICENSE-GPL2 %{buildroot}/usr/share/package-licenses/pypi-wxPython/2136dbc93e95a70deae070e44ff6b2702ec1599c || :
cp %{_builddir}/wxPython-%{version}/sip/siplib/LICENSE-GPL3 %{buildroot}/usr/share/package-licenses/pypi-wxPython/34e9b06e7f12eaed676f57481de931ec91c6ce0a || :
cp %{_builddir}/wxPython-%{version}/wx/lib/pubsub/LICENSE_BSD_Simple.txt %{buildroot}/usr/share/package-licenses/pypi-wxPython/12d9aac371b94aee9fd5e5a9465166095d6438db || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildapx/
python build.py install_py --destdir=%{buildroot}_va
popd
GOAMD64=v2
python build.py install_py --destdir=%{buildroot}
## install_append content
# Remove bins that are really just demos
rm -rf %{buildroot}/usr/bin/*

# Remove locale files (already provided by wxWidgets)
rm -rf %{buildroot}/usr/lib/python*/site-packages/wx/locale
## install_append end
/usr/bin/elf-move.py apx %{buildroot}-va %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/lib/python3.12/site-packages/wx/include/wxPython/sip.h
/usr/lib/python3.12/site-packages/wx/include/wxPython/wxpy_api.h

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-wxPython/12d9aac371b94aee9fd5e5a9465166095d6438db
/usr/share/package-licenses/pypi-wxPython/17e3b0eea99abffe6ac71e65627413236e0b117a
/usr/share/package-licenses/pypi-wxPython/233f44af3fb55dcc7fddfef8e77ac627b0008756
/usr/share/package-licenses/pypi-wxPython/3005b2c68faac406829c8ea56376ddcb1ed0eabb
/usr/share/package-licenses/pypi-wxPython/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90
/usr/share/package-licenses/pypi-wxPython/3f65d8e23a75d7c0a9a7b7092c9249e4f8cd2db4
/usr/share/package-licenses/pypi-wxPython/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/pypi-wxPython/8623dd26727a708a49dbe6a52edb1d931d70816d
/usr/share/package-licenses/pypi-wxPython/9a5a0d7c8ffa82a9489acbb7f0d6947a2b1bc27f
/usr/share/package-licenses/pypi-wxPython/9da27f7b263edb706105ccd68880474013b11bca
/usr/share/package-licenses/pypi-wxPython/a2f64f2a85f5fd34bda8eb713c3aad008adbb589
/usr/share/package-licenses/pypi-wxPython/ba8966e2473a9969bdcab3dc82274c817cfd98a1
/usr/share/package-licenses/pypi-wxPython/ec2350cf4fe9c4f97c3ee5c9046d0396672c365a
/usr/share/package-licenses/pypi-wxPython/ece76272e705e27f0c76531aac6dd0b10820bc10
/usr/share/package-licenses/pypi-wxPython/f4f94babc436555d2f5992e29aacc47433fbadb4
/usr/share/package-licenses/pypi-wxPython/fa2b5c52bc6b71cbf75cf48e541569d83b22c0a3
/usr/share/package-licenses/pypi-wxPython/fc3951ba26fe1914759f605696a1d23e3b41766f
/usr/share/package-licenses/pypi-wxPython/ff3ed70db4739b3c6747c7f624fe2bad70802987

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
