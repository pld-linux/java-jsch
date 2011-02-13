#
%define		pkgname	jsch
#
Summary:	JSch - a pure Java implementation of SSH2
Summary(pl.UTF-8):	JSch - implementacja protokołu SSH2 w języku Java
Name:		java-%{pkgname}
Version:	0.1.44
Release:	1
License:	BSD-like
Group:		Development/Languages/Java
Source0:	http://downloads.sourceforge.net/jsch/%{pkgname}-%{version}.zip
# Source0-md5:	9954d151f16629ed5cf02e56c031954e
Patch0:		%{name}-date-stupidity.patch
URL:		http://www.jcraft.com/jsch/
BuildRequires:	ant >= 1.5.0
BuildRequires:	jdk >= 1.4
BuildRequires:	jpackage-utils
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires:	jre >= 1.4
Obsoletes:	jsch
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JSch allows you to connect to an sshd server and use port forwarding,
X11 forwarding, file transfer, etc., and you can integrate its
functionality into your own Java programs.

%description -l pl.UTF-8
JSch pozwala na przeniesienie funkcjonalności protokołu SSH2 do
aplikacji pisanych w języku Java. Umożliwia m.in. łączenie się z
serwerem sshd, wykorzystanie przekazywania portów oraz sesji X11,
transfer plików.

%package javadoc
Summary:	JSch API documentation
Summary(pl.UTF-8):	Dokumentacja API JSch
Group:		Documentation
Requires:	jpackage-utils
Obsoletes:	jsch-javadoc

%description javadoc
JSch API documentation.

%description javadoc -l pl.UTF-8
Dokumentacja API JSch.

%prep
%setup -qn %{pkgname}-%{version}
%patch0 -p1
sed -i -e 's/VERSION/%{version}/g' build.xml

%build
unset CLASSPATH || :
export JAVA_HOME="%{java_home}"
%ant dist javadoc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadir},%{_javadocdir}/%{pkgname}-%{version},%{_examplesdir}/%{name}-%{version}}

install dist/lib/jsch-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
ln -s jsch-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/jsch.jar
cp -rf examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

cp -R javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{pkgname}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{_javadir}/jsch-%{version}.jar
%{_javadir}/jsch.jar
%{_examplesdir}/%{name}-%{version}

%files javadoc
%defattr(644,root,root,755)
%doc %{_javadocdir}/%{pkgname}-%{version}
