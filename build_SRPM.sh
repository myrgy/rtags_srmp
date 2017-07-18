#/bin/sh

rpmbuild --define "_topdir `pwd`" -bs SPECS/rtags.spec
