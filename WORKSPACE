workspace(name = "verkada_backend")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "rules_python",
    sha256 = "9acc0944c94adb23fba1c9988b48768b1bacc6583b52a2586895c5b7491e2e31",
    strip_prefix = "rules_python-0.27.0",
    url = "https://github.com/bazelbuild/rules_python/archive/refs/tags/0.27.0.tar.gz",
)

load("@rules_python//python:repositories.bzl", "py_repositories", "python_register_toolchains")

py_repositories()

python_register_toolchains(
    name = "python3_9",
    # Available versions are listed in @rules_python//python:versions.bzl.
    python_version = "3.9.18",
    register_coverage_tool = True,
)

load("@rules_python//python:pip.bzl", "pip_parse")

pip_parse(
    name = "pip_deps",
    requirements_lock = "//:requirements_lock.txt",
)

load("@pip_deps//:requirements.bzl", "install_deps")

install_deps()

http_archive(
    name = "com_github_linux_test_project_lcov",
    build_file_content = """

exports_files(
    ["bin/genhtml"]
)

filegroup(
    name = "bin",
    srcs = glob(["bin/*"]),
    visibility = ["//visibility:public"],
)

filegroup(
    name = "lib",
    srcs = glob(["lib/*"]),
    visibility = ["//visibility:public"],
)
""",
    sha256 = "35866dd6a145dd50d9dccf2eeb7481312cfdb56c733d783074df097013acf6e3",  # pragma: allowlist secret
    strip_prefix = "lcov-950771ee234fdabae3fe75281dd7b2d636e47e07",
    urls = [
        "https://github.com/linux-test-project/lcov/archive/950771ee234fdabae3fe75281dd7b2d636e47e07.zip",
    ],
)
