Summary:	View Your Mind - a mind mapping tool.
Summary(pl):	View Your Mind - program do tworzenia map my¶li.
Name:		vym
Version:	1.7.0
Release:	0.3
License:	GPL v2+, with explicit permission to link against Qt
Group:		Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	f1d4ba9f5a2362a213f7ff90ad6cdfec
Patch0:		%{name}-includes.patch
Patch1:		%{name}-docpath.patch
URL:		http://www.insilmaril.de/vym
BuildRequires:	sed >= 4.0
BuildRequires:	qmake
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VYM (View Your Mind) is a tool to generate and manipulate maps which
show your thoughts. Such maps can help you to improve your creativity
and effectivity. You can use them for time management, to organize
tasks, to get an overview over complex contexts, to sort your ideas
etc.

%description -l pl
VYM jest narzêdziem do tworzenia i edycji map my¶li.  Wspomagaj± one
kreatywno¶æ i efektywno¶æ pracy.  Mo¿na ich u¿ywaæ do zarz±dzania
czasem, organizacji zadañ, ogarniêcia z³o¿onych problemów,
porz±dkowania pomys³ów...

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
qmake \
    QMAKE_CXX="%{__cxx}" \
    QMAKE_LINK="%{__cxx}" \
    QMAKE_CXXFLAGS_RELEASE="%{rpmcflags}" \
    QMAKE_RPATH=
sed -i -e 's/-lqt /-lqt-mt /' Makefile
%{__make} \
    QTDIR=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
    QTDIR=%{_prefix} \
    INSTALL_ROOT=$RPM_BUILD_ROOT

# This is needed to be always there for Help menu to work.
# do not move it  to _docdir, as docdir can be omited with --excludedocs at install time.
mv $RPM_BUILD_ROOT{%{_docdir}/packages/vym,%{_datadir}/%{name}}/vym.pdf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE doc/vym.pdf
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
