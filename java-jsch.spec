Summary:	JSch - a pure Java implementation of SSH2.
Name:		jsch
Version:	0.1.16
Release:	1
License:	BSD-like
Group:		Development/Languages/Java
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.zip
# Source0-md5:	557ca07abd9d921b05bd56b60b4bfcee
URL:		http://www.jcraft.com/jsch/
BuildRequires:	jakarta-ant
BuildRequires:	jdk >= 1.4
Requires:	jre >= 1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JSch allows you to connect to an sshd server and use port forwarding,
X11 forwarding, file transfer, etc., and you can integrate its
functionality into your own Java programs.

%prep
%setup -q

%build
ant

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_javadir},%{_examplesdir}/%{name}-%{version}}
install dist/lib/jsch-20040713.jar $RPM_BUILD_ROOT%{_javadir}
ln -s jsch-20040713.jar $RPM_BUILD_ROOT%{_javadir}/jsch.jar
cp -rf examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{_javadir}/*.jar
%{_examplesdir}/%{name}-%{version}/*
