import datetime


def release_schedule() -> tuple:
    """Chromium release schedule

    https://chromiumdash.appspot.com/schedule
    """
    schedule = (
        ('Jan 28, 2025', 133),
        ('Dec 17, 2024', 132),
        ('Nov 12, 2024', 131),
        ('Oct 15, 2024', 130),
        ('Sep 17, 2024', 129),
        ('Aug 20, 2024', 128),
        ('Jul 23, 2024', 127),
        ('Jun 11, 2024', 126),
        ('May 14, 2024', 125),
        ('Apr 16, 2024', 124),
        ('Mar 19, 2024', 123),
        ('Feb 20, 2024', 122),
        ('Jan 23, 2024', 121),
        ('Dec 5, 2023', 120),
        ('Oct 31, 2023', 119),
        ('Oct 10, 2023', 118),
        ('Sep 12, 2023', 117),
        ('Aug 15, 2023', 116),
        ('Jul 18, 2023', 115),
        ('May 30, 2023', 114),
        ('May 2, 2023', 113),
        ('Apr 4, 2023', 112),
        ('Mar 7, 2023', 111),
        ('Feb 7, 2023', 110),
        ('Jan 10, 2023', 109)
    )

    return schedule


def unified_platform() -> str:
    """platform part of user-agent

    macOS:   'Macintosh; Intel Mac OS X 10_15_7'
    windows: 'Windows NT 10.0; Win64; x64'
    linux:   'X11; Linux x86_64'

    https://chromium.googlesource.com/chromium/src.git/+/refs/heads/main/content/common/user_agent.cc
    """
    platform = 'Macintosh; Intel Mac OS X 10_15_7'

    return platform


def major_version(now: datetime.datetime | None = None) -> int:
    """Major version of Chrome Browser"""

    if now is None:
        now = datetime.datetime.now(datetime.timezone.utc)

    schedule = release_schedule()
    version = 100

    for item in schedule:
        if now.date() > datetime.datetime.strptime(item[0], '%b %d, %Y').date():
            version = item[1]
            break

    return version


def user_agent(major_ver: int | None = None) -> str:
    """Return the user-agent of Chrome Browser"""

    if major_ver is None:
        major_ver = major_version()

    agent = 'Mozilla/5.0 ({}) AppleWebKit/537.36 (KHTML, like Gecko) ' \
            'Chrome/{}.0.0.0 Safari/537.36'

    return agent.format(unified_platform(), major_ver)
