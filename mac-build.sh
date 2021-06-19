#!/bin/bash
DIR=$(dirname "${BASH_SOURCE[0]}")
mkdir "$DIR/app"
cp -r "$DIR/mac-build" "$DIR/app/Contents"
cp -r "$DIR/scheduler" "$DIR/app/Contents/MacOS/scheduler"
LINE=$(head -1 "$DIR/app/Contents/MacOS/scheduler/version.txt")
sed -i "" "s/VERSION/$LINE/g" "$DIR/app/Contents/Info.plist"
ln -s /System/Library/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/MacOS/Python "$DIR/app/Contents/MacOS/pylink"
compgen -G "/Library/Frameworks/Python.framework/Versions/3*/Resources/Python.app/Contents/MacOS/Python" | xargs -I{} ln -s -f {} "$DIR/app/Contents/MacOS/pylink"
mv "$DIR/app" "$DIR/Scheduler.app"
echo "Scheduler has been built! You may move it to your Applications folder and then discard the rest of the project files."
