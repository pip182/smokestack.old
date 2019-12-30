#!/usr/bin/python

import subprocess
import sys
from time import sleep, time


# Colors for the command line
class colors:
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'

    class fg:
        red = '\033[31m'
        orange = '\033[33m'
        cyan = '\033[36m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'


# Check to see if we have the needed requirements and try to install them if not.
try:
    import sass
    from watchdog.observers import Observer
    from watchdog.events import PatternMatchingEventHandler
except Exception:
    good_result = False
    print("\nWe need libsass and watchdog, I'll attempt to install them for you...\n")
    print("\nYou should install it locally if using a virtual environment or globally if not.\n")
    while not good_result:
        result = input("\nShould this be installed (G)lobally or (L)ocally?:")
        result = result.lower()
        if result == "g" or result == "l":
            good_result = True
        else:
            print("\nPlease input either 'g' or 'l'.\n")
    if result == 'g':
        try:
            subprocess.check_call("sudo -H pip install watchdog libsass", shell=True)
        except subprocess.CalledProcessError:
            try:
                print("\nI can't use 'sudo' here, I will try to install it locally then.\n ")
                subprocess.check_call("pip install watchdog libsass", shell=True)
            except subprocess.CalledProcessError:
                print("""\nWell that didn't work either... you'll have to install them manually
                    Try running: {0}pip install libsass watchdog{1}\n""".format(
                    colors.fg.lightcyan, colors.reset))
                print("""{0}{1}If there was a permission error during compilation you will need to run:
                    {2}sudo pip install libsass{3}\n\n""".format(
                    colors.underline, colors.fg.lightred, colors.fg.yellow, colors.reset))
                input("Press Enter to continue...")
                quit()
    elif result == "l":
        subprocess.check_call("pip install watchdog libsass", shell=True)
    print("\nRequirements installed! Please re run the script!")
    quit()


# The directory containing the SASS files we want to compile.
source_dir = 'smokestack/static/sass/'

# Where we want the compiled CSS files to go.
output_dir = 'smokestack/static/css/'

# The files to build, their compression types and if only the listed file should be built.
# Format: (NAME, OUTPUT_STYLE, SINGLE_FILE)
filenames = (('styles', 'compressed', False),)
            #  ('theme.dark', 'compressed', True),
            #  ('theme.light', 'compressed', True),
            #  ('print', 'expanded', True),
            #  ('print_pdf', 'expanded', True))


def build(filenames, src_path="", build_all=False):
    "This is what actually builds the CSS files."

    # Possibly need to wait a little bit for the file to be completly saved since once in
    # a while it will complain that the file can't be accessed. 1/4 second should be more
    # than enough time but this can be adjusted.
    sleep(0.25)

    start = time()
    for name, output, single in filenames:
        if build_all or not single or "{0}.scss".format(name) in src_path:
            with open('{0}{1}.css'.format(output_dir, name), 'w') as file:
                file.write(sass.compile(
                    filename='{0}{1}.scss'.format(source_dir, name),
                    output_style=output))
                file.close()
                print("{0} has been compiled and {1}!".format(file.name, output))
    end = time()
    print("Took {0} milliseconds to complete.\n".format(round((end - start) * 1000, 4)))


class SassWatcher(PatternMatchingEventHandler):
    patterns = ["*"]

    def __init__(self):
        self._ignore_directories = False
        self._ignore_patterns = ""
        self._case_sensitive = False

    def on_any_event(self, event):
        "This is the code that gets executed when a change is detected."

        print("\n{0} was changed, compiling...".format(event.src_path))
        build(filenames, event.src_path)


if __name__ == '__main__':
    observer = Observer()
    observer.schedule(SassWatcher(), path=source_dir, recursive=True)

    print("\nBuilding CSS files!\n")
    build(filenames, build_all=True)

    # Passing 'build' as the first argument will only compile the code and not watch for
    # changes.
    if len(sys.argv) <= 1:
        observer.start()
        print('''Watching {0} for changes...
        Press CTRL+C to stop the script.'''.format(source_dir))

        try:
            while True:
                sleep(1)
        except KeyboardInterrupt:
            print("\nKilling file watcher...")
            observer.stop()
        observer.join()

    print("Done!")
