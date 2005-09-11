Summary:	HCI Emulation for Linux Bluetooth protocol stack
Summary(pl):	Emulacja HCI dla linuksowego stosu protoko³u Bluetooth
Name:		bluez-hciemu
Version:	1.2
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://bluez.sourceforge.net/download/%{name}-%{version}.tar.gz
# Source0-md5:	94d99005c3068334387012bf579e0af7
URL:		http://bluez.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bluez-libs-devel
BuildRequires:	glib-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HCI Emulation for Linux Bluetooth protocol stack.

%description -l pl
Emulacja HCI dla linuksowego stosu protoko³u Bluetooth.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_sbindir}/*
