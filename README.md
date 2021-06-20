# bat.rpm

An RPM spec for the [bat](https://github.com/sharkdp/bat) utility.

## Building

To build, you will need two packages on a Fedora or Rocky Linux machine:

- `mock`
- `rpmdevtools`

Once you have cloned the repository into your rpmbuild/ directory, you can
perform the steps required to build the package.

```shell
# build srpm
$ rpmbuild -bs SPECS/bat.spec

# build rpm with mock
$ mock -r epel-8-x86_64 --rebuild SRPMS/bat-*.src.rpm
```

With this command, your output should be in
`/var/lib/mock/epel-8-x86_64/result/`. This should include a `build.log` and
`bat-*.rpm` file. You can install said `.rpm` file with `rpm`.

