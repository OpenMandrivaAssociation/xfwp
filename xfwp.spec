Name:		xfwp
Version:	1.0.1
Release:	%mkrel 6
Summary:	X firewall proxy
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires: libice-devel >= 1.0.0
BuildRequires: libx11-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
The X firewall proxy (xfwp) is an application layer gateway proxy that
may be run on a network firewall host to forward X traffic across the
firewall. Used in conjunction with the X server Security extension and
authorization checking, xfwp constitutes a safe, simple, and reliable
mechanism both to hide the addresses of X servers located on the
Intranet and to enforce a server connection policy.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xfwp
%{_mandir}/man1/xfwp.1*
