Name:           sshproxy
Version:        1.6.3
Release:        1%{?dist}
Summary:        Proxy SSH connections on a gateway

URL:            https://github.com/cea-hpc/%{name}
License:        CeCILL-B
Source0:        https://github.com/cea-hpc/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  golang asciidoc

Provides:       %{name} = %{version}

%description
sshproxy is used on a gateway to transparently proxy a user SSH connection on
the gateway to an internal host via SSH. scp, sftp, rsync, etc. are supported.

%global debug_package %{nil}

%prep
%autosetup

%build
go build  -mod=vendor -ldflags "-X main.SshproxyVersion=%{version}" -o bin/%{name} github.com/cea-hpc/sshproxy/cmd/%{name}
go build  -mod=vendor -ldflags "-X main.SshproxyVersion=%{version}" -o bin/%{name}-dumpd github.com/cea-hpc/sshproxy/cmd/%{name}-dumpd
go build  -mod=vendor -ldflags "-X main.SshproxyVersion=%{version}" -o bin/%{name}-replay github.com/cea-hpc/sshproxy/cmd/%{name}-replay
go build  -mod=vendor -ldflags "-X main.SshproxyVersion=%{version}" -o bin/%{name}ctl github.com/cea-hpc/sshproxy/cmd/%{name}ctl
a2x -asshproxy_version=%{version} -f manpage doc/sshproxy.yaml.txt
a2x -asshproxy_version=%{version} -f manpage doc/sshproxy.txt
a2x -asshproxy_version=%{version} -f manpage doc/sshproxy-dumpd.txt
a2x -asshproxy_version=%{version} -f manpage doc/sshproxy-replay.txt
a2x -asshproxy_version=%{version} -f manpage doc/sshproxyctl.txt

%install
install -dpm 0755                     %{buildroot}%{_mandir}/man8/
install -dpm 0755                     %{buildroot}%{_sharedstatedir}/%{name}
install -dpm 0755                     %{buildroot}%{_localstatedir}/log/%{name}
install -dpm 0755                     %{buildroot}%{_datadir}/licenses/%{name}
install -Dpm 0755 bin/%{name}         %{buildroot}%{_sbindir}/%{name}
install -Dpm 0755 bin/%{name}-dumpd   %{buildroot}%{_sbindir}/%{name}-dumpd
install -Dpm 0755 bin/%{name}-replay  %{buildroot}%{_bindir}/%{name}-replay
install -Dpm 0755 bin/%{name}ctl      %{buildroot}%{_bindir}/%{name}ctl
install -Dpm 0644 config/%{name}.yaml %{buildroot}%{_sysconfdir}/%{name}/%{name}.yaml
install -Dpm 0644 doc/*.8             %{buildroot}%{_mandir}/man8/
install -Dpm 0644 Licence_*.txt       %{buildroot}%{_datadir}/licenses/%{name}

%files
%dir %{_sysconfdir}/%{name}
%dir %{_sharedstatedir}/%{name}
%dir %{_localstatedir}/log/%{name}
%{_sbindir}/%{name}
%{_sbindir}/%{name}-dumpd
%{_bindir}/%{name}-replay
%{_bindir}/%{name}ctl
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.yaml
%{_datadir}/licenses/%{name}/*
%{_mandir}/man8/*


%changelog
* Wed Feb 12 2025 Ariel L - 1.6.3-1
- first release
