Name:       bat
Version:    0.18.1
Release:    1%{?dist}
Summary:    A cat(1) clone with wings.

License:    APL2.0+ or MIT
URL:        https://github.com/sharkdp/%{name}
Source0:    https://github.com/sharkdp/%{name}/releases/download/v%{version}/%{name}-v%{version}-x86_64-unknown-linux-gnu.tar.gz

BuildArch:  x86_64

%description
A cat(1) clone with syntax highlighting and Git integration.

%prep
%setup -q -n %{name}-v%{version}-x86_64-unknown-linux-gnu

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -D -p -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%license LICENSE-APACHE LICENSE-MIT
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%changelog
* Sun Jun 20 2021 Hayden Young <hi@hbjy.dev>
- Create initial package for `bat` utility.

