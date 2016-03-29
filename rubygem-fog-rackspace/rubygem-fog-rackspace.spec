%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name fog-rackspace

Summary: Module for the 'fog' gem to support Rackspace
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: 0.1.1
Release: 1%{?dist}
Group: Development/Ruby
License: MIT
URL: http://github.com/fog/fog-rackspace
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix}rubygem(fog-core) >= 1.35
Requires: %{?scl_prefix}rubygem(fog-json) >= 1.0
Requires: %{?scl_prefix}rubygem(fog-xml) >= 0.1
Requires: %{?scl_prefix}rubygem(ipaddress) >= 0.8
Requires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%define gembuilddir %{buildroot}%{gem_dir}

%description
Rackspace provider gem for Fog.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -T -c

%build

%install
mkdir -p %{gembuilddir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0} --no-rdoc --no-ri
%{?scl:"}

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE.txt

%files doc
%{gem_instdir}/CODE_OF_CONDUCT.md
%{gem_instdir}/README.md
%{gem_instdir}/tests
%{gem_instdir}/Gemfile*
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/bin
%exclude %{gem_instdir}/%{gem_name}.gemspec

%changelog
* Wed Mar 09 2016 Dominic Cleal <dominic@cleal.org> 0.6.3-1
- Update fog-vsphere to 0.6.3 (dominic@cleal.org)

* Fri Mar 04 2016 Dominic Cleal <dominic@cleal.org> 0.6.1-1
- Update fog-vsphere to 0.6.1 (dominic@cleal.org)

* Mon Feb 01 2016 Dominic Cleal <dcleal@redhat.com> 0.6.0-1
- Update fog-vsphere to 0.6.0 (dcleal@redhat.com)

* Tue Jan 19 2016 Dominic Cleal <dcleal@redhat.com> 0.5.0-1
- new package built with tito
