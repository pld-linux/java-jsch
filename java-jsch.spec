Summary:	JSch - a pure Java implementation of SSH2
Summary(pl):	JSch - implementacja protoko³u SSH2 w jêzyku Java
Name:		jsch
Version:	0.1.16
Release:	2
License:	BSD-like
Group:		Development/Languages/Java
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.zip
# Source0-md5:	557ca07abd9d921b05bd56b60b4bfcee
Patch0:		%{name}-date-stupidity.patch
URL:		http://www.jcraft.com/jsch/
BuildRequires:	jakarta-ant
BuildRequires:	jdk >= 1.4
BuildRequires:	unzip
Requires:	jre >= 1.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JSch allows you to connect to an sshd server and use port forwarding,
X11 forwarding, file transfer, etc., and you can integrate its
functionality into your own Java programs.

%description -l pl
JSch pozwala na przeniesienie funkcjonalno¶ci protoko³u SSH2 do
aplikacji pisanych w jêzyku Java. Umo¿liwia m.in. ³±czenie siê z
serwerem sshd, wykorzystanie przekazywania portów oraz sesji X11,
transfer plików.

%prep
%setup -q
%patch0 -p1

%build
ant

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_javadir},%{_examplesdir}/%{name}-%{version}}
install dist/lib/jsch-*.jar $RPM_BUILD_ROOT%{_javadir}
ln -s jsch-*.jar $RPM_BUILD_ROOT%{_javadir}/jsch.jar
cp -rf examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{_javadir}/*.jar
%{_examplesdir}/%{name}-%{version}
