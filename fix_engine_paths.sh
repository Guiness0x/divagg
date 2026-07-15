#!/bin/bash

find ~/divagg/engine \
-type f \
-name "*.py" \
-exec sed -i \
's/parent\.parent/parent.parent.parent/g' {} +

echo "DIVAGG ENGINE PATH REWRITE COMPLETE"
