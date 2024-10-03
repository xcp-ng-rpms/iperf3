Name:           iperf3
Version:        3.9
Release:        13%{?dist}
Summary:        Measurement tool for TCP/UDP bandwidth performance

License:        BSD
URL:            https://github.com/esnet/iperf
Source0:        https://github.com/esnet/iperf/archive/%{version}.tar.gz
Patch0000:	0000-cve-2023-38403.patch
Patch0001:	0001-cve-2023-7250.patch
Patch0002:	0002-cve-2024-26306.patch

BuildRequires:  libuuid-devel
BuildRequires:  gcc
BuildRequires:  lksctp-tools-devel
BuildRequires:  openssl-devel
BuildRequires:  make

%description
Iperf is a tool to measure maximum TCP bandwidth, allowing the tuning of
various parameters and UDP characteristics. Iperf reports bandwidth, delay
jitter, data-gram loss.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n iperf-%{version} -p1

%build
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall -C src INSTALL_DIR="%{buildroot}%{_bindir}"
mkdir -p %{buildroot}%{_mandir}/man1
rm -f %{buildroot}%{_libdir}/libiperf.la

%files
%doc README.md LICENSE RELNOTES.md
%{_mandir}/man1/iperf3.1.gz
%{_mandir}/man3/libiperf.3.gz
%{_bindir}/iperf3
%{_libdir}/*.so.*

%files          devel
%{_includedir}/iperf_api.h
%{_libdir}/*.so

%changelog
* Tue Jun 11 2024 Michal Ruprich <mruprich@redhat.com> - 3.9-13
- Resolves: RHEL-29579 - vulnerable to marvin attack if the authentication option is used

* Tue Jun 04 2024 Michal Ruprich <mruprich@redhat.com> - 3.9-12
- Resolves: RHEL-39975 - possible denial of service

* Wed Aug 09 2023 Michal Ruprich <mruprich@redhat.com> - 3.9-11
- Related: #2223676 - bumping version for correct update path

* Fri Jul 28 2023 Jonathan Wright <jonathan@almalinux.org> - 3.9-10
- Fixes CVE-2023-38403
  Resolves: rhbz#2223676

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 3.9-9
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Wed Jun 16 2021 Mohan Boddu <mboddu@redhat.com> - 3.9-8
- Rebuilt for RHEL 9 BETA for openssl 3.0
  Related: rhbz#1971065

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 3.9-7
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 31 2020 Kevin Fenzi <kevin@scrye.com> - 3.9-5
- Update to 3.9. Fixes bug #1846161

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 19 2020 Michal Ruprich <mruprich@redhat.com> - 3.7-4
- Add openssl-devel to BuildRequires to enable authentization of client

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 2019 Kevin Fenzi <kevin@scrye.com> - 3.7-1
- Update to 3.7. Fixes bug #1723020

* Tue Feb 26 2019 Tomas Korbar <tkorbar@redhat.com> - 3.6-5
- Add lksctp-tools-devel to BuildRequires
- Fix bug #1647385

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Kevin Fenzi <kevin@scrye.com> - 3.6-3
- Fix FTBFS bug #1604377 by adding BuildRequires: gcc

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Kevin Fenzi <kevin@scrye.com> - 3.6-1
- Update to 3.6. Fixes bug #1594995

* Sat Mar 03 2018 Kevin Fenzi <kevin@scrye.com> - 3.5-1
- Update to 3.5. Fixes bug #1551166

* Fri Feb 16 2018 Kevin Fenzi <kevin@scrye.com> - 3.4-1
- Upgrade to 3.4. Fixes bug #1545468

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 04 2017 Kevin Fenzi <kevin@scrye.com> - 3.3-1
- Update to 3.3. Fixes bug #1508669

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Kevin Fenzi <kevin@scrye.com> - 3.2-1
- Update to 3.2. Fixes bug #1465195

* Wed Mar 08 2017 Kevin Fenzi <kevin@scrye.com> - 3.1.7-1
- Update to 3.1.7. Fixes bug #1429901

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 03 2017 Kevin Fenzi <kevin@scrye.com> - 3.1.6-1
- Update to 3.1.6. Fixes bug #1418879

* Fri Jan 13 2017 Kevin Fenzi <kevin@scrye.com> - 3.1.5-1
- Update to 3.1.5. Fixes bug #1412848

* Sat Nov 05 2016 Kevin Fenzi <kevin@scrye.com> - 3.1.4-1
- Update to 3.1.4. Fixes bug #1390396

* Wed Jun 08 2016 Kevin Fenzi <kevin@scrye.com> - 3.1.3-1
- Update to 3.1.3

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1b3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 08 2015 Susant Sahani <ssahani@gmail.com> 3.1b3
- Update to 3.1b3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 04 2015 Susant Sahani <ssahani@gmail.com> 3.0.11-1
- Update to 3.0.11

* Sat Dec 20 2014 Susant Sahani <ssahani@redhat.com> 3.0.10-1
- Update to 3.0.10

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 30 2014 Susant Sahani <ssahani@redhat.com> 3.0.6-1
- Update to 3.0.6

* Thu Jun 19 2014 Susant Sahani <ssahani@redhat.com> 3.0.5-1
- Update to 3.0.5

* Tue Jun 10 2014 Susant Sahani <ssahani@redhat.com> - 3.0.3-5
- fix compilation BZ #1106803

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 2 2014 François Cami <fcami@fedoraproject.org> - 3.0.3-3
- Drop static library support (#1081486).
- iperf3-devel subpackage must require iperf3.
- iperf3-devel should only contain the unversioned shared library.
- Call ldconfig since we are installing a shared library now.
- Removed INSTALL file.

* Wed Apr 2 2014 Susant Sahani <ssahani@redhat.com> 3.0.3-2
- Moved static library to devel section only .

* Sun Mar 30 2014 Susant Sahani <ssahani@redhat.com> 3.0.3-1
- Update to 3.0.3 and added devel rpm support

* Tue Mar 11 2014 Susant Sahani <ssahani@redhat.com> 3.0.2-1
- Update to 3.0.2

* Tue Jan 14 2014 Susant Sahani <ssahani@redhat.com> 3.0.1-1
- Update to 3.0.1

* Fri Oct 25 2013 Steven Roberts <strobert@strobe.net> 3.0-1
- Update to 3.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.5.b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat May 04 2013 Kevin Fenzi <kevin@scrye.com> 3.0-0.4.b5
- Update to 3.0b5

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.3.b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.2.b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.1.b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Apr 06 2011 G.Balaji <balajig81@gmail.com> 3.0b4-2
- Changed the Spec name, removed static libs generation and devel
- package.

* Sat Mar 26 2011 G.Balaji <balajig81@gmail.com> 3.0b4-1
- Initial Version
