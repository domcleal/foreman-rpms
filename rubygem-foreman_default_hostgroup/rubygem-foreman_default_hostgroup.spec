# This package contains macros that provide functionality relating to
# Software Collections. These macros are not used in default
# Fedora builds, and should not be blindly copied or enabled.
# Specifically, the "scl" macro must not be defined in official Fedora
# builds. For more information, see:
# http://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation
# /1/html/Software_Collections_Guide/index.html

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_default_hostgroup

%define rubyabi 1.9.1
%global foreman_dir /usr/share/foreman
%global foreman_bundlerd_dir %{foreman_dir}/bundler.d
%global foreman_pluginconf_dir /etc/foreman/plugins

Summary:    Default Hostgroup Plugin for Foreman
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    3.0.0
Release:    1%{?dist}
Group:      Applications/System
License:    GPLv3
URL:        http://github.com/GregSutcliffe/foreman_default_hostgroup
Source0:    http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires:   foreman >= 1.5.0

%if 0%{?fedora} > 18
Requires: %{?scl_prefix_ruby}ruby(release)
%else
Requires: %{?scl_prefix_ruby}ruby(abi) >= %{rubyabi}
%endif
Requires: %{?scl_prefix_ruby}rubygems

%if 0%{?fedora} > 18
BuildRequires: %{?scl_prefix_ruby}ruby(release)
%else
BuildRequires: %{?scl_prefix_ruby}ruby(abi) >= %{rubyabi}
%endif
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems

BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-default-hostgroup

Obsoletes: ruby193-rubygem-%{gem_name}

%description
Adds the option to specify a default hostgroup for new hosts created from
facts/reports.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0} --no-rdoc --no-ri
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{foreman_bundlerd_dir}
cat <<GEMFILE > %{buildroot}%{foreman_bundlerd_dir}/%{gem_name}.rb
gem '%{gem_name}'
GEMFILE

mkdir -p %{buildroot}%{foreman_pluginconf_dir}
mv %{buildroot}%{gem_instdir}/default_hostgroup.yaml.example \
   %{buildroot}%{foreman_pluginconf_dir}/%{gem_name}.yaml.example

%files
%dir %{gem_instdir}
%{gem_instdir}/app
%{gem_instdir}/lib
%exclude %{gem_cache}
%exclude %{gem_instdir}/test
%{gem_spec}
%{foreman_bundlerd_dir}/%{gem_name}.rb
%doc %{foreman_pluginconf_dir}/%{gem_name}.yaml.example
%doc %{gem_instdir}/LICENSE

%exclude %{gem_dir}/cache/%{gem_name}-%{version}.gem

%files doc
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md

%changelog
* Mon Dec 15 2014 Dominic Cleal <dcleal@redhat.com> 3.0.0-1
- Update foreman_default_hostgroup to 3.0.0 (dcleal@redhat.com)

* Wed Apr 30 2014 Dominic Cleal <dcleal@redhat.com> 2.0.1-1
- Update to v2.0.1, add example config file (dcleal@redhat.com)

* Tue Apr 29 2014 Dominic Cleal <dcleal@redhat.com> 2.0.0-1
- Update to v2.0.0 (dcleal@redhat.com)

* Mon Feb 10 2014 Dominic Cleal <dcleal@redhat.com> 1.1.0-1
- Update to v1.1.0 (dcleal@redhat.com)

* Fri Oct 04 2013 Dominic Cleal <dcleal@redhat.com> 1.0.0-1
- new package built with tito

