from subprocess import run
from sys import executable


check_list = [
    [executable, "-m", "unittest"],
    ["mypy", "-p", "src.addressable_sql_queries"],
    ["mypy", "-p", "src.addressable_sql_queries.__main__"],
    ["coverage", "erase"],
    ["coverage", "run", "-m", "unittest"],
    ["coverage", "html", "-i"],
    ["coverage", "report", "--fail-under=100"],

]

failing_check_list = [
    [executable, "-m", "src.addressable_sql_queries"],

]

if __name__ == "__main__":
    for cmd in check_list:
        if run(cmd).returncode != 0:
            exit(1)
    print("Tests succeeded correctly.")
    for cmd in failing_check_list:
        if run(cmd).returncode == 0:
            exit(1)
    print("Tests correctly failed.")
    if run([executable, "-m", "build"]).returncode == 0:
        print("Build finished successfully.")
    else:
        print("Build failed.")
        exit(1)
