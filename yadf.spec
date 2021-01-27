#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : yadf
Version  : 0.12.2
Release  : 1
URL      : file:///insilications/build/clearlinux/packages/yadf/yadf-v0.12.2.tar.gz
Source0  : file:///insilications/build/clearlinux/packages/yadf/yadf-v0.12.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: yadf-bin = %{version}-%{release}
Requires: regex
BuildRequires : ca-certs
BuildRequires : ca-certs-static
BuildRequires : grep
BuildRequires : openssl
BuildRequires : openssl-dev
BuildRequires : regex
BuildRequires : rustc
BuildRequires : rustc-bin
BuildRequires : rustc-data
BuildRequires : rustc-dev
BuildRequires : rustc-staticdev
BuildRequires : termcolor
BuildRequires : time
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# YADF — Yet Another Dupes Finder
> _It's [fast](#benchmarks) on my machine._
## Installation

%package bin
Summary: bin components for the yadf package.
Group: Binaries

%description bin
bin components for the yadf package.


%prep
%setup -q -n yadf
cd %{_builddir}/yadf

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
RUSTFLAGS="-C target-cpu=native"
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
cargo update --verbose

%install
RUSTFLAGS="-C target-cpu=native"
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
RUSTFLAGS="-C target-cpu=native" cargo install --verbose --no-track --path . --root %{buildroot}/usr/
## install_append content
# shell completion for bash
# install -dm 0755 %{buildroot}/usr/share/bash-completion/completions
# install -m0644 ./target/release/build/ripgrep-*/out/rg.bash %{buildroot}/usr/share/bash-completion/completions/rg
# rm -rf ./target/release/build/ripgrep-*/out/rg.bash
# man docs
# install -dm 0755 %{buildroot}/usr/share/man/man1
# install -m0644 ./target/release/build/ripgrep-*/out/rg.1 %{buildroot}/usr/share/man/man1/rg.1
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/yadf
