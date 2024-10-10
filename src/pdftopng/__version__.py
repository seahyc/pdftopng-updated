# -*- coding: utf-8 -*-

VERSION = (0, 2, 3)
PRERELEASE = None  # alpha, beta or rc
REVISION = None


def generate_version(version, prerelease=None, revision=None):
    version_parts = [".".join(map(str, version))]
    if prerelease is not None:
        version_parts.append(f"-{prerelease}")
    if revision is not None:
        version_parts.append(f".{revision}")
    return "".join(version_parts)


__title__ = "pdftopng"
__description__ = "A PDF to PNG conversion library."
__url__ = "https://github.com/seahyc/pdftopng-updated"
__version__ = generate_version(VERSION, prerelease=PRERELEASE, revision=REVISION)
__author_email__ = "seahyingcong@gmail.com"
__author__ = "Seah Ying Cong"
__license__ = "GPL-2.0"
