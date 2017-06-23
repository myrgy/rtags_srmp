# This file is encoded in UTF-8.  -*- coding: utf-8 -*-

%define debug_package %{nil}

Summary: RTags C/C++ index/refactoring tool
Name: rtags
Version: 2.10
Release: 1
License: GPLv3
URL:     https://github.com/Andersbakken/rtags
Group:   Programming
Source0: https://andersbakken.github.io/rtags-releases/rtags-%{version}.tar.bz2

Buildroot: %{_tmppath}/%{name}-%{version}-root

# BuildRequires:
BuildRequires: cmake llvm llvm-devel clang-devel clang-libs gcc-c++
BuildRequires: zlib zlib-devel
BuildRequires: openssl-devel openssl
Requires:      clang-libs zlib openssl

%description
RTags is a client/server application that indexes C/C++ code and keeps a persistent file-based database of references, declarations, definitions, symbolnames etc. There’s also limited support for ObjC/ObjC++. It allows you to find symbols by name (including nested class and namespace scope). Most importantly we give you proper follow-symbol and find-references support. We also have neat little things like rename-symbol, integration with clang’s “fixits” (http://clang.llvm.org/diagnostics.html). We also integrate with flymake using clang’s vastly superior errors and warnings. Since RTags constantly will reindex “dirty” files you get live updates of compiler errors and warnings. Since we already know how to compile your sources we have a way to quickly bring up the preprocessed output of the current source file in a buffer.

While existing taggers like gnu global, cscope, etags, ctags etc do a decent job for C they often fall a little bit short for C++. With its incredible lexical complexity, parsing C++ is an incredibly hard task and we make no bones about the fact that the only reason we are able to improve on the current tools is because of clang (http://clang.llvm.org/). RTags is named RTags in recognition of Roberto Raggi on whose C++ parser we intended to base this project but he assured us clang was the way to go. The name stuck though.

%prep
%setup
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
