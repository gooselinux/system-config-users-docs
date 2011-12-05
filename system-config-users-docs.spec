# Command line configurables

%if 0%{?fedora}%{?rhel} == 0 || 0%{?fedora} >= 8 || 0%{?rhel} >= 6
%bcond_without rarian_compat
%else
%bcond_with rarian_compat
%endif

Summary: Documentation for administering users and groups
Name: system-config-users-docs
Version: 1.0.8
Release: 1%{?dist}
URL: https://fedorahosted.org/%{name}
License: GPLv2+
Group: Documentation
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
Source: http://fedorahosted.org/released/%{name}/%{name}-%{version}.tar.bz2
BuildRequires: gettext
BuildRequires: pkgconfig
BuildRequires: gnome-doc-utils
BuildRequires: docbook-dtds
%if %{with rarian_compat}
BuildRequires: rarian-compat
%else
BuildRequires: scrollkeeper
%endif
# Until version 1.2.81, system-config-users contained online documentation.
# From version 1.2.82 on, online documentation is split off into its own
# package system-config-users-docs. The following ensures that updating from
# earlier versions gives you both the main package and documentation.
Obsoletes: system-config-users < 1.2.82
Requires: system-config-users >= 1.2.82
%if %{with rarian_compat}
Requires: rarian-compat
%else
Requires(post): scrollkeeper >= 0:0.3.4
Requires(postun): scrollkeeper >= 0:0.3.4
%endif
Requires: yelp

%description
This package contains the online documentation for system-config-users which is
a graphical utility for administrating users and groups.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_bindir}/scrollkeeper-update -q || :

%postun
%{_bindir}/scrollkeeper-update -q || :

%files
%defattr(-,root,root,-)
%doc COPYING
%doc %{_datadir}/omf/system-config-users
%doc %{_datadir}/gnome/help/system-config-users

%changelog
* Tue Mar 23 2010 Nils Philippsen <nils@redhat.com> - 1.0.8-1
- pick up translation updates

* Mon Sep 28 2009 Nils Philippsen <nils@redhat.com> - 1.0.7-1
- pick up new translations

* Wed Aug 26 2009 Nils Philippsen <nils@redhat.com>
- explain obsoleting old versions

* Thu May 28 2009 Nils Philippsen <nils@redhat.com>
- use simplified source URL

* Tue Apr 14 2009 Nils Philippsen <nils@redhat.com> - 1.0.6-1
- add sr@latin structure (#495293, sr@latin.po by Miloš Komarčević)
- pick up updated translations

* Wed Apr 08 2009 Nils Philippsen <nils@redhat.com> - 1.0.5-1
- pull in updated translations

* Thu Dec 18 2008 Nils Philippsen <nils@redhat.com> - 1.0.4-1
- use non-colored rarian-compat requirement

* Wed Dec 17 2008 Nils Philippsen <nils@redhat.com>
- add yelp dependency

* Mon Dec 08 2008 Nils Philippsen <nils@redhat.com> - 1.0.3-1
- remove unnecessary "Conflicts: system-config-users < 1.2.82"

* Fri Nov 20 2008 Nils Philippsen <nils@redhat.com> - 1.0.2-1
- separate documentation from system-config-users
- remove stuff not related to documentation
- add source URL
