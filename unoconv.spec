# $Id$
# Authority: dag
# Upstream: Dag Wieers <dag$wieers,com>

Summary: Convert any document to any document supported by OpenOffice
Name: unoconv
Version: 0.1
Release: 1
License: GPL
Group: System Environment/Base
URL: http://dag.wieers.com/home-made/unoconv/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dag.wieers.com/home-made/unoconv/unoconv-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel, openoffice-core
Requires: python >= 2.0

%description
unoconv converts any document format that OpenOffice can import, to any
document format that OpenOffice can export.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README THANKS TODO WISHLIST
%{_bindir}/unoconv

%changelog
* Sat May 19 2007 Dag Wieers <dag@wieers.com> - 0.1-1
- Initial package. (using DAR)