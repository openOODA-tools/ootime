Name:           ootime
Version:        0.1.0
Release:        1%{?dist}
Summary:        High-resolution process execution timing, memory high-watermark, and cgroup metering.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ootime
Source0:        ootime-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ootime is a sovereign, capability-bounded RESOURCE PROFILER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ootime
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ootime-uninstall

%files
/usr/bin/ootime
/usr/bin/ootime-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
