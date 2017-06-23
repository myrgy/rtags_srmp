# This file is encoded in UTF-8.  -*- coding: utf-8 -*-

%define debug_package %{nil}

Summary: RTags C/C++ index/refactoring tool
Name: rtags
Version: 2.10
Release: 1
License: GPL3
URL:     https://github.com/Andersbakken/rtags
Group:   Programming
Source0: https://andersbakken.github.io/rtags-releases/rtags-%{version}.tar.bz2

Prefix:  %{cdir}

Buildroot: %{_tmppath}/%{name}-%{version}-root

# BuildRequires:
BuildRequires: cmake llvm llvm-devel clang-devel clang-libs gcc-c++
BuildRequires: zlib zlib-devel
BuildRequires: openssl-devel openssl-libs
Requires:      clang-libs zlib openssl

%description
RTags is a client/server application that indexes C/C++ code and keeps a persistent file-based database of references, declarations, definitions, symbolnames etc. 

%prep
%setup -q
cmake .

%clean
%__make clean

%build
%__make %{?_smp_mflags}

%install
%__make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/local/share/bash-completion/completions/rtags
/usr/local/share/bash-completion/completions/rc
/usr/local/share/bash-completion/completions/rdm
/usr/local/bin/rdm
/usr/local/bin/rc
/usr/local/bin/rp
/usr/local/bin/gcc-rtags-wrapper.sh
/usr/local/share/man/man7/rc.7
/usr/local/share/man/man7/rdm.7
/usr/local/share/emacs/site-lisp/rtags/rtags.el
/usr/local/share/emacs/site-lisp/rtags/rtags.elc
/usr/local/share/emacs/site-lisp/rtags/ac-rtags.el
/usr/local/share/emacs/site-lisp/rtags/ac-rtags.elc
/usr/local/share/emacs/site-lisp/rtags/helm-rtags.el
/usr/local/share/emacs/site-lisp/rtags/helm-rtags.elc
/usr/local/share/emacs/site-lisp/rtags/ivy-rtags.el
/usr/local/share/emacs/site-lisp/rtags/ivy-rtags.elc
/usr/local/share/emacs/site-lisp/rtags/company-rtags.el
/usr/local/share/emacs/site-lisp/rtags/company-rtags.elc
/usr/local/share/emacs/site-lisp/rtags/flycheck-rtags.el
/usr/local/share/emacs/site-lisp/rtags/flycheck-rtags.elc
