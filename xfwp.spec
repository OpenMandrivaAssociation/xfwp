Name:		xfwp
Version:	1.0.3
Release:	14
Summary:	X firewall proxy
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires:	pkgconfig(ice) >= 1.0.0
BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xorg-macros)
Provides:	proxymngr = %{EVRD}

%description
The X firewall proxy (xfwp) is an application layer gateway proxy that
may be run on a network firewall host to forward X traffic across the
firewall. Used in conjunction with the X server Security extension and
authorization checking, xfwp constitutes a safe, simple, and reliable
mechanism both to hide the addresses of X servers located on the
Intranet and to enforce a server connection policy.

%prep
%setup -q

%build
%configure2_5x --disable-strict-compilation --disable-selective-werror
%make

%install
%makeinstall_std

%files
%{_bindir}/xfwp
%{_mandir}/man1/xfwp.1*
