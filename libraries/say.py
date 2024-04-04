import cowsay
import sys

from sayings import hello
from sayings import goodbye


# Below is for cowsay
# if len(sys.argv) == 2:
#     # cowsay.cow("hello, " + sys.argv[1])
#     cowsay.trex("hello, " + sys.argv[1])


# Below is for sayings

if len(sys.argv) == 2:
    # hello(sys.argv[1])
    goodbye(sys.argv[1])
