Summary:	JSch - a pure Java implementation of SSH2
Summary(pl):	JSch - implementacja protoko³u SSH2 w jêzyku Java
Name:		jsch
Version:	0.1.20
Release:	2
License:	BSD-like
Group:		Development/Languages/Java
Source0:	http://dl.sourceforge.net/jsch/%{name}-%{version}.zip
# Source0-md5:	b965afb2cea1bd6c541e833862022564
Patch0:		%{name}-date-stupidity.patch
URL:		http://www.jcraft.com/jsch/
BuildRequires:	ant >= 1.5.0
BuildRequires:	jdk >= 1.4
BuildRequires:	jpackage-utils
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires:	jre >= 1.4
BuildArch:	noarch
ExclusiveArch:	i586 i686 pentium3 pentium4 athlon %{x8664} noarch
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

%package javadoc
Summary:	JSch API documentation
Summary(pl):	Dokumentacja API JSch
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
JSch API documentation.

%description javadoc -l pl
Dokumentacja API JSch.

%prep
%setup -q
%patch0 -p1
sed -i -e 's/VERSION/%{version}/g' build.xml

%build
unset CLASSPATH || :
export JAVA_HOME="%{java_home}"
%ant dist javadoc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadir},{%{_javadocdir},%{_examplesdir}}/%{name}-%{version}}

install dist/lib/jsch-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
ln -s jsch-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/jsch.jar
cp -rf examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

cp -R javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{_javadir}/*.jar
%{_examplesdir}/%{name}-%{version}

%files javadoc
%defattr(644,root,root,755)
%doc %{_javadocdir}/%{name}-%{version}
