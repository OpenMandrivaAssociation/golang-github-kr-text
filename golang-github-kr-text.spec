# http://github.com/kr/text

%global goipath         github.com/kr/text
%global commit          6807e777504f54ad073ecef66747de158294b639


%gometa -i

Name:           %{goname}
Version:        0
Release:        0.17%{?dist}
Summary:        Go package for manipulating paragraphs of text
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%install
chmod 664 wrap.go
%goinstall glide.lock glide.yaml
mv colwriter/Readme Readme-colwriter
mv mc/Readme Readme-mc

%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license License
%doc Readme Readme-colwriter Readme-mc

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.16.git6807e77
- Upload glide files

* Thu Mar 01 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.15.20131111git6807e77
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.git6807e77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.git6807e77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.git6807e77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.git6807e77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 18 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.10.git6807e77
- Polish the spec file
  related: #1248175

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.9.git6807e77
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.git6807e77
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.git6807e77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.6.git6807e77
- Update to spec-2.1
  related: #1248175

* Wed Jul 29 2015 jchaloup <jchaloup@redhat.com> - 0-0.5.git6807e77
- Update of spec file to spec-2.0
  resolves: #1248175

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.git6807e77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Sep 19 2014 Jan Chaloupka <jchaloup@fedoraproject.org> - 0-0.3.git6807e77
- add golang version with necessary golang macros
- quiet setup

* Thu Sep 11 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.2.git6807e77
- gopath defined in golang package
- preserve timestamps while copying source files
- attrs not needed
- devel description update
- include check section
- get rid of files listed twice warning for doc files
- noarch
- needs kr/pty as BR
- chmod wrap.go to 644 (needs to be upstreamed)

* Wed Aug 06 2014 Adam Miller <maxamillion@fedoraproject.org> - 0.1.git6807e77
- First package for Fedora.

