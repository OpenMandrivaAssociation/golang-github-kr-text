%global debug_package %{nil}

# Run tests in check section
%bcond_without check

# https://github.com/kr/text
%global goipath		github.com/kr/text
%global forgeurl	https://github.com/kr/text
Version:		0.2.0

%gometa

Summary:	Miscellaneous functions for formatting text
Name:		golang-github-kr-text

Release:	1
Source0:	https://github.com/kr/text/archive/v%{version}/text-%{version}.tar.gz
URL:		https://github.com/kr/text
License:	MIT
Group:		Development/Other
BuildRequires:	compiler(go-compiler)

%description
This is a Go package for manipulating paragraphs of text.

%files
%license License
%doc Readme Readme-colwriter Readme-mc
%{_bindir}/agg
%{_bindir}/go-mc

#-----------------------------------------------------------------------

%package devel
Summary:	%{summary}
Group:		Development/Other
BuildArch:	noarch

%description devel
%{description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%files devel -f devel.file-list
%license License
%doc Readme Readme-colwriter Readme-mc

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n text-%{version}

# fix docs
mv colwriter/Readme Readme-colwriter
mv mc/Readme Readme-mc

%build
%gobuildroot
for cmd in $(ls -1 cmd) ; do
	%gobuild -o _bin/$cmd %{goipath}/cmd/$cmd
done
%gobuild -o _bin/go-mc %{goipath}/mc

%install
%goinstall
for cmd in $(ls -1 _bin) ; do
	install -Dpm 0755 _bin/$cmd %{buildroot}%{_bindir}/$cmd
done


%check
%if %{with check}
%gochecks
%endif

