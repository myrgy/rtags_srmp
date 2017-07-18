# This file is encoded in UTF-8.  -*- coding: utf-8 -*-

%define debug_package %{nil}

Summary: RTags C/C++ index/refactoring tool
Name: rtags
Version: 2.11
Release: 1
License: GPLv3
URL:     https://github.com/Andersbakken/rtags
Group:   Programming
Source0: https://andersbakken.github.io/rtags-releases/rtags-%{version}.tar.bz2

# BuildRequires:
BuildRequires: cmake >= 3.0.0
BuildRequires: llvm llvm-devel clang-devel clang-libs gcc-c++
BuildRequires: zlib zlib-devel
BuildRequires: openssl-devel openssl
BuildRequires: emacs bash bash-completion help2man
Requires:      clang-libs zlib openssl

BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(bash-completion)
Requires:	emacs-filesystem >= %{_emacs_version}

%description
RTags is a client/server application that indexes C/C++ code and keeps a persistent file-based database of references, declarations, definitions, symbolnames etc. There’s also limited support for ObjC/ObjC++. It allows you to find symbols by name (including nested class and namespace scope). Most importantly we give you proper follow-symbol and find-references support. We also have neat little things like rename-symbol, integration with clang’s “fixits” (http://clang.llvm.org/diagnostics.html). We also integrate with flymake using clang’s vastly superior errors and warnings. Since RTags constantly will reindex “dirty” files you get live updates of compiler errors and warnings. Since we already know how to compile your sources we have a way to quickly bring up the preprocessed output of the current source file in a buffer.

While existing taggers like gnu global, cscope, etags, ctags etc do a decent job for C they often fall a little bit short for C++. With its incredible lexical complexity, parsing C++ is an incredibly hard task and we make no bones about the fact that the only reason we are able to improve on the current tools is because of clang (http://clang.llvm.org/). RTags is named RTags in recognition of Roberto Raggi on whose C++ parser we intended to base this project but he assured us clang was the way to go. The name stuck though.

%prep
%setup

%clean
%__make -C build clean

%build
pwd
ls
mkdir build; pushd build
%cmake ..
popd
%__make -C build VERBOSE=1 %{?_smp_mflags}
%__make -C build VERBOSE=1 %{?_smp_mflags} man

%install
%__make -C build VERBOSE=1 DESTDIR="%{buildroot}" install

%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man7/*
%{_datadir}/*

%changelog
* Update to 2.11
- Initial RPM release
